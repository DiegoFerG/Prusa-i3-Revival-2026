---
type: project
area: project
status: active
phase: stage-02
priority: high
updated: 2026-09-23
---

# Open Issues

[Home](../Home.md) · [Current State](Current-State.md) · [Decision Log](../decisions/Decision-Log.md)

This is a source-linked register of unresolved work. IDs are local knowledge-base identifiers, not GitHub issue numbers. Priorities express dependency order for this register. Close an item only after linking its resolution or test record; preserve its ID.

| ID | Priority / scope | Open item and closure evidence |
| --- | --- | --- |
| KB-002 | High / Stage 02 | Record remaining Stage H mounting/acceptance evidence, manual I–J work and the final mechanical gate. The [21 September batch](../../../photos/03-reassembly/BATCH-20260921.md) reports Stage H assembly complete and documents the geared-extruder subassembly; it does not record all manual checks. Close using results linked from the [manual](../../02-reassembly/original-reassembly-manual.md). |
| KB-003 | High / legacy extrusion | Confirm the legacy hotend revision and thermistor type; resolve the damaged heater-retaining screw/captive heater cartridge. The [roadmap](../../ROADMAP.md) explicitly leaves these unresolved. Record identification and inspection/test evidence in the existing inventory before reuse. |
| KB-004 | High / Generation 3 bed | Measure the original heated-bed PCB footprint and mounting geometry before freezing plate CAD, heater dimensions/power and related load calculations. The carriage and mirror dimensions are not substitutes. See [target BOM](../../../hardware/generation-3-target-bom.md#bed-size-rule). |
| KB-005 | Medium / Generation 3 motion | Resolve rail supplier/preload/lengths, exact X/Y 2020/2040-class profile sections and orientations, profile-to-frame brackets/adjusters, Tr8 lead and the measurement-dependent Z implementation. The Z hierarchy is already frozen: direct steel-frame mounting first, thin aluminium backing plate second, T-slot profile only if required. See [motion architecture](../../../hardware/generation-3-linear-motion.md) and [deferred selections](../../../hardware/generation-3-target-bom.md#selections-intentionally-deferred). |
| KB-006 | Medium / Generation 3 components | EBB36 Gen2 + Roto + Revo + Eddy Duo is the frozen extrusion/probing direction. EBB36 Gen2 is purchased; current Roto/Revo purchase preference is Roto Sensored + Revo 24 V / 40 W. Confirm exact Roto/Revo SKU/revision, toolplate fit, fans/ducts, Eddy mount/offsets/CAN harness/calibration, lighting, PSU rating, connectors/wire gauges and enclosure/airflow details when dependencies are known. See the [toolhead target](../../../hardware/generation-3-extrusion-toolhead.md) and [target BOM](../../../hardware/generation-3-target-bom.md#selections-intentionally-deferred). |
| KB-007 | Medium / imaging and interface | Resolve frame-camera sensor/lens and CSI-versus-USB integration. The optional nozzle camera remains a possible upgrade. Follow the [architecture](../../final-build-architecture.md#component-level-selections-still-open); do not promote it to a baseline requirement. |
| KB-008 | Medium / illustrations | No standalone project illustration assets have been established in this checkout; existing inline design diagrams are indexed separately. Imported period text references images that are not bundled. Track source/licence and separate future diagrams from photo evidence; see [Illustrations](../indexes/Illustrations.md). |
| KB-009 | Medium / archaeology documentation | Expand the detailed per-image table for photographs 073–080 without assigning retrospective provenance. The gap is recorded by the [detailed inventory](../../00-archaeology/05-detailed-photo-inventory.md). |
| KB-010 | Medium / Generation 3 smart spools | Resolve reader/antenna, tag schema, load cell/holder, controller, service/database and UI details; validate real-tag decoders and profile mappings before claiming support. Follow the [smart-spool open decisions](../../../hardware/generation-3-smart-spool-system.md#open-component-level-decisions), preserving manual fallback and stable weighing as the inventory reference. |
| KB-011 | High / Generation 3 candidate evaluation | Work through the prioritised [enhancement candidate register](../../../hardware/generation-3-enhancement-candidates.md): prototype software-only candidates that reuse frozen hardware first, then study minimal-hardware/high-impact candidates one by one. Record benefit, complexity, dependencies, failure modes, safety implications and measurable prototype results before promote/defer/reject decisions. Hardware emergency-stop topology remains an open final-safety design item. |
| KB-012 | Medium / Generation 3 RASS | Resolve RASS feeder/spool-drive motors, motor drivers, feeder geometry/encoder, buffer-dancer mechanism and sensing, spool-rotation feedback, PTFE routing, fallback/freewheel design and control calibration. Preserve the toolhead direct-drive extruder as master and keep the full spool support inside the calibrated load-cell path. See [RASS open decisions](../../../hardware/generation-3-rass.md#open-component-level-decisions). |
| KB-013 | Medium / Generation 3 procurement/bench test | Receive, photograph and bench-test the purchased Manta M8P V2.0, EBB36 Gen2 kit and 6× TMC2209 V1.3 while warranty/return windows are open. The [versioned bench-test pack](../../../hardware/bench-tests/generation-3-electronics/README.md) is now prepared, including Raspberry Pi 2 host setup, six-driver isolation, eight Manta-socket coverage, EBB36 USB checks and a two-node CAN test. CB2 remains pending. Close only after reviewed PASS evidence is recorded in the [procurement status](../../../hardware/generation-3-procurement-status.md). |
| KB-014 | High / original printable parts | Confirm exact design-to-part matches, remaining accessory coverage and source attribution; see [coverage details](#kb-014--exact-original-printable-part-coverage). |

Further commissioning, spare-electronics evaluation and legacy-filament qualification remain planned work in the [roadmap](../../ROADMAP.md), [spares record](../../00-archaeology/06-motion-electronics-spares.md) and [filament inventory](../../01-filaments/01-inventory.md). Their presence in inventory does not establish a passing test.

## KB-014 — Exact original printable-part coverage

**High / Stage 02.** The [historical design sets](../../../printed-parts/original-designs/Original-Printed-Parts.md) are now archived, including the leading 9/47 gear-pair candidate. The supplier and precise kit revision remain unknown. Confirm gear teeth/bore/spacing and each selected part's measured interfaces; identify the remaining mechanical endstop mounts, hotend clamp/duct and loose accessory revisions. Close with source-to-physical-part mapping and fit evidence, not download counts. Preserve source notices; individual attribution/license details for the Clone Wars V2/Extras files also remain to be resolved as recorded in [provenance](../../../printed-parts/original-designs/Provenance.md).

The archive-coverage item previously duplicated the procurement ID KB-013. On 21 September 2026 it was reassigned to KB-014; KB-013 continues to track purchased electronics and bench testing.

## Resolved items

| ID | Resolution date | Closure evidence |
| --- | --- | --- |
| KB-001 | 2026-09-21 | Reconciled the [archaeology photo README](../../../photos/00-archaeology/README.md) with the [catalogue](../../00-archaeology/02-photo-catalogue.md), [spare-box provenance](../../00-archaeology/06-motion-electronics-spares.md) and 89 repository JPEGs: 80 historical baseline images plus nine later sanitized spare-box photographs. Image files and permanent IDs are unchanged. |
