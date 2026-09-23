---
type: system
area: firmware
status: planned
phase: stage-07
priority: normal
updated: 2026-09-23
---

# Firmware

The current [firmware directory](../../../firmware/README.md) is a placeholder for legacy 3 mm and future 1.75 mm configurations. No commissioned configuration is established by that placeholder.

[Roadmap Stage 07](../../ROADMAP.md) covers configuration, electrical checks, motion and endstop tests, heater safety, PID tuning, calibration and first controlled prints. The current Stage 02 reconstruction is unpowered.

## Future software architecture

The [Generation 3 architecture](../../final-build-architecture.md) freezes Klipper on CB2 with Moonraker, Mainsail, KlipperScreen and Crowsnest. CB2 is not yet purchased; until it is available, a temporary Linux PC/Raspberry Pi may run the Klipper host and connect to the Manta M8P V2.0 by USB for bench testing without changing the final architecture. Manta manages machine axes and enclosure/bed I/O; EBB36 manages local toolhead functions; Eddy Duo is a separate 5 V CAN MCU/node downstream of the EBB36 passthrough; the permanent bed accelerometer connects over USB.

Final configuration, macros and calibration data must be versioned under `firmware/`. The temporary [Generation 3 electronics bench-test pack](../../../hardware/bench-tests/generation-3-electronics/README.md) intentionally keeps its disposable acceptance-test templates beside the hardware procedure; they are not commissioned printer configuration. Any future files should identify the machine generation and actual hardware they were validated against. The architecture is a target, not evidence that this software is already deployed.

## Dependencies

The [smart-spool architecture](../../../hardware/generation-3-smart-spool-system.md) adds a target local service, decoder registry, assisted unknown-tag learning and mappings to calibrated Revival profiles. The [RASS architecture](../../../hardware/generation-3-rass.md) adds a local active-feed controller whose upstream feeder follows toolhead demand through buffer/dancer feedback; exact control implementation and calibration remain future work. Real-tag validation is required before claiming decoder support. The [enhancement candidate register](../../../hardware/generation-3-enhancement-candidates.md) now prioritises software-only work that can reuse the frozen baseline: pre-flight checks, service history, subsystem-health checks, notifications, job/event reports, thermal-response trends, resonance/belt trends, fixed-camera failure detection, first-layer vision, health scoring and later sensor fusion. Candidate status does not imply implementation, and automatic safety actions remain bounded by the independent hardware-safety architecture.

- [Electronics](Electronics.md) — controller, drivers, sensors and wiring.
- [Mechanics](Mechanics.md) — alignment before software compensation.
- [Safety](Safety.md) — software checks supplement physical protections.
- [Filament system](Filament-System.md) — measured material data and later profiles.

[Systems](Systems.md) · [Roadmap](../project/Roadmap.md)
