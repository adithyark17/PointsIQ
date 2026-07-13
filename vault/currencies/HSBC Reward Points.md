---
type: currency
tags:
- currency
bank: '[[HSBC India]]'
expiry: 3 years
redemption_floor: ~₹0.25-1.00
---

Premier/TravelOne transfer to ~20 air/hotel partners, mostly 1:1.

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
