---
type: currency
tags:
- currency
bank: '[[IDFC FIRST Bank]]'
expiry: no expiry (lifetime, card-dependent)
redemption_floor: ~₹0.25 catalogue
---

Mayura/Wealth added a small airline transfer list (2024).

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
