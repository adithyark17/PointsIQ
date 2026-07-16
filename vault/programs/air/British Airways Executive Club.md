---
type: air-program
tags:
- program
- program/air
airline: '[[British Airways]]'
alliance: '[[oneworld]]'
currency_name: Avios
pricing_model: distance
expiry: 36 months of inactivity
fuel_surcharges: high
award_chart: '[[British Airways Avios Distance Chart]]'
---

Distance-banded. Sweet from India for short hops (BOM-DXB, DEL-BKK) on partners. Avios pool freely between BA, Qatar, Iberia, Finnair and Aer Lingus accounts.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
