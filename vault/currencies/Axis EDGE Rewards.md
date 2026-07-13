---
type: currency
tags:
- currency
bank: '[[Axis Bank]]'
expiry: no expiry while account active
redemption_floor: ~₹0.20 per point in catalogue; 5:4 into EDGE Miles
---

Earned on Magnus/Reserve and mainstream Axis cards; convert to EDGE Miles before transferring.

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
