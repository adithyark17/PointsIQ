---
type: hotel-program
tags:
- program
- program/hotel
chain: Hyatt
currency_name: World of Hyatt points
pricing_model: zone
expiry: 24 months of inactivity
---

Published award chart survives; consistently the highest cpp hotel currency.

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
