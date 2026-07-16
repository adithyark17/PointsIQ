---
type: air-program
tags:
- program
- program/air
airline: '[[TAP Air Portugal]]'
alliance: '[[Star Alliance]]'
currency_name: TAP miles
pricing_model: zone
expiry: 36 months
fuel_surcharges: high
---

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
