# Prusa i3 Revival 2026

> Bringing a classic Prusa i3 back to life — one documented subsystem at a time.

**Prusa i3 Revival 2026** documents the restoration and modernization of a self-built classic Prusa i3 recovered after more than a decade in storage.

The project is not intended to turn the machine into a modern Prusa clone. The objective is to preserve the character and documented history of the original printer while rebuilding it into a safe, reliable and reproducible machine.

## Knowledge base

Open [Home](docs/knowledge-base/Home.md) for project status, decisions, subsystem/build navigation and source-linked evidence indexes. The repository root is also the Obsidian vault. Follow the [maintenance guide](docs/knowledge-base/Maintenance.md) and [repository instructions](AGENTS.md) when changing project knowledge.

## Current status

- **Stage 00 — Archaeology: COMPLETE (12 September 2026).** The non-invasive as-found baseline is frozen and preserved.
- **Stage 01 — Teardown, cleaning and inventory: COMPLETE (13 September 2026).** The printer has been fully dismantled, cleaned and catalogued. The teardown photo sequence reaches `TD-20260913-228`.
- **Stage 02 — Original mechanical reassembly: IN PROGRESS (13 September 2026).** Historical assembly sources have been indexed, a project-specific reassembly manual has been created and physical reconstruction is underway. The Stage 02 photo archive currently contains **116 sanitized JPEGs** in four batches: `RA-20260914-001` through `RA-20260914-035`, `RA-20260915-001` through `RA-20260915-009`, `RA-20260916-001` through `RA-20260916-058`, and `RA-20260921-001` through `RA-20260921-014`. The [16 September batch](photos/03-reassembly/BATCH-20260916.md) records progress through manual Stages B–G. The [21 September batch](photos/03-reassembly/BATCH-20260921.md) adds 14 Stage H photographs of the geared-extruder subassembly. Assembly is reported complete in that batch; mounting and acceptance evidence remain to be recorded. Photographic coverage does not establish completion of every mechanical acceptance check.
- **Generation 3 target architecture: FROZEN (13 September 2026).** The final Manta/CB2/Klipper/CAN architecture is documented in **[docs/final-build-architecture.md](docs/final-build-architecture.md)** and will not be implemented until the earlier generations have been documented and tested. Initial Generation 3 stock has been acquired: Manta M8P V2.0, EBB36 Gen2 kit and 6× BTT TMC2209 V1.3; these parts are not yet recorded as tested or commissioned. **[Revival Intelligence & Diagnostics](hardware/generation-3-revival-intelligence-diagnostics.md)** groups future CB2-hosted supervisory intelligence, machine vision, condition monitoring and diagnostic candidate work; individual RID features remain unpromoted until separately evaluated.

The complete stage-by-stage plan is maintained in **[docs/ROADMAP.md](docs/ROADMAP.md)**.

Original printable-design candidates are available in the [historical parts catalogue](printed-parts/original-designs/Original-Printed-Parts.md), including the [small Greg/Wade extruder gear](printed-parts/original-designs/Small-Extruder-Gear.md). The archive preserves source files and provenance; exact part matching and fit checks remain open.

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

1. **Original Hardware Revival** — rebuild the original machine and establish a reliable legacy 3 mm / 2.85 mm printing baseline using the Arduino Mega 2560 + RAMPS-era stack.
2. **Re-ARM transitional study** — document and, if worthwhile, test the recovered Panucatt Re-ARM with RAMPS-era hardware as a period 32-bit upgrade path.
3. **Revival 2026 final build** — move to 1.75 mm extrusion, 24 V power, modern electronics, CAN toolhead, new wiring and current safety practices while preserving the classic i3 character. The frozen target is defined in **[docs/final-build-architecture.md](docs/final-build-architecture.md)**.

## Design principles

1. **Document before changing.**
2. **Reconstruct before redesigning.**
3. **Reuse only when it makes engineering sense.**
4. **Modernize safety-critical systems.**
5. **Prefer reproducible and readily available components.**
6. **Publish editable source files**, not only STL exports.
7. **Keep the legacy 3 mm stage functional** before the later 1.75 mm conversion.
8. Record measurements, decisions, failures and test results so the work can be reproduced.
9. **Preserve the historical red-and-black visual identity:** mechanical/structural printed parts are red in the final build, while frame and rods remain black; newly introduced enclosures may use other colours/materials when justified by function and design.

## Repository

- `docs/` — archaeology, inventory, roadmap and project documentation
  - [`docs/ROADMAP.md`](docs/ROADMAP.md) — current project stages
  - [`docs/final-build-architecture.md`](docs/final-build-architecture.md) — frozen Generation 3 control/electrical architecture and final visual identity
  - `docs/00-archaeology/` — frozen as-found archaeology and provenance
  - `docs/01-filaments/` — recovered legacy-filament inventory and future qualification
  - [`docs/02-reassembly/`](docs/02-reassembly/) — Stage 02 historical source index and original-geometry reassembly manual
- `hardware/` — mechanical/electrical baseline and future BOM documentation
- `printed-parts/` — CAD sources, STEP, STL and reference 3MF projects
- `firmware/` — printer configurations for the documented generations
- `profiles/` — manufacturing and slicer profiles
- `photos/00-archaeology/` — frozen Stage 00 evidence
- `photos/02-teardown/` — Stage 01 teardown originals and cleaned component-inventory derivatives (`TD-20260913-001` through `TD-20260913-228`)
- [`photos/03-reassembly/`](photos/03-reassembly/) — Stage 02 sanitized reassembly evidence: **116 photographs** across `RA-20260914-001`–`035`, `RA-20260915-001`–`009`, `RA-20260916-001`–`058` and `RA-20260921-001`–`014`

## Safety

No old mains-powered hardware should be energized merely to see whether it still works. The PSU, mains wiring, heated bed, connectors, power distribution, insulation and protection arrangements must be inspected before electrical commissioning.

---

Started in September 2026.
