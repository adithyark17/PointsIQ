---
type: air-program
tags:
- program
- program/air
airline: '[[Iberia]]'
alliance: '[[oneworld]]'
currency_name: Avios
pricing_model: distance
expiry: 36 months of inactivity
fuel_surcharges: low
---

Same Avios currency as BA/Qatar; lower YQ on many routes.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
