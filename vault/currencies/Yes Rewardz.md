---
type: currency
tags:
- currency
bank: '[[Yes Bank]]'
expiry: 3 years
redemption_floor: ~₹0.25
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
