---
type: air-program
tags:
- program
- program/air
airline: '[[Japan Airlines]]'
alliance: '[[oneworld]]'
currency_name: JAL miles
pricing_model: distance
expiry: 36 months fixed
fuel_surcharges: moderate
---

Distance-based partner chart is one of aviation's best-value charts.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
