---
type: air-program
tags:
- program
- program/air
airline: '[[Singapore Airlines]]'
alliance: '[[Star Alliance]]'
currency_name: KrisFlyer miles
pricing_model: zone
expiry: 36 months fixed
fuel_surcharges: low
award_chart: '[[KrisFlyer Saver Chart]]'
---

The premium-cabin benchmark from India: Saver awards on SQ metal (suites/J) are near-impossible to book with anything except KrisFlyer miles. Reachable from almost every Indian transferable currency.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
