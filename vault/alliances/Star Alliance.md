---
type: alliance
tags:
- alliance
founded: 1997
---

The largest alliance. Key India relevance: Air India is a member, so Maharaja Club points redeem across the whole network, and Star partners (Singapore Airlines, United, Turkish, Thai, ANA, Ethiopian) all serve Indian gateways.

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
