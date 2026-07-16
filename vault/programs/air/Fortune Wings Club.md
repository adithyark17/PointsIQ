---
type: air-program
tags:
- program
- program/air
airline: '[[Hainan Airlines]]'
currency_name: Fortune Wings points
pricing_model: zone
expiry: 36 months
fuel_surcharges: moderate
---

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
