---
type: project
area: project
status: in-progress
phase: stage-02
priority: high
updated: 2026-09-23
---

# Current State

[Home](../Home.md) · [Roadmap](Roadmap.md) · [Open Issues](Open-Issues.md)

This snapshot was checked against the published repository on 21 September 2026. Its latest reassembly batch is dated 21 September 2026; it does not imply a new physical inspection on the review date.

| Scope | Documented state | Evidence / next gate |
| --- | --- | --- |
| Stage 00 — Archaeology | Complete as a frozen non-invasive baseline, closed 12 September | [Stage record](../../00-archaeology/README.md); later spare-box additions are distinguished in [Photos](../indexes/Photos.md) |
| Stage 01 — Teardown, cleaning and inventory | Complete, closed 13 September | [Roadmap](../../ROADMAP.md), [teardown inventory](../../../photos/02-teardown/INDEX.md) |
| Stage 02 — Original mechanical reassembly | In progress; photo evidence covers manual Stages A–H, with the latest batch documenting the geared-extruder subassembly | [Photo index](../../../photos/03-reassembly/INDEX.md), [21 September batch](../../../photos/03-reassembly/BATCH-20260921.md) |
| Remaining original reassembly and validation | Stage H assembly is reported complete; its mounting/acceptance evidence, manual I–J completion and the final mechanical gate remain unrecorded | [Build sequence](../build/Build.md), [manual](../../02-reassembly/original-reassembly-manual.md) |
| Generation 3 | Architecture frozen; historical steel frame and M8/M10 threaded base retained, MGN12 guidance uses X/Y T-slot extrusion supports and the direct/plate/profile Z hierarchy; first electronics acquired and a bench-test pack is prepared, but no purchased Generation 3 electronics are yet recorded as tested/commissioned | [Architecture](../../final-build-architecture.md), [linear motion](../../../hardware/generation-3-linear-motion.md), [target BOM](../../../hardware/generation-3-target-bom.md), [procurement status](../../../hardware/generation-3-procurement-status.md), [electronics bench-test pack](../../../hardware/bench-tests/generation-3-electronics/README.md) |
| Generation 3 smart spools | Identification, assisted tag learning and weighing architecture frozen; RASS extends it with single-spool active feed, driven-spool assistance and buffer/dancer control; exact implementation and decoder support require validation | [Smart-spool architecture](../../../hardware/generation-3-smart-spool-system.md), [RASS](../../../hardware/generation-3-rass.md), [Filament System](../systems/Filament-System.md) |
| Generation 3 extrusion/probing | E3D Roto + Revo + BTT Eddy Duo is the frozen 1.75 mm direct-drive / bed-scan direction; PLA quality is primary and ABS/ASA is occasional open-frame use only | [Toolhead target](../../../hardware/generation-3-extrusion-toolhead.md), [Extrusion](../systems/Extrusion.md) |
| Revival Intelligence & Diagnostics | RID is the Generation 3 umbrella for CB2-hosted supervisory intelligence, vision, condition monitoring, maintenance history and diagnostic sensor fusion. Practical S/H candidates remain prioritised by value/complexity; a separate M01–M15 Moonshot tier records extreme concepts at production score 1/5 without placing them on the production path | [RID concept](../../../hardware/generation-3-revival-intelligence-diagnostics.md), [RID backlog and Moonshots](../../../hardware/generation-3-enhancement-candidates.md), [Decision Log](../decisions/Decision-Log.md) |
| Firmware and print profiles | Repository areas reserved for configuration/profile records; successful commissioning is not established here | [Firmware](../../../firmware/README.md), [profiles](../../../profiles/README.md) |
| Original printable designs | Historical single-frame and Greg/Wade files archived locally; leading gear/idler candidates identified visually, exact fit and accessory coverage still open | [Catalogue](../../../printed-parts/original-designs/Original-Printed-Parts.md), [small gear](../../../printed-parts/original-designs/Small-Extruder-Gear.md), [provenance](../../../printed-parts/original-designs/Provenance.md) |

## Current evidence boundary

The [reassembly archive](../../../photos/03-reassembly/INDEX.md) contains **116 sanitized JPEGs in four batches**: 35 from 14 September, 9 from 15 September, 58 from 16 September and 14 from 21 September. The latest batch is classified as manual Stage H and records the geared-extruder subassembly. A photograph of an assembled subsystem is evidence of reconstruction, not proof of alignment, free motion, electrical suitability or successful printing.

## Next work supported by the record

1. Record the outstanding [Phase H checks](../build/Phase-H.md) against the latest assembly evidence, then continue with [Phase I — Endstops](../build/Phase-I.md) and [Phase J — Electronics placement](../build/Phase-J.md) using the [Stage 02 manual](../../02-reassembly/original-reassembly-manual.md).
2. Record measurements and results at the relevant [build phase](../build/Build.md); only then change completion/test status.
3. Resolve the measurement and identification dependencies in [Open Issues](Open-Issues.md) before releasing future CAD, selections or commissioning records.

The present mechanical work does not authorize mains power-up. The [existing safety boundary](../../02-reassembly/README.md#safety-boundary) remains in force.
