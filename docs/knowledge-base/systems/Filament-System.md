---
type: system
area: filament
status: documented
priority: normal
updated: 2026-09-19
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

A filament-motion/jam sensor is a separate [enhancement candidate](../../../hardware/generation-3-enhancement-candidates.md), not proof of spool identification or weighing and not yet frozen hardware.

[Parts](../indexes/Parts.md) · [Photos](../indexes/Photos.md) · [Systems](Systems.md)
