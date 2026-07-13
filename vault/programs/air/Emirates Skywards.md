---
type: air-program
tags:
- program
- program/air
airline: '[[Emirates]]'
currency_name: Skywards Miles
pricing_model: hybrid
expiry: 36 months (extendable)
fuel_surcharges: high
award_chart: '[[Emirates Skywards Chart]]'
---

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
