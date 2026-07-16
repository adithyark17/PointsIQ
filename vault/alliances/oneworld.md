---
type: alliance
tags:
- alliance
founded: 1999
---

British Airways, Qatar Airways, Cathay Pacific, Qantas, JAL, American, Alaska, Malaysia Airlines, SriLankan. Qatar's Doha hub makes oneworld the deepest westbound network from India; Avios (BA/Qatar/Iberia/Aer Lingus/Finnair) is the most India-accessible oneworld currency.

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
