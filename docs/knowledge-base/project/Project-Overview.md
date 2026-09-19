---
type: project
area: project
status: active
updated: 2026-09-19
---

# Project Overview

[Home](../Home.md) · [Current State](Current-State.md) · [Roadmap](Roadmap.md)

Restore and modernize the recovered classic Prusa i3 while preserving its documented history, steel frame, silhouette and machine envelope. The [repository overview](../../../README.md) owns the project scope and original baseline.

## Three generations, one machine

| Generation | Role | Authoritative sources |
| --- | --- | --- |
| 1 — Original Hardware Revival | Reconstruct the original geometry and establish a legacy 3 mm / 2.85 mm printing baseline with Arduino Mega 2560 and RAMPS-era hardware | [Overview](../../../README.md), [reassembly manual](../../02-reassembly/original-reassembly-manual.md) |
| 2 — Re-ARM transitional study | Document and, if worthwhile, evaluate the recovered period 32-bit upgrade path | [Hardware](../../../hardware/README.md), [motion-electronics spares](../../00-archaeology/06-motion-electronics-spares.md) |
| 3 — Revival 2026 final build | Implement the frozen modern mechanical/control architecture after earlier generations have been documented and tested | [Final architecture](../../final-build-architecture.md), [linear motion](../../../hardware/generation-3-linear-motion.md), [target BOM](../../../hardware/generation-3-target-bom.md) |

A **roadmap stage** is a workstream numbered 00–10. A **manual stage** is a reconstruction step lettered A–J inside roadmap Stage 02. A **generation** is a machine configuration. Generation 3 is not roadmap Stage 03.

Generation 3 also includes the frozen [smart-spool architecture](../../../hardware/generation-3-smart-spool-system.md). The separate [enhancement candidates](../../../hardware/generation-3-enhancement-candidates.md) remain proposals; their presence in the repository does not promote them into the frozen build.

## Constraints to carry forward

- Document before changing; reconstruct before redesigning. Preserve evidence IDs, provenance and confidence levels. See [method and provenance](../../00-archaeology/03-method-and-provenance.md).
- Keep the original bed footprint and travel envelope; measure the bed PCB before releasing final bed CAD. See [architecture](../../final-build-architecture.md).
- Preserve the red structural printed parts / black frame-and-rods identity. Final ASA preference and enclosure exceptions are defined in the [visual identity policy](../../final-build-architecture.md#visual-identity-and-colour-policy).
- Build new wiring; recovered wiring is evidence only. Stage 02 remains mechanical. See [reassembly scope](../../02-reassembly/README.md).

## Reading this knowledge base

These pages are a navigation and status layer over the existing manuals, inventories and architecture. Detailed measurements, BOM rows, photographs and procedures stay in their existing locations. Start with [Systems](../systems/Systems.md), [Build](../build/Build.md) or the [Documentation index](../indexes/Documentation.md).
