---
name: meta-ad-campaign
description: End-to-end Meta (Facebook/Instagram) ad campaign setup for a Shopify store — Claude prepares everything for the campaign (brief, structure, ad copy, creative brief, pre-launch funds/Pixel/domain checks) so the owner can publish it in Ads Manager in minutes, then reads results honestly and reconciles Meta's purchase count against real Shopify orders. Claude CANNOT create, change or publish ads — the account is write-disabled — so the owner always does the publish clicks in Ads Manager. Modeled on the live Fragrance Empire campaigns FIRST20 (Nov 2-9, 2026) and 11.11 (Nov 10-14, 2026). Use when the user asks to plan, set up, launch, check or report on a Meta ad campaign, or when Meta's purchase count disagrees with store orders.
---

# Meta Ad Campaign Setup

## When to use

Use this skill when the user asks to plan, set up, launch, check or report on a Meta (Facebook / Instagram) ad campaign for a Shopify store — or asks why Meta's purchase count does not match the store's orders, why an ad is not delivering, or whether a campaign made money.

Do not use it for Google ads, TikTok ads, or organic social posts (use the social-content-plan skill for organic posts), unless the user explicitly asks to adapt it.

## Who does what — Claude prepares everything, the owner publishes

Claude runs every preparation step below — brief, campaign structure, ad copy, creative brief, pre-launch checks, the Ads Manager walkthrough, delivery check, results read, Shopify reconciliation and the report. The owner is involved at these points:

1. **Campaign decisions only the owner can make** — the offer, the budget, the schedule, the creative (video / images), and the destination. Claude drafts everything; the owner supplies the facts and approves them.
2. **Accounts, sign-ins and money** — the Meta ad account, adding funds, and every click in Ads Manager. These happen on the owner's own device, with the owner's own sign-in. Claude never handles the owner's password, payment details, or ad account credentials.
3. **The publish clicks in Ads Manager** — the owner presses Review and publish and reads back the final status text. Claude cannot do this step (see Hard limits).
4. **Approval gates** — the owner approves the exact campaign plan, ad copy, creative and budget before anything is published, and approves the results report before any decision (keep / pause / scale) is acted on.

Two device-bound exceptions, stated honestly so the "end to end" claim is not overstated:

- **Ads Manager publish:** Claude works through the owner's Ads Manager (browser, with the owner's sign-in). Claude prepares the complete publish plan — campaign, ad set, each ad, toggles, schedule, destination — and walks the owner through it click by click. Claude never claims a draft campaign exists in Ads Manager, because it cannot create one.
- **Billing and funds figures:** the owner reads the billing type, Available funds, account spending limit and daily spending limit from the billing screen and reports them back. Claude never guesses these figures.

Everything else — research, copy, creative briefs, checklists, status decoding, results reading, order reconciliation, ROAS math — is Claude's work. Do not hand any of it back to the owner as homework.

## Account facts — the live reference account (do not invent others)

- **Business:** Fragrance Empire, store fragranceempire.my, Shopify store in Malaysia (MYR).
- **Ad account:** 1649995396533273, currency MYR, in the "Fragrance Empire" business portfolio.
- **Pixel:** "Fragrance Empire", ID 1462430982679469, connected, data sharing MAXIMUM (Conversions API via the official Facebook & Instagram app).
- **Billing:** MANUAL (prepaid) via Touch 'n Go. Available funds must cover the campaign budget — with Available funds at RM 0.00, ads do not deliver. Daily spending limit RM 460.83 (Meta-set, cannot be removed by the owner; it rises over time).
- **Advertiser verification:** "Asjad Farooq", country Pakistan — APPROVED Nov 5, 2026.
- **Domains allowlist (Events Manager → Traffic permissions):** fragranceempire.my, instagram.com, facebook.com, m.facebook.com (each "and subdomains").
- **Pixel history:** a manual Pixel loader in theme.liquid plus Conversions API together caused duplicate Purchase events. The manual Pixel was REMOVED from theme.liquid on Nov 11, 2026; the domain-verification meta tag was kept. Only the official app sends Pixel / Conversions API events now.
- **Meta support case (duplicate purchases):** 1151478110603366. Match quality 9.3/10. Event coverage 50% vs Meta minimum 75% (Browser Event ID 50%, Server 100%) at the Nov 13, 2026 check; the Event Deduplication tab loads but shows no 'Deduplicated' status yet.

## The reference campaigns (do not invent others)

### FIRST20 — Nov 2–9, 2026 (ended)

- Campaign "FIRST20 - 20% Off Malaysia" (ID 52538496705307), Sales objective, **lifetime RM 100**.
- Ad set "Malaysia Broad" (ID 52538496705507): Malaysia only, 18–65+, Purchase conversion on Pixel 1462430982679469.
- Two ads ran: "Dewaali offer" (ID 52538707230707, bundle posters → /collections/bundles) and "FIRST20 Storewide" (ID 52538496705707).
- **Final verified figures (Nov 10, 2026):** spend **RM 92.59**, impressions 6,097, reach 4,154, clicks 156, Meta reported **5 purchases**.
- **The correction that matters:** order #1002 was ORGANIC, not ad-driven — placed Nov 2 at 11:38 PKT, about 5 hours BEFORE the ad started at 16:52 PKT. True ad-driven orders = **4** (#1003, #1004, #1005, #1006; total RM 676.60); retained ad-driven = **2** (#1005 RM 218.40 + #1006 RM 152.00 = RM 370.40); cancelled ad-driven = 2 (RM 306.20).
- **True costs:** RM 23.15 per ad-driven order (92.59 / 4); RM 46.30 per retained order (92.59 / 2). ROAS: 7.31 on ad-driven value (676.60 / 92.59), 4.00 on retained value (370.40 / 92.59).
- Unspent RM 7.41 does NOT transfer to the next campaign and is not refundable — it was never charged.

### 11.11 — Nov 10–14, 2026

- Campaign "11.11 - 50% Off Malaysia" (ID 52540446749907), Sales objective, **lifetime RM 120**.
- Ad set "11.11 50% Video" (ID 52540446750107): Malaysia, 18–65+, Advantage+ placements, Website → Purchase. Bid strategy: **Highest volume** (keep it; do not change it).
- One ad: "11.11 Reel - 50% Off" (ID 52540446750307) — the owner's 20s vertical video, Shop Now → https://fragranceempire.my/.
- **Report Nov 12, 2026:** spend **RM 54.89 / 120**, impressions 1,771, clicks 127; Meta reported 2 purchases but only **1 real order** (#1007, RM 96.39, Nov 10) — the 2nd was the voided test order #1008 (RM 90). True cost per real order **RM 54.89**; ROAS 1.76 (96.39 / 54.89).
- **Blocker that stopped delivery (Nov 10):** Available funds hit RM 0.00 — delivery off, substatus `account_spend_limit_reached`, while the campaign still showed ACTIVE. Fixed when the owner added RM 120 via Touch 'n Go; delivery moved to "preparing", then delivered.

## Hard limits — state them honestly, do not work around them

- **Claude CANNOT create, change or publish ads.** The account is write-disabled for Muse/Claude (HTTP 403 verified on a pause attempt). The skill prepares everything; the OWNER publishes in Ads Manager. Never promise to publish an ad, never say a draft is ready in Ads Manager, and never say "I will publish it".
- **A campaign showing ACTIVE does NOT prove delivery.** Check the ad-level delivery status AND substatuses. A campaign can show ACTIVE while delivery is off (for example `account_spend_limit_reached` when funds are empty). Never call an ad "live / delivering" from the campaign status alone.
- **Never assume the account is postpaid and never say no funds are needed.** A MANUAL prepaid account cannot deliver with Available funds at zero. Check billing type and Available funds before launch, and check they cover at least the campaign budget.
- **Meta charges per impression / click, NEVER per purchase.** A wrong purchase count is a tracking problem, not an overcharge. Never tell the owner Meta overcharged on purchases.
- **Meta's purchase count ≠ Shopify orders.** Always cross-check orders in Shopify — order id, time, amount, status — before reporting attribution, cost per order, or ROAS. Never present Meta's purchase count as the number of orders. Orders placed before the ad started are organic; test orders never count as ad-driven; cancelled orders placed inside the ad window DO count as ad-driven (the ad drove them) but never as retained.
- **Duplicate Purchase events happen.** One order can produce 2–3 raw Purchase events (browser Pixel + server Conversions API both firing). Treat two or more raw events for one order as a possible duplicate until the Event Deduplication tab confirms otherwise. Match quality and event coverage (minimum 75%) are reported beside the dedup status.
- **No credentials in the skill.** Never put an API key, password, access token, bank detail or secret in a skill file, in chat, or in the repo. Logins, bank details and adding funds happen on the owner's own device.
- **Approval gates are mandatory.** Nothing is published until the owner approves the exact campaign plan, ad copy, creative, budget and schedule. A changed budget, copy or creative needs fresh approval.
- **Never claim a product is original / authentic unless the owner states it and takes responsibility for it.** Do not write "100% original" into ad copy on Claude's own initiative. If the products are impressions / inspired-by, say so in the store's own terms or say nothing.
- **Leftover budget does not transfer.** Unspent lifetime budget from one campaign does not move to the next campaign and is not refunded (it was never charged).

## Workflow

### Step 1 — Brief (decisions first, no building before this)

Collect and write down, in `templates/campaign-brief.md`:

1. Campaign name, objective (Sales), offer (what is on sale, the discount, the end date).
2. Budget: lifetime or daily, amount, currency. Schedule: start and end date/time (with timezone).
3. Ad set: location, age range, placements (Advantage+ or manual), optimization (Purchase), conversion location (Website), Pixel.
4. Ads: how many, creative type (video / image / carousel), the creative files, destination URL, call to action.
5. What the owner explicitly does NOT want (for example: no "100% original" claim, no second ad set yet, no budget increase without approval).
6. Billing: billing type, Available funds, account spending limit, daily spending limit — read from the billing screen by the owner before launch.

Do not start Step 2 until the brief is filled in and the owner has confirmed it. A missing budget or a missing offer end date is a blocker, not something to guess.

### Step 2 — Campaign structure

Write the full structure in the brief before anyone opens Ads Manager:

1. **Campaign:** name, objective Sales, budget type (lifetime preferred for a dated sale), total budget.
2. **Ad set:** name, location, age range, placements, optimization event (Purchase), Pixel, schedule (start / end at ad set level, not inside the ad).
3. **Ads:** one row per ad — name, creative (file name, length, ratio), primary text, headline, description, call to action, destination URL, toggle state (ON for the ads in the plan, OFF for everything else).
4. Keep it to one ad set and one or two ads for a first campaign. Do not build a second ad set "just in case" — the owner approves each one separately.

### Step 3 — Ad copy + creative brief

Write the copy using `templates/ad-copy-template.md`. Rules from the real campaigns:

1. **Primary text:** offer first, then free delivery, then COD, then the sale end date. Example (11.11, real copy): "11.11 MEGA SALE — 50% OFF, FREE delivery across Malaysia, and EXTRA 10% OFF with card payments. Cash on Delivery available. Sale ends 15 November — shop now!"
2. **Headline:** the offer, short. Example: "11.11 MEGA SALE — 50% OFF".
3. **Description:** delivery + payment in one line. Example: "FREE delivery across Malaysia • COD available".
4. **Call to action:** Shop Now. **Destination:** the store homepage (or the collection page the ad is about) — one destination per ad, no redirect chains.
5. **Creative:** video 20s vertical 9:16 (720x1280) for a video ad; images portrait for an image ad. First 5 seconds must be an unskippable hook. No price or offer text baked into the video that contradicts the copy — the copy is the source of truth for the offer.
6. **Creative route decision (before building):** an ad built from an existing post cannot have its call-to-action button edited or added later. Use a newly built ad with uploaded media when a specific call to action and destination are required. Prepare the images in numbered order plus the primary text, headline, description, call to action and destination as one pack first. A zip pack must be extracted on the device first — Ads Manager uploads individual images, not a zip file.
7. No "100% original" claim unless the owner explicitly approved it. No invented prices, reviews or guarantees.

### Step 4 — Pre-launch checks (complete before Review and publish)

Complete `templates/pre-launch-checklist.md` with the owner. Every box must be ticked before publishing:

1. **Billing type confirmed** (MANUAL prepaid or postpaid) and **Available funds** read from the billing screen. Available funds must cover at least the campaign budget — add funds first when the balance is lower.
2. **Account spending limit and daily spending limit** read as two separate figures and recorded. Do not tell the owner to remove a daily spending limit Meta set — it cannot be removed and it rises over time.
3. **Pixel selected** (1462430982679469 for Fragrance Empire) and **data sharing MAXIMUM** (Conversions API on) — verified in Events Manager, not assumed.
4. **Domains on the Events Manager allowlist** (fragranceempire.my, instagram.com, facebook.com, m.facebook.com) and Diagnostics showing no errors.
5. **Advertiser verification** current (Asjad Farooq, Pakistan — approved Nov 5, 2026; re-check if Meta asks again).
6. **No manual Pixel code** in the live theme (search theme files for `fbq` / manual loader) when the official app already sends the same events. Keep the domain-verification meta tag.
7. **Toggles and schedule** per the plan: campaign toggle ON, each planned ad's toggle ON, everything else OFF, start/end dates set at ad set level.
8. **Unpublished changes count** — must fall to zero after Review and publish.

### Step 5 — Ads Manager publish walkthrough (owner clicks, Claude guides)

This step follows the `ads_manager_publish_walkthrough` skill. Give the owner the complete publish plan in ONE message before they start clicking, naming the campaign, the ad set, each ad, its toggle state, its schedule and its destination.

1. Work through the levels in order: campaign, then ad set, then each ad — an ad cannot run while a higher level is off or unpublished.
2. Set budget and schedule at the ad set level, not inside the ad. Confirm the start and end dates there before publishing.
3. Press **Review and publish** after the toggles and schedule are set, confirm the publish, and check that the count of unpublished changes falls to zero.
4. Ask the owner to send a screenshot of the exact status text whenever a step does not match the plan, and diagnose from that text instead of guessing.
5. Decode every status before acting:
   - **Campaign off** — campaign-level problem; send the owner back to the campaign toggle, then Review and publish.
   - **In draft** — unpublished changes; send the owner to Review and publish, not to the ad itself.
   - **Processing** — Meta is applying recent changes (for example new images); tell the owner to wait, not rebuild.
   - **In review** — normal policy check, usually resolves within a day.
   - **Active** — the only state that means the ad is live (and see Step 6: still check delivery).
   - **Account spending limit reached** — a funds or limit block; send the owner to add funds or check the limits, not to rebuild the ad.
   - **Preparing** — Meta is starting delivery after a block is cleared; tell the owner to wait and check for impressions instead of changing the campaign.
   - Refresh the page before concluding a status is stuck — status text can update late after a publish.
6. When time is short: publish the version that is already built first, and build the button version afterwards, rather than holding the whole campaign for one button. Split a long guided session into one short checklist message per level when the owner is working on a phone.

### Step 6 — Delivery check (after publishing)

1. Check the **ad-level delivery status and substatuses** — not the campaign status alone. A campaign showing ACTIVE while the ad shows `account_spend_limit_reached` is NOT delivering.
2. If delivery is off with a spending-limit substatus: check Available funds first, then the daily spending limit. Add funds; do not rebuild the ad.
3. If the ad shows "preparing": wait and check for impressions; do not change the campaign.
4. Record the delivery state and the first impressions / reach figures with their date and time. Connector insights can lag behind Meta's own emails — if the numbers disagree, say so and re-check later instead of picking the bigger number.
5. If no impressions appear after a reasonable wait with funds in place, check the toggles again (campaign → ad set → ad) and the schedule before touching the creative.

### Step 7 — Results read (Meta figures only)

1. Read the Meta figures for the exact campaign and period: spend, impressions, reach, clicks, Meta-reported purchases, cost per purchase. Record the period and timezone beside each figure.
2. Do NOT report Meta's purchase count as orders, and do NOT calculate a cost per order from it. Label Meta's "cost per purchase" separately from the true cost per order (Step 8).
3. If the order count is in low single digits, pause reporting a cost per order and report spend, impressions and clicks instead until more orders arrive.
4. Never write Meta figures to memory as a ledger — re-fetch them fresh each time; they are live state.

### Step 8 — Shopify reconciliation (the true numbers)

This step follows the `meta_purchase_reconciliation` skill. Use `scripts/reconcile_orders.py` with the Shopify order list.

1. List every store order in the campaign period by order id, time, amount and status.
2. Exclude, and name plainly with the reason:
   - every order placed **before the ad started** (organic — the #1002 rule);
   - every **test order** (including a voided / cancelled test order like #1008);
   - every order placed **after the ad ended** (list separately; do not count it silently).
3. **Ad-driven orders** = placed inside the ad window, not a test order. A cancelled order placed inside the window DOES count as ad-driven — the ad drove it, the customer then cancelled — but it never counts as retained. **Retained orders** = ad-driven with status delivered / fulfilled / paid. (FIRST20: 4 ad-driven including 2 cancelled, 2 retained.)
4. Calculate: true cost per ad-driven order (spend / ad-driven count), true cost per retained order (spend / retained count), ROAS on ad-driven value and on retained value.
5. Report the Meta count and the store order count together, with the difference explained. Correct the report and the saved record together when a new check changes the count, and name the correction plainly.
6. **Dedup audit when counts disagree:** compare Browser and Server event counts for the same order — two or more raw events for one order is a possible duplicate until deduplication confirms otherwise. Check that every event for one order shares the same event id, and report when individual events fail to load instead of assuming they match. List every installed app and check whether any app besides the official Facebook & Instagram app sends Pixel or Conversions API events. Search the live theme for a manual Pixel loader and `fbq` track calls. Report the Event Deduplication tab status, the match quality figure, and the event coverage figure beside the 75% minimum. If the tab says "Still parsing", report it as inconclusive, not confirmed — re-check on a later day.
7. **Test purchase (only if the owner approves):** use the cheapest product, choose cash on delivery when no card is available so no money changes hands, cancel the test order after it is placed, record its order id, time and amount, then open Test Events and check whether the Browser and Server Purchase events show as Deduplicated. Send findings to Meta support only after the checks above are complete, with the event counts, the manual code found and the test order result.

### Step 9 — Report + decision

Complete `templates/results-report.md` and give the owner the report in one message:

1. Meta figures (with period + timezone) and store order figures side by side, with exclusions named.
2. True cost per ad-driven order, true cost per retained order, ROAS on both values.
3. Dedup status (match quality, event coverage, 'Deduplicated' or 'Still parsing' or not shown).
4. **ROI advice pattern:** too early to judge on 1 order. The real test is profit per order vs ad cost (product cost is known only to the owner / partner). Let it run 2–3 more days; reassess at about RM 60–70 spend. State the spend so far and the budget left.
5. **Decision options (owner's choice, never Claude's):** keep running, pause, scale budget, or stop. Do not change a budget or toggle on the owner's behalf.
6. Record what was decided and the date, so the next report starts from a known state.

## How to run one campaign

1. Fill in the brief (Step 1) and get the owner to confirm it.
2. Write the campaign structure and ad copy (Steps 2–3) and get the owner's approval.
3. Complete the pre-launch checklist with the owner (Step 4) — funds, limits, Pixel, domains, verification.
4. Walk the owner through Ads Manager (Step 5) — campaign → ad set → ad, Review and publish, unpublished changes to zero.
5. Check delivery at ad level (Step 6) — ACTIVE alone is not proof.
6. Read Meta results (Step 7), reconcile against Shopify orders (Step 8), report with true costs and ROAS (Step 9).
