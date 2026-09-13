# 00 — Archaeology

This stage documents the machine **before cleaning, dismantling, or replacing components**.

## Objectives

- Identify the exact Prusa i3 variant.
- Photograph the complete machine and each subsystem.
- Inventory loose recovered parts separately.
- Measure the frame, rods, bearings, fasteners, bed and transmissions during teardown.
- Identify the extruder, hotend, motors, power supply, controller and endstops.
- Classify each component as reuse, restore, replace, redesign or archive.
- Do not power the old electronics before an electrical inspection.
- Preserve enough traceability to turn this stage into both technical documentation and Chapter 0 of the bilingual blog.

## Current status

**CLOSED — 12 September 2026.**

The initial non-invasive archaeology session is frozen as the project's pre-teardown baseline. The printer has **not yet been dismantled**. From this point onward, observations made while removing components belong to the teardown/assessment stage rather than being retroactively folded into the as-found archaeology.

A set of **80 original photographs** is preserved at:

`photos/00-archaeology/originals/`

The archaeology archive also documents loose period electronics, notably a **Panucatt Devices Re-ARM** paired with a **RAMPS 1.4sb**, plus LCDs, Arduino-class boards, heater cartridges, heatsinks, an Ethernet module and assorted fans. Their relationship to the printer is not assumed and their electrical condition is still untested.

The provisional identification points to a classic/Rework-era Prusa i3 / RepRap derivative with a Wade/Greg's-Wade-family geared extruder and an E3D-family hotend. The exact printer variant and several component revisions remain open until teardown and measurement.

## Documents in this stage

- [01 — Initial inventory](01-initial-inventory.md)
- [02 — Photo catalogue](02-photo-catalogue.md)
- [03 — Archaeology method and provenance](03-method-and-provenance.md)
- [04 — Blog source notes / Chapter 0](04-blog-source-notes-chapter-0.md)
- [05 — Detailed photo inventory](05-detailed-photo-inventory.md)
- [Photo archive](../../photos/00-archaeology/README.md)

## Critical distinction

The project maintains two different kinds of evidence:

1. **Components physically installed on the printer.**
2. **Items found loose in boxes from the same period.**

A motor, board or printed part found near the Prusa is not considered part of its original configuration unless evidence demonstrates that relationship.

## Archaeology closure

The as-found evidence set is considered sufficient to begin controlled teardown. Open questions are intentionally carried forward instead of being guessed.

During teardown, follow the documented workflow:

photograph → ID → connections/orientation → removal → cleaning → measurements → test → decision → record

New close-up photographs may clarify an existing ARQ identification, but teardown evidence must be documented as a new stage/batch so the original baseline remains immutable.

## Blog workflow

The blog is a **living project log**, not a final retrospective deliverable. Archaeology provides the source material for the first article/chapter, and every later project stage should update the Spanish and English blog as work actually happens. Technical conclusions in the blog should link back to repository evidence whenever practical.
