---
type: system
area: user-interface
status: planned
phase: stage-05
priority: normal
generation: generation-3
updated: 2026-10-06
---

# User interface

## Historical baseline

The [hardware inventory](../../../hardware/README.md) documents a RepRapDiscount-style full graphic smart controller, RAMPS adapter and Panasonic SDHC card. SD contents have not been accepted as trusted project documentation. [Manual Stage J](../build/Phase-J.md) is mechanical placement, not functional validation.

## Generation 3 target

The [final-build architecture](../../final-build-architecture.md) specifies two distinct local touch interfaces. The main interface is the HDMI5 five-inch touchscreen with KlipperScreen and a custom retro industrial enclosure. A second compact **RASS Spool Panel** sits beside the spool/RASS assembly and is dedicated to material/RASS status plus guarded filament LOAD/UNLOAD requests. Mainsail provides remote access. A fixed **Innomaker U30CAM-4K-S1 (Sony IMX415) USB/UVC** frame camera is the frozen primary camera. The earlier CSI-preferred/model-open statement is obsolete; final mount/framing and validated operating mode remain open until bench and machine tests.

Camera housings follow a retro CCTV visual language. The optional nozzle camera remains a possible future upgrade and is not part of the frozen base moving harness. Lighting and status colours are defined in the same architecture.

This page records the target experience; there is no claim that the new display, camera or interface is installed.

The [smart-spool UI requirements](../../../hardware/generation-3-smart-spool-system.md#user-experience) add spool identity, remaining mass, profile mapping, calibration and assisted registration with manual fallback. The RASS Spool Panel shows a compact subset intended for use while standing at the spool: identity/material/colour, remaining amount, tag state, feeder/buffer state, warnings and nozzle readiness.

Its LOAD/UNLOAD controls are presentation/request controls only. The Linux host decides whether they are enabled and independently revalidates the action when pressed. They remain disabled during printing or pause/resume-capable print state, during incompatible machine activity, when the required MCU/sensors are unavailable, when the hotend is outside the validated filament-handling temperature window, or when the sensed filament/RASS state makes the requested action invalid.

The exact local-panel hardware remains open; a small wired serial HMI is preferred so it does not depend on a second Linux framebuffer. A retro physical control panel remains a separate [enhancement candidate](../../../hardware/generation-3-enhancement-candidates.md), not a replacement for either touchscreen.

[Electronics](Electronics.md) · [Firmware](Firmware.md) · [Decision log](../decisions/Decision-Log.md) · [Systems](Systems.md)
