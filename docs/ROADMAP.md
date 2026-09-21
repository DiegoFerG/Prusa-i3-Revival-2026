# Roadmap — Prusa i3 Revival 2026

## 00 · Archaeology — COMPLETE (12 September 2026)
Freeze the non-invasive as-found baseline, identify the printer family provisionally, separate installed hardware from loose period material, and preserve the original photographic evidence.

## 01 · Teardown, cleaning and inventory — COMPLETE (13 September 2026)
Controlled disassembly, cleaning, measurement and component cataloguing are complete. The Stage 01 photographic sequence now reaches `TD-20260913-228`: originals `001–159` plus cleaned component-inventory derivatives `160–228`.

Key outcomes include identification of the installed Arduino Mega 2560 / StaticBoards RAMPS 1.4SB stack, Wantai 42BYGHW811 motors, JCPOWER JC-360-12 PSU, T2.5 transmission, LM8UU-family linear bearings, FAG 608Z bearings, legacy E3D-family hotend, original bed hardware and major rod dimensions.

The removed legacy wiring harness is archived as evidence and will **not** be reused.

## 02 · Original mechanical reassembly — IN PROGRESS (13 September 2026)
Rebuild the printer from the documented original geometry before applying modernization changes. The purpose is to validate how every subsystem fits together and to establish a known mechanical baseline.

Stage documentation:

- [`02-reassembly/README.md`](02-reassembly/README.md) — Stage 02 scope and safety boundary;
- [`02-reassembly/original-reassembly-manual.md`](02-reassembly/original-reassembly-manual.md) — project-specific historical reassembly manual;
- [`02-reassembly/historical-references.md`](02-reassembly/historical-references.md) — period source catalogue and provenance;
- `02-reassembly/historical-manuals/` — locally mirrored period source material where licensing and retrieval permit it;
- [`../photos/03-reassembly/README.md`](../photos/03-reassembly/README.md) — Stage 02 photographic evidence archive;
- [`../photos/03-reassembly/INDEX.md`](../photos/03-reassembly/INDEX.md) — reassembly photo inventory and range index.

The current Stage 02 photographic archive contains **102 sanitized JPEGs** in three batches: `RA-20260914-001` through `RA-20260914-035`, `RA-20260915-001` through `RA-20260915-009`, and `RA-20260916-001` through `RA-20260916-058`. The 14–15 September evidence covers Stage A structural reconstruction and its checkpoint. The [16 September batch](../photos/03-reassembly/BATCH-20260916.md) adds progress through manual Stages B–G: Y guides/carriage and transmission, bed mounting, Z supports/guides, X assembly and joining X to Z. This photographic coverage does not establish completion of every manual operation or the final mechanical checks.

Planned order:

1. steel frame and threaded-rod base;
2. Y axis and bed carriage;
3. Z guides and original threaded drive;
4. X axis and carriage;
5. belt drives, pulleys and idlers;
6. geared extruder and legacy hotend mounting;
7. motors and endstops;
8. mechanical alignment and free-motion checks.

No mains power-up is part of this stage.

## 03 · Revival Z axis
After the original geometry has been validated, replace the conventional threaded Z rods with suitable leadscrews. Design the new supports, nut mounts and couplings from measured geometry rather than assumption.

## 04 · Printed parts
Redesign or reproduce required parts and manufacture them primarily in ASA on a Bambu Lab P1S. Publish editable sources plus STEP, STL and reference 3MF where appropriate.

Historical preparation added on 19 September 2026: [original single-frame and Greg/Wade designs](../printed-parts/original-designs/Original-Printed-Parts.md) are archived locally with provenance. Use them as measured replacement candidates during Stage 02 where needed. Exact accessory identification, adaptation, printing and fit validation remain outstanding; this does not mark Stage 04 complete.

## 05 · Electronics, power and new wiring
Design the new controller architecture, drivers, power distribution, protection, connectors and enclosures. The printer will be rewired from scratch; the original mixed harness will not be reused.

The recovered Arduino Mega 2560 / RAMPS 1.4SB stack, the Panucatt Re-ARM material and other period electronics remain documented for historical comparison and controlled bench evaluation.

## 06 · Legacy 3 mm / 2.85 mm extrusion
Restore or modularly rebuild the geared extruder / hotend system so the recovered legacy filament stock can be evaluated and consumed where practical.

The existing hotend is E3D-family and probably V5-era, but the exact revision is still intentionally unclaimed. Its installed heater cartridge is currently captive because the retaining screw head is damaged. The thermistor type also remains to be electrically confirmed.

## 07 · Firmware and commissioning
Configuration, electrical checks, motion tests, endstop validation, heater safety, PID tuning, dimensional calibration and first controlled prints.

## 08 · Legacy Filament Lab
Inventory and test the old filament by material, manufacturer, diameter, storage condition, drying procedure, print parameters and result.

## 09 · 1.75 mm conversion
Perform a modular conversion of the extrusion system after the legacy stock has been evaluated or consumed.

## 10 · Results
Document reliability, print quality, noise, realistic speed limits, lessons learned and a reproducible community guide.

## Continuous workstream · Bilingual blog
The Spanish and English blog is maintained throughout the project. Repository evidence remains the technical source of truth; each completed stage should generate or update its corresponding article rather than postponing the narrative until the final build.
