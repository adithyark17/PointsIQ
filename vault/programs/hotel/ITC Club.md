---
type: hotel-program
tags:
- program
- program/hotel
chain: ITC Hotels
currency_name: Club ITC Green Points
pricing_model: fixed-value
expiry: 36 months
---

India-native luxury program; Green Points redeem ~₹1 each at ITC properties.

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
