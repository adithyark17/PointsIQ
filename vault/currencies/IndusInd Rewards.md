---
type: currency
tags:
- currency
bank: '[[IndusInd Bank]]'
expiry: no expiry on premium cards
redemption_floor: ~₹0.35-0.75 (cash credit on Legend/Pinnacle)
---

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
