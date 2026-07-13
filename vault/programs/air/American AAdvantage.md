---
type: air-program
tags:
- program
- program/air
airline: '[[American Airlines]]'
alliance: '[[oneworld]]'
currency_name: AAdvantage miles
pricing_model: dynamic
expiry: 24 months of inactivity
fuel_surcharges: none
---

Web Specials + no YQ on most partners; hard to earn from India.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
