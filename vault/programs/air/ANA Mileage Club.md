---
type: air-program
tags:
- program
- program/air
airline: '[[ANA]]'
alliance: '[[Star Alliance]]'
currency_name: ANA miles
pricing_model: zone
expiry: 36 months fixed
fuel_surcharges: moderate
---

Round-trip-only awards; superb value India → Japan in J.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
