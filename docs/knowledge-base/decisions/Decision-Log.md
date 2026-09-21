---
type: decision-log
area: project
status: active
updated: 2026-09-20
---

# Decision Log

[Home](../Home.md) · [Open Issues](../project/Open-Issues.md)

This register indexes decisions already present in the repository. It does not re-approve them or turn target selections into installed/tested hardware. Dates are included only where the source states them; the register was assembled on 19 September 2026.

| ID | Decision | State | Source / rationale |
| --- | --- | --- | --- |
| DEC-001 | Document before changing; reconstruct the original geometry before redesigning | Established project rule | [Method and provenance](../../00-archaeology/03-method-and-provenance.md) preserves the evidence chain |
| DEC-002 | Keep original revival, Re-ARM study and final build as distinct machine generations | Established project scope | [Overview](../../../README.md#project-generations), [architecture scope](../../final-build-architecture.md#scope-and-generation-model) |
| DEC-003 | Preserve steel frame, silhouette, bed footprint and travel envelope | Frozen Generation 3 constraint; architecture agreed 13 September 2026 | [Non-negotiable constraints](../../final-build-architecture.md#non-negotiable-constraints) |
| DEC-004 | Use the Manta/CB2/Klipper, 24 V and CAN toolhead target architecture | Frozen architecture, implementation deferred | [Final architecture](../../final-build-architecture.md), [target BOM](../../../hardware/generation-3-target-bom.md) |
| DEC-005 | Use MGN12-class guidance with alignable metallic reference structures; GT2 X/Y drive and independent Tr8 Z drive | Frozen architecture; dimensions and detailed selections deferred | [Linear-motion architecture](../../../hardware/generation-3-linear-motion.md) |
| DEC-006 | Preserve red structural printed parts / black frame and rods; prefer suitable ASA for the final build | Established visual identity | [Colour policy](../../final-build-architecture.md#visual-identity-and-colour-policy); enclosure exceptions remain explicit |
| DEC-007 | Reproduce blocking original parts during Stage 02 when necessary; ABS is acceptable if ASA is unavailable | Established Stage 02 allowance | [Reassembly scope](../../02-reassembly/README.md#temporary-replacement-parts-during-reassembly); does not freeze final material |
| DEC-008 | Replace all legacy wiring; keep critical protection independent of host software | Established safety constraint | [Architecture](../../final-build-architecture.md#non-negotiable-constraints), [provenance](../../00-archaeology/03-method-and-provenance.md#safety) |
| DEC-009 | Distinguish recovered spare electronics from installed historical components | Established evidence rule | [Motion-electronics spares](../../00-archaeology/06-motion-electronics-spares.md) and [provenance classes](../../00-archaeology/03-method-and-provenance.md#provenance-classes) |
| DEC-010 | Use the repository itself as the Obsidian vault, with English relative Markdown links and native features | Implemented locally; publication approved by the user on 19 September 2026 | [Maintenance](../Maintenance.md), [repository instructions](../../../AGENTS.md). Native features only; no community plugins installed. |
| DEC-011 | Include smart-spool identification, assisted unknown-tag learning, local inventory/profile mapping and load-cell weighing in Generation 3 | Frozen architecture; hardware, software and real-tag support remain to be implemented/validated | [Smart-spool decisions](../../../hardware/generation-3-smart-spool-system.md#frozen-architectural-decisions), [target BOM](../../../hardware/generation-3-target-bom.md). Manual fallback and calibrated Revival profiles remain explicit. |
| DEC-012 | Evaluate fault detection, fast probing/cleaning, physical controls, telemetry and pre-print automation separately from frozen requirements | Proposed candidates; no automatic promotion into the baseline | [Enhancement evaluation rule](../../../hardware/generation-3-enhancement-candidates.md#evaluation-rule) and [priorities](../../../hardware/generation-3-enhancement-candidates.md#promotion-priorities). |
| DEC-013 | Use RASS as the Generation 3 single-spool active-feed architecture: driven spool assistance + upstream feeder + buffer/dancer, while the toolhead direct drive remains extrusion master | Frozen architecture; component selection and control tuning deferred | [RASS frozen decisions](../../../hardware/generation-3-rass.md#frozen-architectural-decisions), [target BOM](../../../hardware/generation-3-target-bom.md). |
<<<<<<< HEAD
| DEC-014 | Preserve the original printable designs locally, retaining upstream bytes, attribution, revisions and hashes; keep adaptations separate | Archive implemented locally, 19 September 2026; exact physical fit remains open | [Archive](../../../printed-parts/original-designs/README.md), requested by the owner after finding the missing small-gear file; [KB-013](../project/Open-Issues.md#kb-013--exact-original-printable-part-coverage) tracks remaining identification and fit. |
=======
| DEC-014 | Use E3D Roto + Revo for Generation 3 direct-drive extrusion; optimise primarily for high-quality PLA, with occasional ABS/ASA and no heated-chamber requirement | Frozen architecture / use-case intent; exact SKU and final CAD deferred | [Extrusion/toolhead target](../../../hardware/generation-3-extrusion-toolhead.md), [target BOM](../../../hardware/generation-3-target-bom.md). |
| DEC-015 | Use BIGTREETECH Eddy Duo with the EBB36 Gen2 + Roto + Revo toolhead for rapid/dense eddy-current scanning of the Generation 3 spring-steel/magnetic bed | Frozen architecture; Eddy is an independent 5 V CAN node downstream of the EBB36 passthrough; mount, offsets, harness and calibration deferred | [Extrusion/toolhead target](../../../hardware/generation-3-extrusion-toolhead.md), [final architecture](../../final-build-architecture.md). |
| DEC-016 | Keep CB2 as the final Generation 3 host rather than buying a higher-priced CM4 solely for availability; permit temporary external Linux host over USB for Manta bench testing | Frozen host choice / procurement rule | [Procurement status](../../../hardware/generation-3-procurement-status.md), [final architecture](../../final-build-architecture.md). |
| DEC-017 | Record Manta M8P V2.0, EBB36 Gen2 kit and 6× BTT TMC2209 V1.3 as purchased Generation 3 stock; four plug-in drivers cover base X/Y/Z0/Z1 and two remain spare | Purchased, not yet tested or commissioned | [Procurement status](../../../hardware/generation-3-procurement-status.md), [target BOM](../../../hardware/generation-3-target-bom.md). |
| DEC-018 | Preserve the original flat steel frame and the complete 2× M10×350 + 4× M8×200 threaded-rod lower structure as functional Generation 3 mechanics; do not replace them with an extrusion chassis | Frozen Generation 3 constraint; agreed 20 September 2026 | [Final architecture](../../final-build-architecture.md#non-negotiable-constraints), [linear-motion architecture](../../../hardware/generation-3-linear-motion.md#design-intent) |
| DEC-019 | Use commercial aluminium T-slot profiles as X/Y MGN12 support structures, with exact 2020/2040-class sections deferred; for Z prefer direct rail mounting to the steel frame, then thin aluminium backing plates, and use profiles only if metrology requires them | Frozen mechanical architecture; exact dimensions and final Z implementation deferred to measured CAD | [Linear-motion architecture](../../../hardware/generation-3-linear-motion.md#frozen-axis-architecture), [target BOM](../../../hardware/generation-3-target-bom.md) |
>>>>>>> e3ea30161f3ec71d9c18876863de755e655eaf0b

## Recording the next decision

Update the authoritative architecture, inventory or test document first. Add a stable decision ID here with the decision date, status, rationale and source link. For a revision, link the superseding decision and preserve the previous outcome. Reflect affected system/build pages, [Current State](../project/Current-State.md), [Roadmap](../project/Roadmap.md) and [Open Issues](../project/Open-Issues.md).
