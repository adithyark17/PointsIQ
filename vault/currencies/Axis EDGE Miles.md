---
type: currency
tags:
- currency
bank: '[[Axis Bank]]'
expiry: no expiry while account active
redemption_floor: 1 EDGE Mile ≈ ₹1 via Travel Edge
---

Earned directly on Atlas. Standard partner ratio is a market-best 1:2 (1 EDGE Mile = 2 partner miles) across Group A/B partners with separate annual caps — though the April 2026 devaluation dropped Qatar/Marriott/Accor and added BA/Finnair/Vietnam at an inverted 2:1.

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
