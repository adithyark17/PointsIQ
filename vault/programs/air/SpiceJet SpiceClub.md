---
type: air-program
tags:
- program
- program/air
airline: '[[SpiceJet]]'
currency_name: SC Points
pricing_model: dynamic
fuel_surcharges: none
---

Domestic LCC program; became an Axis Group B transfer partner in April 2026.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
