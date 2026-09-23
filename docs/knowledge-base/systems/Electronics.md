---
type: system
area: electronics
status: documented
phase: stage-02
priority: high
generation: original
updated: 2026-09-23
---

# Electronics

## Recovered baseline

The [hardware inventory](../../../hardware/README.md) identifies Arduino Mega 2560, StaticBoards RAMPS 1.4SB, four A4988-family drivers, a graphic LCD/adapter, mechanical endstops and the JCPOWER JC-360-12 supply. Identification is not electrical clearance: motor condition, endstop operation and power hardware still require controlled testing.

During Stage 02, [manual Stage J](../build/Phase-J.md) permits historical mechanical placement only. The recovered mixed wiring harness is archival evidence and will not be reused.

## Generation boundaries

The [final-build architecture](../../final-build-architecture.md) separates the original hardware, the Re-ARM transitional study and the future Generation 3 machine. Generation 3 targets Manta M8P V2.0 + CB2 + TMC2209, 24 V power, CEB distribution and an EBB36 Gen2 CAN toolhead. The Manta M8P V2.0, EBB36 Gen2 kit and 6× BTT TMC2209 V1.3 have now been purchased; purchase does not establish electrical testing or commissioning. See the [target BOM](../../../hardware/generation-3-target-bom.md) for frozen versus deferred selections; a target entry is not proof of purchase or installation.

CB2 remains the frozen final host but is not yet purchased; a temporary Linux PC/Raspberry Pi may host Klipper over USB solely for Manta bench testing. A [Generation 3 electronics bench-test pack](../../../hardware/bench-tests/generation-3-electronics/README.md) now defines the receiving, Manta/TMC, EBB36 and CAN acceptance sequence. Preparing the procedure is not evidence that any part passed. Exact PSU wattage, connector families, wire gauges and routing remain open until loads and interfaces are defined. New electrical design and wiring belong to [Roadmap Stage 05](../../ROADMAP.md).

## Related work

The [procurement status](../../../hardware/generation-3-procurement-status.md) is the canonical record for Generation 3 purchases and receiving tests. The [smart-spool target](../../../hardware/generation-3-smart-spool-system.md) adds separate reader/weighing electronics with wired USB to CB2 preferred; exact parts and integration are deferred. The [RASS extension](../../../hardware/generation-3-rass.md) adds local motor control for spool assistance and the upstream feeder plus buffer/dancer sensing; it remains separate from the motion-control MCU and prefers USB to CB2. The [enhancement register](../../../hardware/generation-3-enhancement-candidates.md) separately prioritises minimal-hardware/high-impact studies including filament-motion sensing, hardware emergency stop/controls, nozzle cleaning, DC power monitoring, ambient/abnormal-air sensing, optional additional temperature sensing, nozzle camera, CB2 graceful-shutdown support and later position/acoustic/thermal diagnostics. These candidates are not installed, purchased or automatically frozen by their inclusion.

- [Safety](Safety.md) — no mains power during Stage 02; independent future protections.
- [Firmware](Firmware.md) — software responsibilities and configuration storage.
- [Heated bed](Heated-Bed.md) — dedicated future power stage and protection.
- [User interface](User-Interface.md) — original LCD and final touchscreen.

[Systems](Systems.md) · [Parts](../indexes/Parts.md)
