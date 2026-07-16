---
type: currency
tags:
- currency
bank: '[[ICICI Bank]]'
expiry: 3 years
redemption_floor: ~₹0.25-1.00 depending on card and redemption
---

₹1/point on iShop flights/hotels is the real ceiling; the only airline transfer is Air India Maharaja Club at 1:1.

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
