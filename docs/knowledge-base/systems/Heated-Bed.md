---
type: system
area: heated-bed
status: in-progress
phase: stage-02
priority: high
generation: original
updated: 2026-09-20
---

# Heated bed

## Original baseline

The [hardware inventory](../../../hardware/README.md) records the recovered heated-bed PCB, approximate Y-carriage dimensions, levelling hardware and 200 × 200 × 3 mm SÖRLI mirrors. The carriage and mirror dimensions must not be substituted for the actual PCB footprint.

[Manual Stage D](../build/Phase-D.md) reconstructs the original bed mechanically with no electrical connection. The [16 September evidence batch](../../../photos/03-reassembly/BATCH-20260916.md) contains Stage D progress photographs; this does not establish electrical safety, flatness or completion of all checks.

## Future Generation 3

The [final-build architecture](../../final-build-architecture.md) freezes an original-footprint aluminium/silicone/magnetic/flexible-PEI bed at 24 V, with an external DC power stage, branch fuse and independent thermal fuse. The exact aluminium thickness, heater dimensions and wattage remain open until the original PCB is measured. See the [target BOM bed-size rule](../../../hardware/generation-3-target-bom.md).

The permanent Y accelerometer is mounted to the moving bed/carriage and connects to CB2 by USB; this is a future architecture requirement.

A **BIGTREETECH Eddy Duo** is now part of the frozen Generation 3 Roto + Revo toolhead architecture for rapid/dense surface scanning. Final mount, offsets, connection mode, thermal calibration and repeatability on the actual bed stack remain to be validated. See the [toolhead target](../../../hardware/generation-3-extrusion-toolhead.md).

[Mechanics](Mechanics.md) · [Electronics](Electronics.md) · [Safety](Safety.md) · [Systems](Systems.md)
