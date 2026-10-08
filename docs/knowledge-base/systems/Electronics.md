---
type: system
area: electronics
status: documented
phase: stage-02
priority: high
generation: original
updated: 2026-10-08
---

# Electronics

## Recovered baseline

The [hardware inventory](../../../hardware/README.md) identifies Arduino Mega 2560, StaticBoards RAMPS 1.4SB, four A4988-family drivers, a graphic LCD/adapter, mechanical endstops and the JCPOWER JC-360-12 supply. Identification is not electrical clearance: motor condition, endstop operation and power hardware still require controlled testing.

During Stage 02, [manual Stage J](../build/Phase-J.md) permits historical mechanical placement only. The recovered mixed wiring harness is archival evidence and will not be reused.

## Generation boundaries

The [final-build architecture](../../final-build-architecture.md) separates the original hardware, the Re-ARM transitional study and the future Generation 3 machine. Generation 3 targets Manta M8P V2.0 + CB2 + TMC2209, 24 V power, CEB distribution and an EBB36 Gen2 CAN toolhead. The Manta M8P V2.0, EBB36 Gen2 kit and 6× BTT TMC2209 V1.3 have now been purchased; purchase does not establish electrical testing or commissioning. See the [target BOM](../../../hardware/generation-3-target-bom.md) for frozen versus deferred selections; a target entry is not proof of purchase or installation.

CB2 remains the frozen final host but is not yet purchased; a temporary Linux PC/Raspberry Pi may host Klipper over USB solely for Manta bench testing. A [Generation 3 electronics bench-test pack](../../../hardware/bench-tests/generation-3-electronics/README.md) now defines the receiving, Manta/TMC, EBB36 and CAN acceptance sequence. Preparing the procedure is not evidence that any part passed. Local upstream manuals, pinouts, schematics, connection diagrams and reference configurations for the purchased controller/toolboard/drivers are preserved in the [BIGTREETECH vendor reference archive](../../../hardware/reference/bigtreetech/README.md); their presence establishes documentation provenance, not electrical acceptance. The final PSU target is now **Mean Well LRS-600-24 (24 V / 25 A / 600 W)**, with purchase deferred until the final load budget is rechecked. An existing NUOFUWEI S-24-600 of the same nominal rating may be reused for bench/prototype work after inspection. A [dedicated PSU enclosure and 24 V distribution specification](../../../hardware/generation-3-power-distribution.md) now establishes seven independently protected XT60E panel outlet provisions (Manta logic, drivers, bed heater, EBB feed, CAN logic, auxiliaries and spare) and XT30(2+2) vertical PCB / cable CAN harness candidates. Actual fuse values, Manta domains, connector footprints and wire sizes remain engineering validation gates. This is a specification, not installed or tested hardware. New electrical design and wiring belong to [Roadmap Stage 05](../../ROADMAP.md).

## Bed-local electronics

The final bed uses a custom [Revival Bed Node](../../../hardware/generation-3-bed-node.md) as a CAN node on the CEB V1.0 backbone, with USB-C retained for first flash, recovery, bench diagnostics and optional alternate runtime. Initial commissioning intentionally uses separate thermistor/heater/accelerometer wiring so PCB development does not block the printer. The final fixed node integrates bed sensing and local heater-stage control, interfaces to a remote LIS2DW-class daughterboard on the moving bed, includes a local chassis accelerometer, provides a remote frame-top accelerometer port, monitors electrical/thermal telemetry and drives 24 V RGB status lighting, while retaining an independent branch fuse and thermal fuse. Both this board and the RASS CAN Node follow the [common custom-node rules](../../../hardware/generation-3-custom-can-node-design-rules.md): unmodified upstream Klipper MCU firmware and a mandatory post-allocation reserve of SPI/I2C/UART/ADC/GPIO/PWM resources.

## Related work

The [procurement status](../../../hardware/generation-3-procurement-status.md) is the canonical record for Generation 3 purchases and receiving tests. The [smart-spool target](../../../hardware/generation-3-smart-spool-system.md) adds reader/weighing and host-side inventory/decoder services; exact parts and integration remain deferred. The [RASS extension](../../../hardware/generation-3-rass.md) adds a **custom Klipper-compatible CAN node** on the CEB V1.0 backbone for spool-assist motor control, upstream feeder control and buffer/encoder sensing. High-level RFID/NFC decoding and inventory logic remain separate from deterministic RASS motor control. The [Revival Intelligence & Diagnostics subsystem](../../../hardware/generation-3-revival-intelligence-diagnostics.md) owns the supervisory diagnostic concept; its [RID candidate backlog](../../../hardware/generation-3-enhancement-candidates.md) separately prioritises minimal-hardware/high-impact studies including filament-motion sensing, hardware emergency stop/controls, nozzle cleaning, DC power monitoring, ambient/abnormal-air sensing, optional additional temperature sensing, nozzle camera, CB2 graceful-shutdown support and later position/acoustic/thermal diagnostics. These candidates are not installed, purchased or automatically frozen by their inclusion.

- [Safety](Safety.md) — no mains power during Stage 02; independent future protections.
- [Firmware](Firmware.md) — software responsibilities and configuration storage.
- [Heated bed](Heated-Bed.md) — dedicated future power stage and protection.
- [User interface](User-Interface.md) — original LCD and final touchscreen.

[Systems](Systems.md) · [Parts](../indexes/Parts.md)
