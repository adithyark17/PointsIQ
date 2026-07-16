---
type: air-program
tags:
- program
- program/air
airline: '[[Vietnam Airlines]]'
alliance: '[[SkyTeam]]'
currency_name: Lotusmiles
pricing_model: zone
expiry: 36 months
fuel_surcharges: moderate
---

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
