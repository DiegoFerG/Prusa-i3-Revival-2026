---
type: system
area: user-interface
status: planned
phase: stage-05
priority: normal
generation: generation-3
updated: 2026-09-19
---

# User interface

## Historical baseline

The [hardware inventory](../../../hardware/README.md) documents a RepRapDiscount-style full graphic smart controller, RAMPS adapter and Panasonic SDHC card. SD contents have not been accepted as trusted project documentation. [Manual Stage J](../build/Phase-J.md) is mechanical placement, not functional validation.

## Generation 3 target

The [final-build architecture](../../final-build-architecture.md) specifies an HDMI5 five-inch touchscreen with KlipperScreen and a custom retro industrial enclosure. Mainsail provides remote access. A fixed frame camera is part of the concept, with CSI preferred and USB permitted; its actual model and final interface remain open.

Camera housings follow a retro CCTV visual language. The optional nozzle camera remains a possible future upgrade and is not part of the frozen base moving harness. Lighting and status colours are defined in the same architecture.

This page records the target experience; there is no claim that the new display, camera or interface is installed.

The [smart-spool UI requirements](../../../hardware/generation-3-smart-spool-system.md#user-experience) add spool identity, remaining mass, profile mapping, calibration and assisted registration with manual fallback. Exact UI integration is still open. A retro physical control panel is a separate [enhancement candidate](../../../hardware/generation-3-enhancement-candidates.md), not a frozen implemented interface.

[Electronics](Electronics.md) · [Firmware](Firmware.md) · [Decision log](../decisions/Decision-Log.md) · [Systems](Systems.md)
