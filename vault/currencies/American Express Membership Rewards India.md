---
type: currency
tags:
- currency
aliases:
- Amex MR India
- Membership Rewards
bank: '[[American Express India]]'
expiry: no expiry while card active
redemption_floor: ~₹0.25-0.50 catalogue; up to ₹1 via Gold Collection / transfers
---

18/24K Gold Collection redemptions and airline transfers set the value ceiling.

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
