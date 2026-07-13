---
type: hotel-program
tags:
- program
- program/hotel
chain: IHCL (Taj Hotels)
currency_name: NeuCoins
pricing_model: fixed-value
expiry: 12 months
---

Tata Neu-integrated; NeuCoins ≈ ₹1 across the Tata ecosystem including Taj stays.

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
