---
type: air-program
tags:
- program
- program/air
airline: '[[Air India]]'
alliance: '[[Star Alliance]]'
currency_name: Maharaja Points
pricing_model: hybrid
expiry: 24 months of inactivity
fuel_surcharges: low
award_chart: '[[Air India Maharaja Club Chart]]'
---

The merged Air India + Vistara program. The only FFP most Indian bank currencies reach at 1:1, and the cheapest Star Alliance redemption channel from India.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
