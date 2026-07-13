---
type: mcc-category
tags:
- mcc
mcc_codes:
- '4900'
- '4814'
- '4816'
typically_excluded: true
---

Capped or excluded on most premium cards since the 2023-24 devaluation wave.

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
