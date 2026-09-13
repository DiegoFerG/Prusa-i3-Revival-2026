# Prusa i3 Revival 2026

> Bringing a classic Prusa i3 back to life — one documented subsystem at a time.

**Prusa i3 Revival 2026** documents the restoration and modernization of a self-built classic Prusa i3 recovered after more than a decade in storage.

The project is not intended to turn the machine into a modern Prusa clone. The objective is to preserve the character and documented history of the original printer while rebuilding it into a safe, reliable and reproducible machine.

## Current status

- **Stage 00 — Archaeology: COMPLETE (12 September 2026).** The non-invasive as-found baseline is frozen and preserved.
- **Stage 01 — Teardown, cleaning and inventory: COMPLETE (13 September 2026).** The printer has been fully dismantled, cleaned and catalogued. The teardown photo sequence currently reaches `TD-20260913-228`.
- **Stage 02 — Original mechanical reassembly: NEXT.** The printer will first be rebuilt from the documented original geometry before modernization decisions are applied.

The complete stage-by-stage plan is maintained in **[docs/ROADMAP.md](docs/ROADMAP.md)**.

## Confirmed original baseline

The teardown and component inventory established a substantially clearer baseline than the initial visual archaeology:

- classic Prusa i3 / Rework-era / RepRap-derived architecture with a single-sheet steel vertical frame;
- threaded-rod Y structure and 8 mm smooth linear guides;
- Y bed carriage approximately **220 × 220 mm**, approximately **210 mm mounting-hole spacing** in both axes, **6 mm** thick, with M3 threaded mounting holes;
- 2× M10 × 350 mm structural threaded rods, 4× M8 × 200 mm threaded rods and 2× M5 × 310 mm threaded rods;
- 2× Ø8 × 350 mm, 2× Ø8 × 330 mm and 2× Ø8 × 317 mm smooth rods;
- 10× LM8UU-family linear bearings and 3× FAG 608Z radial bearings;
- 5× Wantai **42BYGHW811** NEMA17 motors, labelled **2.5 A** and **1.8°/step**;
- T2.5 belt transmission with approximately 20-tooth aluminium drive pulleys;
- Arduino Mega 2560 + StaticBoards RAMPS 1.4SB + four A4988-family plug-in stepper-driver modules;
- RepRapDiscount-style full graphic controller, RAMPS smart adapter and Panasonic 16 GB SDHC card;
- JCPOWER **JC-360-12** open-frame PSU, **12 V / 30 A**;
- Wade/Greg's-Wade-family geared direct extruder for the legacy 3 mm stage;
- legacy E3D-family hotend, probably V5-era, with exact revision still intentionally unclaimed;
- four IKEA SÖRLI mirrors, **200 × 200 × 3 mm**, used as removable build surfaces;
- screw-and-spring bed levelling hardware, including the historically improvised clothes-peg springs.

The original mixed wiring harness has been documented but **will not be reused**. The revival will be wired from scratch when the electrical stage begins.

## Project generations

The long-term plan deliberately keeps three generations of the same machine visible and documented:

1. **Original Hardware Revival** — rebuild the original machine and establish a reliable legacy 3 mm / 2.85 mm printing baseline.
2. **Re-ARM transitional study** — document and, if worthwhile, test the recovered Panucatt Re-ARM with RAMPS-era hardware as a period 32-bit upgrade path.
3. **Revival 2026 final build** — move to 1.75 mm extrusion, proper Z leadscrews, modern electronics, new wiring and current safety practices while preserving the classic i3 character.

## Design principles

1. **Document before changing.**
2. **Reconstruct before redesigning.**
3. **Reuse only when it makes engineering sense.**
4. **Modernize safety-critical systems.**
5. **Prefer reproducible and readily available components.**
6. **Publish editable source files**, not only STL exports.
7. **Keep the legacy 3 mm stage functional** before the later 1.75 mm conversion.
8. Record measurements, decisions, failures and test results so the work can be reproduced.

## Repository

- `docs/` — archaeology, inventory, roadmap and project documentation
  - [`docs/ROADMAP.md`](docs/ROADMAP.md) — current project stages
  - `docs/00-archaeology/` — frozen as-found archaeology and provenance
  - `docs/01-filaments/` — recovered legacy-filament inventory and future qualification
- `hardware/` — mechanical/electrical baseline and future BOM documentation
- `printed-parts/` — CAD sources, STEP, STL and reference 3MF projects
- `firmware/` — printer configurations
- `profiles/` — manufacturing and slicer profiles
- `photos/00-archaeology/` — frozen Stage 00 evidence
- `photos/02-teardown/` — Stage 01 teardown originals and cleaned component-inventory derivatives

## Safety

No old mains-powered hardware should be energized merely to see whether it still works. The PSU, mains wiring, heated bed, connectors, power distribution, insulation and protection arrangements must be inspected before electrical commissioning.

---

Started in September 2026.