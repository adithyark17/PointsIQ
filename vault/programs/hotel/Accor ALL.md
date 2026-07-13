---
type: hotel-program
tags:
- program
- program/hotel
chain: Accor
currency_name: ALL Reward Points
pricing_model: fixed-value
expiry: 12 months of inactivity
---

2,000 points = €40 off any stay; effectively a cash-value currency.

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
