---
type: air-program
tags:
- program
- program/air
airline: '[[Air France]]'
alliance: '[[SkyTeam]]'
currency_name: Flying Blue miles
pricing_model: dynamic
expiry: 24 months of inactivity
fuel_surcharges: moderate
award_chart: '[[Flying Blue India Sweet Spots]]'
---

Monthly Promo Rewards (25-50% off) regularly include Indian gateways — the cheapest Europe J from India when they hit.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
