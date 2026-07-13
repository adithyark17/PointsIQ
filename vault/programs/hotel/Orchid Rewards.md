---
type: hotel-program
tags:
- program
- program/hotel
chain: Royal Orchid Hotels
currency_name: Orchid points
pricing_model: fixed-value
---

India-native chain program; added as an Axis Group B partner in April 2026.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

## Outbound transfer routes

```dataview
TABLE target AS "To", ratio, transfer_time, verified
FROM "transfers" WHERE source = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
