---
type: system
area: filament
status: documented
priority: normal
updated: 2026-09-23
---

# Filament system

The scope covers recovered filament qualification and the future Generation 3 smart-spool system. The legacy inventory and future automation have separate evidence and implementation states.

## Inventory and qualification

The [canonical legacy inventory](../../01-filaments/01-inventory.md) contains ten spool records linked to eleven label/packaging photographs. It records visual and label inspection only: remaining mass is unknown, and no spool has yet been dried or test-printed in the Revival according to that source.

Keep spool facts, measurements and qualification results in that inventory. Its proposed qualification procedure and `PASS`, `LIMITED USE`, `DISPLAY/ARCHIVE` and `REJECT` outcomes are distinct from hardware component-condition states.

## Sequence and future interfaces

[Roadmap Stage 06](../../ROADMAP.md) prepares legacy 3 mm / 2.85 mm extrusion, Stage 08 evaluates old material and Stage 09 performs the later 1.75 mm conversion. Consult [Extrusion](Extrusion.md) for current hotend uncertainties.

## Generation 3 smart-spool target

The [smart-spool architecture](../../../hardware/generation-3-smart-spool-system.md) and [target BOM](../../../hardware/generation-3-target-bom.md) freeze a future RFID/NFC identification and load-cell weighing subsystem. Its model separates material identity from Revival-calibrated machine profiles and uses stable gross mass minus tare for inventory correction. Implementation and real-tag compatibility remain to be validated.

The target includes Revival-native tags, OpenPrintTag and supported Bambu import, with Creality as a planned validation target. Readable unknown tags use assisted registration/learning; protected or unsupported tags retain manual fallback. Exact reader, antenna, tag schema, load cell, holder, controller and service/UI implementation remain open in the [source decisions](../../../hardware/generation-3-smart-spool-system.md#open-component-level-decisions).

RASS is the frozen active-feed extension to this subsystem. The [RASS architecture](../../../hardware/generation-3-rass.md) adds driven-spool assistance, a feeder near the spool and an intermediate buffer/dancer so the toolhead direct-drive extruder remains the master extrusion actuator. Exact production motors, feeder mechanics, buffer sensing and control calibration remain open. An existing **28BYJ-48 5 V geared stepper + ULN2003 board** has been selected as the preferred prototype candidate for spool-rotation assistance only; it is explicitly not the precision feeder motor. See the [RASS motor-selection section](../../../hardware/generation-3-rass.md#motor-selection-philosophy).

A filament-motion/jam sensor is a separate [enhancement candidate](../../../hardware/generation-3-enhancement-candidates.md), although its future signals may complement RASS diagnostics. It is not proof of spool identification or weighing and is not yet frozen hardware.

[Parts](../indexes/Parts.md) · [Photos](../indexes/Photos.md) · [Systems](Systems.md)
