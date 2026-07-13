---
type: mcc-category
tags:
- mcc
mcc_codes:
- '5541'
- '5542'
- '5983'
typically_excluded: true
---

Excluded from rewards on nearly every Indian card; 1% surcharge waiver instead.

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
