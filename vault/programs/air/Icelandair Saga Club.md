---
type: air-program
tags:
- program
- program/air
airline: '[[Icelandair]]'
currency_name: Saga Points
pricing_model: dynamic
expiry: 36 months
fuel_surcharges: low
---

Relevant to Indians mainly via the Iceland stopover on transatlantic itineraries.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
