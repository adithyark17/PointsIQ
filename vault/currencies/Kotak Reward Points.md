---
type: currency
tags:
- currency
bank: '[[Kotak Mahindra Bank]]'
expiry: 2-3 years by card
redemption_floor: ~₹0.25
---

No airline transfer partners; White Reserve redeems against travel bookings.

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
