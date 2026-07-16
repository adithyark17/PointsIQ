---
type: air-program
tags:
- program
- program/air
airline: '[[Copa Airlines]]'
alliance: '[[Star Alliance]]'
currency_name: ConnectMiles
pricing_model: zone
expiry: 24 months of inactivity
fuel_surcharges: none
---

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
