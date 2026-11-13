#!/usr/bin/env python3
"""Reconcile Meta-reported purchases against real Shopify orders.

Usage:
  python3 reconcile_orders.py --orders orders.csv \
      --ad-start "2026-11-02T16:52:15+08:00" \
      --ad-end "2026-11-09T18:03:00+08:00" \
      --spend 92.59 --meta-purchases 5 [--currency RM]

Orders CSV columns (header row required):
  order_id, placed_at, value, status, note
  - order_id: the Shopify order number, e.g. 1002
  - placed_at: ISO 8601 with timezone offset, e.g. 2026-11-02T11:38:30+08:00
  - value: order total in the campaign currency (number, e.g. 152.00)
  - status: delivered | fulfilled | paid | placed | cancelled (case-insensitive)
  - note: free text; put "test" in it for test orders

Rules (from the Fragrance Empire FIRST20 / 11.11 reconciliations):
  - Orders placed BEFORE the ad start time are ORGANIC, not ad-driven
    (the #1002 rule: #1002 was placed ~5 hours before the FIRST20 ad
    started, so Meta counting it as a purchase was wrong).
  - Test orders (note contains "test") never count as ad-driven.
  - Orders placed AFTER the ad end time are listed separately, not counted.
  - Ad-driven = placed inside [ad_start, ad_end], not a test order.
    Cancelled orders placed inside the window DO count as ad-driven —
    the ad drove them, the customer then cancelled. They count toward
    the ad-driven total and value, but never toward retained.
    (FIRST20: #1003 and #1004 were cancelled yet ad-driven — 4 ad-driven
    orders, RM 676.60; only #1005 and #1006 were retained, RM 370.40.)
  - Retained = ad-driven with status delivered / fulfilled / paid.
  - Cost per ad-driven order = spend / ad-driven count.
  - Cost per retained order = spend / retained count.
  - ROAS = total order value / spend (ad-driven and retained separately).

Exit code: 0 when the reconciliation completes — a disagreement between
Meta's count and the true count is a FINDING, not a script failure.
Exit code 1 only on bad input (missing file, bad timestamp, bad number).
"""

import argparse
import csv
import sys
from datetime import datetime

RETAINED_STATUSES = {"delivered", "fulfilled", "paid"}


def parse_time(text, field, row_no):
    try:
        dt = datetime.fromisoformat(text.strip())
    except ValueError:
        sys.exit(f"ERROR row {row_no}: {field} is not ISO 8601 with timezone: {text!r}")
    if dt.tzinfo is None:
        sys.exit(f"ERROR row {row_no}: {field} has no timezone offset: {text!r}")
    return dt


def parse_value(text, field, row_no):
    try:
        value = float(text)
    except ValueError:
        sys.exit(f"ERROR row {row_no}: {field} is not a number: {text!r}")
    if value < 0:
        sys.exit(f"ERROR row {row_no}: {field} is negative: {text!r}")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--orders", required=True, help="Orders CSV file")
    parser.add_argument("--ad-start", required=True,
                        help="Ad start time, ISO 8601 with offset")
    parser.add_argument("--ad-end", required=True,
                        help="Ad end time, ISO 8601 with offset")
    parser.add_argument("--spend", required=True, type=float,
                        help="Meta spend for the campaign in the currency")
    parser.add_argument("--meta-purchases", required=True, type=int,
                        help="Purchases Meta reported for the campaign")
    parser.add_argument("--currency", default="RM",
                        help="Currency label (default: RM)")
    args = parser.parse_args()

    if args.spend <= 0:
        sys.exit("ERROR: --spend must be greater than 0")
    if args.meta_purchases < 0:
        sys.exit("ERROR: --meta-purchases cannot be negative")

    ad_start = parse_time(args.ad_start, "--ad-start", 0)
    ad_end = parse_time(args.ad_end, "--ad-end", 0)
    if ad_end < ad_start:
        sys.exit("ERROR: --ad-end is before --ad-start")

    try:
        handle = open(args.orders, newline="", encoding="utf-8")
    except OSError as exc:
        sys.exit(f"ERROR: cannot open orders file: {exc}")

    required = {"order_id", "placed_at", "value", "status", "note"}
    with handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            sys.exit("ERROR: orders file is empty")
        missing = required - {name.strip() for name in reader.fieldnames}
        if missing:
            sys.exit(f"ERROR: orders file is missing columns: {sorted(missing)}")
        orders = []
        for row_no, row in enumerate(reader, start=2):
            row = {key.strip(): (val or "").strip() for key, val in row.items()}
            if not row["order_id"]:
                sys.exit(f"ERROR row {row_no}: order_id is empty")
            orders.append({
                "id": row["order_id"],
                "placed": parse_time(row["placed_at"], "placed_at", row_no),
                "value": parse_value(row["value"], "value", row_no),
                "status": row["status"].lower(),
                "note": row["note"],
            })

    organic, test, after_end = [], [], []
    cancelled_driven = []
    ad_driven = []
    for order in orders:
        if order["placed"] < ad_start:
            organic.append((order, "placed before ad start (organic)"))
        elif order["placed"] > ad_end:
            after_end.append((order, "placed after ad end"))
        elif "test" in order["note"].lower():
            test.append((order, "test order"))
        else:
            ad_driven.append(order)
            if order["status"] == "cancelled":
                cancelled_driven.append(order)

    retained = [o for o in ad_driven if o["status"] in RETAINED_STATUSES]
    pending = [o for o in ad_driven
               if o["status"] not in RETAINED_STATUSES and o["status"] != "cancelled"]
    ad_value = sum(o["value"] for o in ad_driven)
    ret_value = sum(o["value"] for o in retained)
    cur = args.currency

    def money(amount):
        return f"{cur} {amount:,.2f}"

    print(f"Ad window: {ad_start.isoformat()} to {ad_end.isoformat()}")
    print(f"Meta spend: {money(args.spend)} | Meta-reported purchases: {args.meta_purchases}")
    print(f"Orders in file: {len(orders)}")
    print()
    print("Excluded:")
    for group in (organic, test, after_end):
        for order, reason in group:
            print(f"  #{order['id']}  {order['placed'].isoformat()}  "
                  f"{money(order['value'])}  {order['status']}  — {reason}")
    if not (organic or test or after_end):
        print("  (none)")
    print()
    print(f"Ad-driven orders: {len(ad_driven)}  total value {money(ad_value)}")
    for order in ad_driven:
        print(f"  #{order['id']}  {order['placed'].isoformat()}  "
              f"{money(order['value'])}  {order['status']}")
    print(f"Retained orders (delivered / fulfilled / paid): {len(retained)}  "
          f"total value {money(ret_value)}")
    if cancelled_driven:
        print(f"Ad-driven but cancelled: {len(cancelled_driven)} "
              f"({', '.join('#' + o['id'] for o in cancelled_driven)}) — "
              "counted as ad-driven, never as retained")
    if pending:
        print(f"Ad-driven but outcome still pending: {len(pending)} "
              f"({', '.join('#' + o['id'] for o in pending)})")
    print()
    if ad_driven:
        print(f"True cost per ad-driven order: {money(args.spend / len(ad_driven))}")
        print(f"ROAS on ad-driven value: {ad_value / args.spend:.2f}")
    else:
        print("True cost per ad-driven order: n/a (no ad-driven orders)")
        print("ROAS on ad-driven value: n/a")
    if retained:
        print(f"True cost per retained order: {money(args.spend / len(retained))}")
        print(f"ROAS on retained value: {ret_value / args.spend:.2f}")
    else:
        print("True cost per retained order: n/a (no retained orders)")
        print("ROAS on retained value: n/a")
    print()
    if args.meta_purchases == len(ad_driven):
        print("Meta count MATCHES the true ad-driven count.")
    else:
        print(f"WARNING: Meta reported {args.meta_purchases} purchases but the "
              f"true ad-driven count is {len(ad_driven)}. "
              "Do not report Meta's count as orders — see the exclusions above.")


if __name__ == "__main__":
    main()
