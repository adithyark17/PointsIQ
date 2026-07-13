---
type: air-program
tags:
- program
- program/air
airline: '[[Aegean Airlines]]'
alliance: '[[Star Alliance]]'
currency_name: Miles
pricing_model: zone
expiry: 36 months
fuel_surcharges: moderate
---

Historically the cheapest Star Alliance status play.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
