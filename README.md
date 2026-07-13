# PointsIQ — Rewards Knowledge Base & Graph

An India-first **points & miles knowledge graph**, built as an [Obsidian](https://obsidian.md) vault.
Every card, reward currency, transfer route, loyalty program, airline, alliance and airport is a
markdown note; every relationship is a wikilink. Obsidian's graph view renders the whole map —
answers to "which card should I swipe?" or "how do I get to Tokyo in business class?" are literally
walks through this graph:

```
MCC: Dining → Card: HDFC Infinia → Currency: HDFC Reward Points
  → Transfer: HDFC RP → KrisFlyer → Program: KrisFlyer
  → Airline: Singapore Airlines → Alliance: Star Alliance → Airport: SIN
```

## What's inside

| Layer | Contents |
|---|---|
| `data/` | **Source of truth** — hand-curated YAML: banks, cards, currencies, transfer routes, FFPs, hotel programs, airlines, alliances, MCC categories, portals, award charts, concepts |
| `scripts/` | Python generators that turn `data/` + the open [OurAirports](https://ourairports.com/data/) dataset into the vault, plus a graph validator |
| `vault/` | **The Obsidian vault** — open this folder in Obsidian. ~6,400 airport nodes + ~250 countries + the curated rewards core, all wikilinked |

## Opening the vault

1. Install [Obsidian](https://obsidian.md).
2. **Open folder as vault** → select `vault/`.
3. (Recommended) Install the **Dataview** community plugin — currency, program, alliance,
   country and MCC notes embed Dataview queries that render live tables (transfer partners,
   alliance members, airports per country…). Everything else works with core Obsidian.
4. Open the **Graph view**. It starts filtered to the curated core (`-tag:#airport/medium`);
   clear the filter to reveal all ~6,400 airports clustered around their countries.

Start at **[[Home]]** — the map of content.

## Regenerating the vault

The vault is a build artifact. Humans edit `data/*.yaml`; generators write the notes.

```sh
pip install pyyaml

python3 scripts/generate_airports.py --fetch   # download OurAirports CSVs → data/cache/, emit airports + geo
python3 scripts/generate_from_data.py           # curated YAML → all other notes
python3 scripts/validate.py                     # broken-link check + node/edge census
```

Generated notes end with `<!-- generated: edits above this line will be overwritten -->`.
Anything you write **below** that marker on a curated-type note is preserved across regeneration.
Airport notes are fully regenerated — annotate their countries or hub airlines instead.

## Data model (node types)

`bank · card · currency · transfer · portal · air-program · hotel-program · airline · alliance ·
mcc-category · award-chart · stopover-program · concept · region · country · airport`

Transfer routes are **dedicated edge notes** (e.g. `transfers/Axis EDGE Miles → KrisFlyer.md`)
carrying ratio, transfer time and a `verified:` date — so the graph shows *named* edges and
Dataview can sort partners by ratio.

## Accuracy

Transfer ratios, earn rates and award charts in this domain drift monthly. Every transfer route
and award chart carries a `verified:` date — treat anything stale as a prompt to re-verify with
the bank/program before moving points.
