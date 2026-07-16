---
type: mcc-category
tags:
- mcc
mcc_codes:
- '5399'
- '5964'
- '5969'
typically_excluded: false
---

Where most accelerated-earn programs (Millennia, Regalia Gold partner brands) live.

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
