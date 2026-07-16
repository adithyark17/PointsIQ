---
type: air-program
tags:
- program
- program/air
airline: '[[Vistara]]'
currency_name: CV Points
pricing_model: zone
status: merged
---

Merged into Air India Maharaja Club (2024-25); balances converted 1:1.

## Inbound transfer routes

```dataview
TABLE source AS "From", ratio, transfer_time, verified
FROM "transfers" WHERE target = this.file.link
SORT ratio ASC
```

<!-- generated: edits above this line will be overwritten -->
