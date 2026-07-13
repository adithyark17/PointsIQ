---
type: air-program
tags:
- program
- program/air
airline: '[[Cathay Pacific]]'
alliance: '[[oneworld]]'
currency_name: Asia Miles
pricing_model: distance
expiry: 18 months of inactivity (activity resets)
fuel_surcharges: moderate
award_chart: '[[Asia Miles Distance Chart]]'
---

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
