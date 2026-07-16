---
type: hotel-program
tags:
- program
- program/hotel
chain: Radisson Hotel Group
currency_name: Radisson points
pricing_model: zone
expiry: 24 months of inactivity
---

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
