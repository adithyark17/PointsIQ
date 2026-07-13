---
type: air-program
tags:
- program
- program/air
airline: '[[Finnair]]'
alliance: '[[oneworld]]'
currency_name: Avios
pricing_model: distance
expiry: 36 months of inactivity
fuel_surcharges: moderate
---

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
