---
type: hotel-program
tags:
- program
- program/hotel
chain: Wyndham
currency_name: Wyndham points
pricing_model: fixed
expiry: 48 months
---

Flat 7.5k/15k/30k per night; strong for Indian leisure properties.

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
