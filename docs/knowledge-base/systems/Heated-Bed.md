---
type: system
area: heated-bed
status: in-progress
phase: stage-02
priority: high
generation: original
updated: 2026-09-30
---

# Heated bed

## Original baseline

The [hardware inventory](../../../hardware/README.md) records the recovered heated-bed PCB, approximate Y-carriage dimensions, levelling hardware and 200 × 200 × 3 mm SÖRLI mirrors. The carriage and mirror dimensions must not be substituted for the actual PCB footprint.

[Manual Stage D](../build/Phase-D.md) reconstructs the original bed mechanically with no electrical connection. The [16 September evidence batch](../../../photos/03-reassembly/BATCH-20260916.md) contains Stage D progress photographs; this does not establish electrical safety, flatness or completion of all checks.

## Future Generation 3

The [final-build architecture](../../final-build-architecture.md) freezes an original-footprint aluminium/silicone/magnetic/flexible-PEI bed at 24 V, with an external DC power stage, branch fuse and independent thermal fuse. The exact aluminium thickness, heater dimensions and wattage remain open until the original PCB is measured. See the [target BOM bed-size rule](../../../hardware/generation-3-target-bom.md).

The bed-control architecture is staged. Initially, thermistor and heater control remain conventionally wired to the Manta/external MOSFET and a separate USB S2DW-class accelerometer is mounted to the moving bed. The final design migrates these local functions to the custom [Revival Bed Node](../../../hardware/generation-3-bed-node.md), a USB secondary Klipper MCU in a printed enclosure on the fixed rear cross-member. A tiny remote IMU daughterboard remains on the moving bed. Heater energy still travels on its own 24 V high-current pair.

The Bed Node also provides structural/diagnostic sensing: a local chassis accelerometer, the remote moving-bed IMU and a remote frame-top IMU, plus heater voltage/current/thermal telemetry and 24 V RGB status lighting. These features support Klipper tuning and RID analysis but do not replace physical protection: the dedicated bed branch fuse and independent thermal fuse remain mandatory even if the local MCU controls the MOSFET.

A **BIGTREETECH Eddy Duo** is now part of the frozen Generation 3 Roto + Revo toolhead architecture for rapid/dense surface scanning. Its independent 5 V CAN-node topology downstream of the EBB36 Gen2 passthrough is frozen. Final mount, offsets, connector pinout, physical CAN harness, thermal calibration and repeatability on the actual bed stack remain to be validated. See the [toolhead target](../../../hardware/generation-3-extrusion-toolhead.md).

[Mechanics](Mechanics.md) · [Electronics](Electronics.md) · [Safety](Safety.md) · [Systems](Systems.md)
