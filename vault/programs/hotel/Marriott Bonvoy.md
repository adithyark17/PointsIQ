---
type: hotel-program
tags:
- program
- program/hotel
chain: Marriott International
currency_name: Bonvoy Points
pricing_model: dynamic
expiry: 24 months of inactivity
---

The bridge currency: transfers to 35+ airlines at 3:1 with a 5,000-mile bonus per 60,000 transferred — the only route from hotel points into many FFPs.

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
