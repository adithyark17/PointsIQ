---
type: mcc-category
tags:
- mcc
mcc_codes:
- '6513'
typically_excluded: true
---

Universally excluded (and often fee-loaded) after the 2022-23 rent-platform boom.

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
