---
type: index
area: documentation
status: active
updated: 2026-10-08
---

# Documentation

[Home](../Home.md) · [Parts](Parts.md) · [Photos](Photos.md) · [Illustrations](Illustrations.md)

The knowledge base connects these canonical documents. Detailed inventories, procedures and specifications remain in their existing files.

| Topic | Start here | Supporting material |
|---|---|---|
| Project scope and phases | [Repository overview](../../../README.md), [canonical roadmap](../../ROADMAP.md) | [Final-build architecture](../../final-build-architecture.md) |
| Historical baseline | [Archaeology overview](../../00-archaeology/README.md) | [Initial inventory](../../00-archaeology/01-initial-inventory.md), [photo catalogue](../../00-archaeology/02-photo-catalogue.md), [method and provenance](../../00-archaeology/03-method-and-provenance.md) |
| Detailed historical evidence | [Detailed photo inventory](../../00-archaeology/05-detailed-photo-inventory.md) | [Recovered motion-electronics spares](../../00-archaeology/06-motion-electronics-spares.md), [Chapter 0 source notes](../../00-archaeology/04-blog-source-notes-chapter-0.md) |
| Original hardware | [Hardware baseline](../../../hardware/README.md) | [Teardown evidence](../../../photos/02-teardown/INDEX.md) |
| Original mechanical reassembly | [Stage 02 scope](../../02-reassembly/README.md), [reassembly manual](../../02-reassembly/original-reassembly-manual.md) | [Historical references](../../02-reassembly/historical-references.md), [local source material](../../02-reassembly/historical-manuals/README.md), [latest photo index](../../../photos/03-reassembly/INDEX.md) |
| Legacy filament | [Filament archive rules](../../01-filaments/README.md) | [Inventory and qualification work](../../01-filaments/01-inventory.md) |
| Generation 3 vendor references | [BIGTREETECH local reference archive](../../../hardware/reference/bigtreetech/README.md) | Pinned upstream manuals, pinouts, schematics, connection diagrams, wiki snapshots and reference configs for Manta M8P V2.0, EBB36 Gen2 / USB adapter and TMC2209 V1.3; provenance and hashes are retained locally. |
| Generation 3 PSU and connector distribution | [Power-distribution specification](../../../hardware/generation-3-power-distribution.md) | Separate mains/PSU enclosure, individually protected XT60E branches, XT30(2+2) CAN/logic cabling, dedicated bed heater supply and engineering release gates |
| Generation 3 bed electronics | [Revival Bed Node architecture](../../../hardware/generation-3-bed-node.md) | Staged conventional-to-CAN-node migration, upstream Klipper integration, heater safety boundaries and open PCB decisions |
| Generation 3 design | [Frozen architecture](../../final-build-architecture.md) | [Procurement status](../../../hardware/generation-3-procurement-status.md), [electronics bench-test pack](../../../hardware/bench-tests/generation-3-electronics/README.md), [bench-fixture dimensional survey](../../../hardware/bench-tests/generation-3-electronics/bench-fixture-dimensional-survey.md), [Target BOM](../../../hardware/generation-3-target-bom.md), [custom CAN-node design rules](../../../hardware/generation-3-custom-can-node-design-rules.md), [linear-motion architecture](../../../hardware/generation-3-linear-motion.md), [Roto + Revo + Eddy extrusion/toolhead target](../../../hardware/generation-3-extrusion-toolhead.md) |
| Generation 3 smart spools | [Identification, learning and weighing architecture](../../../hardware/generation-3-smart-spool-system.md) | [RASS active-feed architecture](../../../hardware/generation-3-rass.md), [Filament System](../systems/Filament-System.md), [target BOM](../../../hardware/generation-3-target-bom.md) |
| Revival Intelligence & Diagnostics | [RID subsystem concept](../../../hardware/generation-3-revival-intelligence-diagnostics.md) | CB2 supervisory role, four diagnostic domains, sensor fusion, machine baseline/history and ML-first/LLM-assisted architecture |
| RID candidates and promotions | [RID candidate backlog](../../../hardware/generation-3-enhancement-candidates.md) | Prioritised software-only and minimal-hardware/high-impact studies; unpromoted candidates remain separate from requirements |
| Original printable designs | [Part catalogue](../../../printed-parts/original-designs/Original-Printed-Parts.md), [archive provenance](../../../printed-parts/original-designs/Provenance.md) | Preserved historical STL/SCAD files, licenses and hashes; exact part matching remains open. |
| Manufacturing, configuration and profiles | [Printed parts](../../../printed-parts/README.md), [firmware](../../../firmware/README.md), [profiles](../../../profiles/README.md) | Historical models are available; new project CAD, working firmware and validated profiles require their own implementation records. |

## Reading evidence correctly

Use dated observations and their provenance when sources differ. Frozen architecture records a decision; it does not establish installation or commissioning. Preserve historical observations and place later findings in their appropriate stage or current source. Track unresolved conflicts in [Open issues](../project/Open-Issues.md).

## USB bench update — 8 October 2026

[Canonical session record](../../../hardware/bench-tests/generation-3-electronics/records/2026-10-08-usb-eddy-camera.md): CB1 is mounted on the replacement Manta; EBB36 Gen2 and Eddy Duo communicate over USB, including the corrected short expansion cable. Direct-USB 30-minute sensor acquisition passed. Main-camera UVC modes were queried and video is visible in Mainsail via /webcam/; warm reboot and PSU cold start worked. Full-board/print commissioning is not claimed. Joint prolonged USB testing and distance calibration remain pending, followed by direct CAN and later CEB CAN. Final CB2 architecture is unchanged.
