---
type: bank
tags:
- bank
country: '[[India]]'
---

## Cards

```dataview
TABLE currency, annual_fee_inr AS "Fee ₹", reward_rate_pct AS "Rate %", status
FROM "cards" WHERE bank = this.file.link
SORT annual_fee_inr DESC
```

<!-- generated: edits above this line will be overwritten -->
