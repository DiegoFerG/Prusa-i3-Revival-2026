---
type: system
area: mechanics
status: in-progress
phase: stage-02
priority: high
generation: original
updated: 2026-09-20
---

# Mechanics

## Current reconstruction

Stage 02 rebuilds the original steel-frame machine using the recovered threaded base, smooth rods, LM8UU bearings, T2.5 transmission and M5 Z drive. Rod-to-axis assignments remain qualified as probable in the [hardware baseline](../../../hardware/README.md). Follow the [original reassembly manual](../../02-reassembly/original-reassembly-manual.md) for dimensions, orientation and checks.

The [reassembly evidence index](../../../photos/03-reassembly/INDEX.md) documents Stage A and progress through manual Stages B–G. Photographic coverage does not by itself certify alignment, bearing condition or successful completion of the final mechanical checks.

## Future Generation 3

The [frozen linear-motion architecture](../../../hardware/generation-3-linear-motion.md) specifies MGN12-class guides on X/Y/Z, GT2 on X/Y and independent Tr8 Z drives. The original flat steel frame plus the 2× M10×350 mm longitudinal and 4× M8×200 mm transverse threaded rods remain the functional Generation 3 skeleton.

X uses a commercial aluminium T-slot extrusion as the structural MGN12 beam. Y uses two longitudinal T-slot extrusion rail carriers mounted to the historical M8/M10 base; 2020/2040-class profiles are the current family to evaluate, with exact sections deferred to CAD and measurement.

Z deliberately avoids adding profile unless needed: direct MGN12 mounting to the measured steel frame is preferred, a thin aluminium backing/reference plate is the second choice, and T-slot extrusion is the fallback only when metrology or packaging requires it. All final rail systems must remain alignable and independently lockable without forcing the rails.

The original frame, threaded-rod base, bed footprint and machine envelope remain constraints in the [final-build architecture](../../final-build-architecture.md).

## Continue here

- [Stage 02 navigation](../build/Stage-02-Original-Reassembly.md) — original assembly sequence and evidence.
- [Parts](../indexes/Parts.md) — component inventories and target BOM.
- [Heated bed](Heated-Bed.md) — original versus final bed geometry.
- [Open issues](../project/Open-Issues.md) — unresolved measurements and condition checks.

[Systems](Systems.md) · [Home](../Home.md)
