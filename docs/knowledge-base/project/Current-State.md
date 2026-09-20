---
type: project
area: project
status: in-progress
phase: stage-02
priority: high
updated: 2026-09-20
---

# Current State

[Home](../Home.md) · [Roadmap](Roadmap.md) · [Open Issues](Open-Issues.md)

This snapshot was checked against the local repository on 19 September 2026. Its latest reassembly batch is dated 16 September 2026; it does not imply a new physical inspection on the review date.

| Scope | Documented state | Evidence / next gate |
| --- | --- | --- |
| Stage 00 — Archaeology | Complete as a frozen non-invasive baseline, closed 12 September | [Stage record](../../00-archaeology/README.md); later spare-box additions are distinguished in [Photos](../indexes/Photos.md) |
| Stage 01 — Teardown, cleaning and inventory | Complete, closed 13 September | [Roadmap](../../ROADMAP.md), [teardown inventory](../../../photos/02-teardown/INDEX.md) |
| Stage 02 — Original mechanical reassembly | In progress; photo evidence covers manual Stage A and subsequent B–G work | [Photo index](../../../photos/03-reassembly/INDEX.md), [16 September batch](../../../photos/03-reassembly/BATCH-20260916.md) |
| Remaining original reassembly and validation | Completion of manual H–J and the final mechanical gate is not established by the latest batch | [Build sequence](../build/Build.md), [manual](../../02-reassembly/original-reassembly-manual.md) |
| Generation 3 | Architecture frozen; implementation deferred | [Architecture](../../final-build-architecture.md), [motion architecture](../../../hardware/generation-3-linear-motion.md), [target BOM](../../../hardware/generation-3-target-bom.md) |
| Generation 3 smart spools | Identification, assisted tag learning and weighing architecture frozen; RASS extends it with single-spool active feed, driven-spool assistance and buffer/dancer control; exact implementation and decoder support require validation | [Smart-spool architecture](../../../hardware/generation-3-smart-spool-system.md), [RASS](../../../hardware/generation-3-rass.md), [Filament System](../systems/Filament-System.md) |
| Generation 3 extrusion/probing | E3D Roto + Revo + BTT Eddy Duo is the frozen 1.75 mm direct-drive / bed-scan direction; PLA quality is primary and ABS/ASA is occasional open-frame use only | [Toolhead target](../../../hardware/generation-3-extrusion-toolhead.md), [Extrusion](../systems/Extrusion.md) |
| Generation 3 enhancements | Non-frozen candidates for fault detection, probing/cleaning, controls, telemetry and automated preparation | [Candidate register](../../../hardware/generation-3-enhancement-candidates.md); adoption requires the documented evaluation |
| Firmware and print profiles | Repository areas reserved for configuration/profile records; successful commissioning is not established here | [Firmware](../../../firmware/README.md), [profiles](../../../profiles/README.md) |

## Current evidence boundary

The [reassembly archive](../../../photos/03-reassembly/INDEX.md) contains **102 sanitized JPEGs in three batches**: 35 from 14 September, 9 from 15 September and 58 from 16 September. The latest batch is classified across manual Stages B–G. A photograph of an assembled subsystem is evidence of reconstruction, not proof of alignment, free motion, electrical suitability or successful printing.

## Next work supported by the record

1. Review the [Stage 02 manual](../../02-reassembly/original-reassembly-manual.md) against the latest evidence, record outstanding checks and continue the documented sequence.
2. Record measurements and results at the relevant [build phase](../build/Build.md); only then change completion/test status.
3. Resolve the measurement and identification dependencies in [Open Issues](Open-Issues.md) before releasing future CAD, selections or commissioning records.

The present mechanical work does not authorize mains power-up. The [existing safety boundary](../../02-reassembly/README.md#safety-boundary) remains in force.
