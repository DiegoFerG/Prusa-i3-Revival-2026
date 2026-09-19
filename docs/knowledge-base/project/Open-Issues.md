---
type: project
area: project
status: active
phase: stage-02
priority: high
updated: 2026-09-19
---

# Open Issues

[Home](../Home.md) · [Current State](Current-State.md) · [Decision Log](../decisions/Decision-Log.md)

This is a source-linked register of unresolved work. IDs are local knowledge-base identifiers, not GitHub issue numbers. Priorities express dependency order for this register. Close an item only after linking its resolution or test record; preserve its ID.

| ID | Priority / scope | Open item and closure evidence |
| --- | --- | --- |
| KB-001 | Medium / documentation | Reconcile the [archaeology photo README](../../../photos/00-archaeology/README.md) description of 80 originals with the later nine sanitized spare-box photographs. Preserve the frozen 80-image historical baseline and ARQ IDs. [Spares record](../../00-archaeology/06-motion-electronics-spares.md) and [Photos](../indexes/Photos.md) distinguish the later additions. |
| KB-002 | High / Stage 02 | Record the outstanding manual H–J work and final mechanical gate. The [latest batch](../../../photos/03-reassembly/BATCH-20260916.md) documents B–G progress, not completion of all checks. Close using results linked from the [manual](../../02-reassembly/original-reassembly-manual.md). |
| KB-003 | High / legacy extrusion | Confirm the legacy hotend revision and thermistor type; resolve the damaged heater-retaining screw/captive heater cartridge. The [roadmap](../../ROADMAP.md) explicitly leaves these unresolved. Record identification and inspection/test evidence in the existing inventory before reuse. |
| KB-004 | High / Generation 3 bed | Measure the original heated-bed PCB footprint and mounting geometry before freezing plate CAD, heater dimensions/power and related load calculations. The carriage and mirror dimensions are not substitutes. See [target BOM](../../../hardware/generation-3-target-bom.md#bed-size-rule). |
| KB-005 | Medium / Generation 3 motion | Resolve rail supplier/preload/lengths, carriers/adjusters, Tr8 lead and Z alignment/support geometry after measured reconstruction. See [motion architecture](../../../hardware/generation-3-linear-motion.md) and [deferred selections](../../../hardware/generation-3-target-bom.md#selections-intentionally-deferred). |
| KB-006 | Medium / Generation 3 components | Select extruder/hotend, probe, filament sensor, fans/ducts, lighting, PSU rating, connectors/wire gauges and enclosure/airflow details when their dependencies are known. The exact open list remains in the [target BOM](../../../hardware/generation-3-target-bom.md#selections-intentionally-deferred). |
| KB-007 | Medium / imaging and interface | Resolve frame-camera sensor/lens and CSI-versus-USB integration. The optional nozzle camera remains a possible upgrade. Follow the [architecture](../../final-build-architecture.md#component-level-selections-still-open); do not promote it to a baseline requirement. |
| KB-008 | Medium / illustrations | No standalone project illustration catalogue or local illustration assets have been established in this checkout. Imported period text references images that are not bundled. Track source/licence and separate future diagrams from photo evidence; see [Illustrations](../indexes/Illustrations.md). |
| KB-009 | Medium / archaeology documentation | Expand the detailed per-image table for photographs 073–080 without assigning retrospective provenance. The gap is recorded by the [detailed inventory](../../00-archaeology/05-detailed-photo-inventory.md). |
| KB-010 | Medium / Generation 3 smart spools | Resolve reader/antenna, tag schema, load cell/holder, controller, service/database and UI details; validate real-tag decoders and profile mappings before claiming support. Follow the [smart-spool open decisions](../../../hardware/generation-3-smart-spool-system.md#open-component-level-decisions), preserving manual fallback and stable weighing as the inventory reference. |
| KB-011 | High / Generation 3 candidate evaluation | Evaluate filament-motion sensing, hardware emergency stop/controls, probe plus nozzle cleaning, maintenance/electrical telemetry and automated pre-print checks according to the [candidate register](../../../hardware/generation-3-enhancement-candidates.md). Record integration, failure-mode and maintenance review before promoting any candidate. Hardware emergency-stop topology remains an open final-safety design item. |
| KB-012 | Medium / Generation 3 RASS | Resolve RASS feeder/spool-drive motors, motor drivers, feeder geometry/encoder, buffer-dancer mechanism and sensing, spool-rotation feedback, PTFE routing, fallback/freewheel design and control calibration. Preserve the toolhead direct-drive extruder as master and keep the full spool support inside the calibrated load-cell path. See [RASS open decisions](../../../hardware/generation-3-rass.md#open-component-level-decisions). |

Further commissioning, spare-electronics evaluation and legacy-filament qualification remain planned work in the [roadmap](../../ROADMAP.md), [spares record](../../00-archaeology/06-motion-electronics-spares.md) and [filament inventory](../../01-filaments/01-inventory.md). Their presence in inventory does not establish a passing test.
