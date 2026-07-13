---
type: currency
tags:
- currency
bank: '[[HDFC Bank]]'
expiry: 2 years from earning (3 years on Infinia/DCB)
redemption_floor: 1 RP ≈ ₹1 on SmartBuy flights/hotels (Infinia), ₹0.50 as airmiles or cashback
---

Value is card-dependent: the same point is worth up to ₹1 on Infinia and far less on mass-market cards. Airline/hotel transfers run through SmartBuy with per-day and per-year caps.

## Transfer partners

```dataview
TABLE target AS "To", ratio, transfer_time, verified
FROM "transfers" WHERE source = this.file.link
SORT ratio ASC
```

## Earned by

```dataview
LIST FROM "cards" WHERE currency = this.file.link
```

<!-- generated: edits above this line will be overwritten -->
