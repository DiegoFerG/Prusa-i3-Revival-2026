---
type: system
area: electronics
status: documented
phase: stage-02
priority: high
generation: original
updated: 2026-09-19
---

# Electronics

## Recovered baseline

The [hardware inventory](../../../hardware/README.md) identifies Arduino Mega 2560, StaticBoards RAMPS 1.4SB, four A4988-family drivers, a graphic LCD/adapter, mechanical endstops and the JCPOWER JC-360-12 supply. Identification is not electrical clearance: motor condition, endstop operation and power hardware still require controlled testing.

During Stage 02, [manual Stage J](../build/Phase-J.md) permits historical mechanical placement only. The recovered mixed wiring harness is archival evidence and will not be reused.

## Generation boundaries

The [final-build architecture](../../final-build-architecture.md) separates the original hardware, the Re-ARM transitional study and the future Generation 3 machine. Generation 3 targets a Manta M8P V2.0 + CB2 + TMC2209 bundle, 24 V power, CEB distribution and an EBB36 Gen2 CAN toolhead. See the [target BOM](../../../hardware/generation-3-target-bom.md) for frozen versus deferred selections; a target entry is not proof of purchase or installation.

Exact PSU wattage, connector families, wire gauges and routing remain open until loads and interfaces are defined. New electrical design and wiring belong to [Roadmap Stage 05](../../ROADMAP.md).

## Related work

The [smart-spool target](../../../hardware/generation-3-smart-spool-system.md) adds separate reader/weighing electronics with wired USB to CB2 preferred; exact parts and integration are deferred. The [RASS extension](../../../hardware/generation-3-rass.md) adds local motor control for spool assistance and the upstream feeder plus buffer/dancer sensing; it remains separate from the motion-control MCU and prefers USB to CB2. The [enhancement register](../../../hardware/generation-3-enhancement-candidates.md) separately records proposed motion sensing, physical controls and diagnostic electrical monitoring. These candidates are not installed or automatically frozen by their inclusion.

- [Safety](Safety.md) — no mains power during Stage 02; independent future protections.
- [Firmware](Firmware.md) — software responsibilities and configuration storage.
- [Heated bed](Heated-Bed.md) — dedicated future power stage and protection.
- [User interface](User-Interface.md) — original LCD and final touchscreen.

[Systems](Systems.md) · [Parts](../indexes/Parts.md)
