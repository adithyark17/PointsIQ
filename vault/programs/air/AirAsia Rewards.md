---
type: air-program
tags:
- program
- program/air
airline: '[[AirAsia]]'
currency_name: AirAsia points
pricing_model: dynamic
expiry: 36 months
fuel_surcharges: none
---

Revenue-linked LCC program; an Axis Group B partner since 2024.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
