---
type: air-program
tags:
- program
- program/air
airline: '[[United Airlines]]'
alliance: '[[Star Alliance]]'
currency_name: MileagePlus miles
pricing_model: dynamic
expiry: never
fuel_surcharges: none
award_chart: '[[United MileagePlus Observed Pricing]]'
---

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
