---
type: air-program
tags:
- program
- program/air
aliases:
- Virgin Atlantic Flying Club
airline: '[[Virgin Atlantic]]'
alliance: '[[SkyTeam]]'
currency_name: Virgin Points
pricing_model: zone
expiry: never
fuel_surcharges: high
---

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
