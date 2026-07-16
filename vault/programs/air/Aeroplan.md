---
type: air-program
tags:
- program
- program/air
airline: '[[Air Canada]]'
alliance: '[[Star Alliance]]'
currency_name: Aeroplan points
pricing_model: zone
expiry: 18 months of inactivity
fuel_surcharges: none
award_chart: '[[Aeroplan Zone Chart]]'
---

Zone chart with no YQ and generous stopover rules (add a stopover for 5,000 pts). Strong for India → North America on Star partners.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
