# 00 — Archaeology

This stage documents the machine **before cleaning, dismantling or replacing components**.

## Status

**CLOSED — 12 September 2026.**

Stage 00 remains a frozen non-invasive baseline. At the moment this stage closed, the printer had not yet been dismantled; that statement is historical context, not the current project state.

**Downstream update:** Stage 01 teardown, cleaning and component inventory was completed on **13 September 2026**. The printer is now dismantled and catalogued, and the next project step is original mechanical reassembly. Technical identifications resolved during teardown belong to Stage 01 and are cross-referenced rather than retroactively rewritten into the as-found evidence.

## Objectives achieved

- Photograph the complete machine and major subsystems before dismantling.
- Inventory loose recovered parts separately from installed hardware.
- Preserve provenance and confidence levels.
- Avoid powering uninspected electrical hardware.
- Create a traceable source for the technical documentation and bilingual blog.

## Frozen evidence

A set of **80 original ARQ photographs** is preserved at:

`photos/00-archaeology/originals/`

The archive includes both printer-as-found evidence and loose period material. Loose material is never assumed to have been part of the printer without evidence.

## What later teardown resolved

Stage 01 subsequently confirmed, among other things:

- Arduino Mega 2560 + StaticBoards RAMPS 1.4SB installed controller stack;
- 4× A4988-family plug-in driver modules;
- 5× Wantai 42BYGHW811 NEMA17 motors;
- JCPOWER JC-360-12, 12 V / 30 A PSU;
- measured rod and Y-carriage dimensions;
- T2.5 belt transmission;
- LM8UU-family linear bearings and FAG 608Z radial bearings;
- four IKEA SÖRLI 200 × 200 × 3 mm build-surface mirrors;
- legacy E3D-family hotend and thermistor assembly.

See [Stage 01 teardown photos](../../photos/02-teardown/README.md) and the [hardware baseline](../../hardware/README.md).

## Documents in this stage

- [01 — Initial inventory](01-initial-inventory.md)
- [02 — Photo catalogue](02-photo-catalogue.md)
- [03 — Archaeology method and provenance](03-method-and-provenance.md)
- [04 — Blog source notes / Chapter 0](04-blog-source-notes-chapter-0.md)
- [05 — Detailed ARQ photo inventory](05-detailed-photo-inventory.md)
- [Photo archive](../../photos/00-archaeology/README.md)

## Critical distinction

The project maintains separate evidence classes for:

1. components physically installed on the printer;
2. items found loose in boxes from the same period;
3. donated/purchased period material;
4. unrelated period hardware;
5. Revival-2026 additions.

A motor, board or printed part found near the Prusa is not considered part of its original configuration unless evidence demonstrates that relationship.

## Archaeology closure rule

Stage 00 IDs and original images remain stable. Later evidence may refine an identification, but it does not alter the fact that the earlier observation was provisional at the time.
