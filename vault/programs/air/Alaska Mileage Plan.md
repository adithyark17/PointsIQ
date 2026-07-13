---
type: air-program
tags:
- program
- program/air
airline: '[[Alaska Airlines]]'
alliance: '[[oneworld]]'
currency_name: Mileage Plan miles
pricing_model: zone
expiry: 24 months of inactivity
fuel_surcharges: low
---

Distance/zone hybrid with stopovers on one-ways; strong Asia sweet spots.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
