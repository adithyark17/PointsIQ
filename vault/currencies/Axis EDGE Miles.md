---
type: currency
tags:
- currency
bank: '[[Axis Bank]]'
expiry: no expiry while account active
redemption_floor: 1 EDGE Mile ≈ ₹1 via Travel Edge
---

Earned directly on Atlas (and by converting EDGE Rewards 5:4). The widest 1:1 airline partner list of any Indian currency.

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
