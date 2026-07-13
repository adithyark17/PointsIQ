---
type: air-program
tags:
- program
- program/air
airline: '[[Turkish Airlines]]'
alliance: '[[Star Alliance]]'
currency_name: Miles
pricing_model: zone
expiry: 36 months
fuel_surcharges: high
---

Cheap zone chart on paper; taxes/YQ and IT quirks temper it.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
