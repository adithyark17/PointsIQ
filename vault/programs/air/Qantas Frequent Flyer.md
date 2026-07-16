---
type: air-program
tags:
- program
- program/air
airline: '[[Qantas]]'
alliance: '[[oneworld]]'
currency_name: Qantas Points
pricing_model: distance
expiry: 18 months of inactivity
fuel_surcharges: high
award_chart: '[[Qantas Classic Rewards Chart]]'
---

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
