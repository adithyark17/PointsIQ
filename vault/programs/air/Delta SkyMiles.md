---
type: air-program
tags:
- program
- program/air
airline: '[[Delta Air Lines]]'
alliance: '[[SkyTeam]]'
currency_name: SkyMiles
pricing_model: dynamic
expiry: never
fuel_surcharges: none
---

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
