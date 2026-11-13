# Meta Ad Campaign Skill

A Claude skill for end-to-end Meta (Facebook / Instagram) ad campaign setup for a Shopify store, built from Asjad's real campaigns for Fragrance Empire. Claude prepares everything — brief, campaign structure, ad copy, creative brief, pre-launch funds / Pixel / domain checks, the Ads Manager publish walkthrough, delivery check, results read and Shopify reconciliation — with the owner involved only for campaign decisions, accounts / sign-ins / money, the publish clicks in Ads Manager, and approval gates.

One honest limit up front: **Claude CANNOT create, change or publish ads.** The ad account is write-disabled for Muse/Claude (HTTP 403 verified). The skill prepares the complete publish plan so the owner can publish it in Ads Manager in minutes — it never promises to publish an ad itself.

## What it does

Takes a campaign from brief to honest report in one repeatable workflow:

1. **Brief** — campaign name, objective, offer, budget, schedule, ad set, ads. No building before the brief is confirmed.
2. **Campaign structure** — campaign, ad set, each ad, toggles, schedule, destination, written down before anyone opens Ads Manager.
3. **Ad copy + creative brief** — primary text, headline, description, call to action, destination, and the creative (20s vertical video or images), following the real campaign copy.
4. **Pre-launch checks** — billing type, Available funds, account + daily spending limits, Pixel + Maximum data sharing, domains allowlist, advertiser verification, no manual Pixel code.
5. **Ads Manager publish walkthrough** — the owner clicks, Claude guides: campaign → ad set → ad, Review and publish, unpublished changes to zero.
6. **Delivery check** — ad-level delivery status + substatuses. ACTIVE alone is not proof of delivery.
7. **Results read** — Meta figures for the exact campaign and period, with period and timezone recorded.
8. **Shopify reconciliation** — Meta's purchase count cross-checked against real store orders (timestamps vs ad start time; test orders excluded; cancelled orders inside the window counted as ad-driven but never as retained) with `scripts/reconcile_orders.py`. True cost per order and ROAS.
9. **Report + decision** — Meta figures and store figures side by side, dedup status, ROI advice, and the owner's keep / pause / scale decision.

## Who does what — Claude prepares, the owner publishes

Claude runs every preparation step — brief, structure, copy, creative brief, checklists, status decoding, results reading, order reconciliation, ROAS math. The owner is involved only at four points: (1) campaign decisions only the owner can make (offer, budget, schedule, creative, destination); (2) accounts, sign-ins and money (Meta ad account, adding funds, every Ads Manager click — all on the owner's own device); (3) the publish clicks in Ads Manager (Review and publish, then reading back the final status text); and (4) approval gates (campaign plan, copy, creative, budget, and the results report). Everything else is Claude's work — do not hand it back to the owner as homework.

## The account

- **Business:** Fragrance Empire, store fragranceempire.my, Shopify store in Malaysia (MYR).
- **Ad account:** 1649995396533273, currency MYR.
- **Pixel:** "Fragrance Empire", ID 1462430982679469, data sharing MAXIMUM (Conversions API via the official Facebook & Instagram app).
- **Billing:** MANUAL (prepaid) via Touch 'n Go. Available funds must cover the campaign budget. Daily spending limit RM 460.83 (Meta-set, cannot be removed).
- **Advertiser verification:** "Asjad Farooq", Pakistan — APPROVED Nov 5, 2026.
- **Domains allowlist:** fragranceempire.my, instagram.com, facebook.com, m.facebook.com.

## The reference campaigns

**FIRST20 — Nov 2–9, 2026 (ended).** Campaign "FIRST20 - 20% Off Malaysia", Sales, lifetime RM 100; ad set "Malaysia Broad" (Malaysia, 18–65+, Purchase on Pixel 1462430982679469). Final: spend RM 92.59, 6,097 impressions, 4,154 reach, 156 clicks, Meta reported 5 purchases. **True ad-driven orders = 4** (retained 2) — order #1002 was organic, placed Nov 2 at 11:38 PKT, about 5 hours before the ad started at 16:52 PKT. True cost per ad-driven order RM 23.15, per retained order RM 46.30. ROAS 7.31 (ad-driven) / 4.00 (retained). Unspent RM 7.41 does not transfer and is not refundable.

**11.11 — Nov 10–14, 2026.** Campaign "11.11 - 50% Off Malaysia", Sales, lifetime RM 120; ad set "11.11 50% Video", one ad "11.11 Reel - 50% Off" (20s vertical video, Shop Now → fragranceempire.my), bid strategy Highest volume. Report Nov 12: spend RM 54.89/120, 1,771 impressions, 127 clicks; Meta reported 2 purchases but only **1 real order** (#1007, RM 96.39) — the 2nd was the voided test order #1008. True cost per real order RM 54.89; ROAS 1.76. Delivery once stopped with Available funds at RM 0.00 (`account_spend_limit_reached`) while the campaign still showed ACTIVE — fixed by adding RM 120 via Touch 'n Go.

## Files

```
meta-ad-campaign-skill/
├── README.md                                  # this file
└── meta-ad-campaign/
    ├── SKILL.md                               # the Claude skill — the workflow itself
    ├── scripts/
    │   └── reconcile_orders.py                # Meta purchases vs Shopify orders: true cost per order + ROAS
    └── templates/
        ├── campaign-brief.md                  # blank campaign brief
        ├── ad-copy-template.md                # primary text / headline / description / CTA / destination
        ├── pre-launch-checklist.md            # funds, limits, Pixel, domains, verification, toggles
        └── results-report.md                  # Meta figures vs store orders, dedup status, decision
```

## Setup

### 1. Read access (no writes needed)

Claude reads the ad account through the Meta Business Manager connector (campaigns, ad sets, ads, spend, results, Pixels, Events Manager) and reads store orders through the Shopify connector. Both are read-only for this skill. The skill never needs write access, and the account is write-disabled for Muse/Claude anyway — do not try to work around that.

### 2. The owner keeps the publish clicks

Publishing happens in Ads Manager (https://business.facebook.com/adsmanager) on the owner's own device, with the owner's sign-in. Claude gives the complete publish plan in one message first, then walks the owner through it level by level. Never paste passwords or payment details into the skill files, into chat, or into the repo — they live only in the owner's secure storage.

### 3. Use in Claude

Copy the `meta-ad-campaign/` folder into a Claude skills directory (for example a Claude Code skills folder, or a repo Claude is pointed at), or keep this whole repo and point Claude at `meta-ad-campaign/SKILL.md`. Then ask Claude to run the workflow, for example: "Plan a 11.11-style sale campaign for Fragrance Empire using the meta-ad-campaign skill."

## Honest limits — read before using

- **Claude cannot create, change or publish ads.** The account is write-disabled (HTTP 403 verified). The skill prepares the publish plan; the owner publishes in Ads Manager. Never claim otherwise.
- **ACTIVE does not prove delivery.** Always check ad-level delivery status + substatuses. A campaign can show ACTIVE while delivery is off because funds ran out.
- **Meta charges per impression / click, never per purchase.** A wrong purchase count is a tracking problem, not an overcharge.
- **Meta's purchase count is not the order count.** Always reconcile against Shopify orders before reporting attribution, cost per order or ROAS. Orders placed before the ad started are organic; test orders never count; cancelled orders inside the window count as ad-driven but never as retained.
- **No credentials in the skill.** No API keys, passwords, access tokens or secrets are stored in these files. If a step needs a login or a payment, the owner does it on their own device.
- **Approval gate is mandatory.** Nothing is published until the owner approves the exact campaign plan, ad copy, creative, budget and schedule. A changed budget, copy or creative needs fresh approval.
- **Leftover budget does not transfer.** Unspent lifetime budget from one campaign does not move to the next and is not refunded (it was never charged).

## How to run one campaign

1. Fill in the brief (Step 1) and get the owner to confirm it.
2. Write the campaign structure and ad copy (Steps 2–3) and get the owner's approval.
3. Complete the pre-launch checklist with the owner (Step 4) — funds, limits, Pixel, domains, verification.
4. Walk the owner through Ads Manager (Step 5) — campaign → ad set → ad, Review and publish, unpublished changes to zero.
5. Check delivery at ad level (Step 6) — ACTIVE alone is not proof.
6. Read Meta results (Step 7), reconcile against Shopify orders with `scripts/reconcile_orders.py` (Step 8), report with true costs and ROAS (Step 9).
