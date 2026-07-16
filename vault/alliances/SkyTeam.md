---
type: alliance
tags:
- alliance
founded: 2000
---

Air France-KLM, Delta, Virgin Atlantic, Vietnam Airlines, Saudia. Flying Blue is the main SkyTeam transfer target for Indian bank currencies.

## Member airlines

```dataview
TABLE iata, program, country FROM "airlines" WHERE alliance = this.file.link
SORT iata ASC
```

## Member programs

```dataview
TABLE airline, pricing_model, fuel_surcharges
FROM "programs/air" WHERE alliance = this.file.link
```

<!-- generated: edits above this line will be overwritten -->
