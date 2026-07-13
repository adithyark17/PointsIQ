---
type: air-program
tags:
- program
- program/air
airline: '[[Qatar Airways]]'
alliance: '[[oneworld]]'
currency_name: Avios
pricing_model: zone
expiry: 36 months of inactivity
fuel_surcharges: moderate
award_chart: '[[Qatar Avios Chart]]'
---

Uses Avios; best westbound J redemptions from India (Qsuites via DOH). Pool with British Airways Executive Club via Avios household transfers.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
