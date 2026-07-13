---
type: mcc-category
tags:
- mcc
mcc_codes:
- '5812'
- '5813'
- '5814'
typically_excluded: false
---

**Concept:** [[Merchant Category Code]]

## Cards that accelerate this category

```dataview
TABLE earn_unit, reward_rate_pct AS "Base %"
FROM "cards" WHERE contains(string(accelerated_earn), this.file.name)
```

## Cards that exclude this category

```dataview
LIST FROM "cards" WHERE econtains(excluded_categories, this.file.link)
```

<!-- generated: edits above this line will be overwritten -->
