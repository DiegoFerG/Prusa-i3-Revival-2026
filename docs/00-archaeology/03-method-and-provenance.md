# Archaeology method and provenance

Prusa i3 Revival 2026 treats the original configuration as technical evidence. The goal is not merely to make the printer work again; the project must be able to explain **what was there, how it was built, what was retained, and why anything was changed**.

## Primary rule

**Document before changing.**

During Stage 00 this meant document before dismantling. During later stages the same rule applies before cleaning, repairing, modifying or replacing a component when that change would destroy useful evidence.

## Confidence levels

Every technical identification uses one of these states:

- **CONFIRMED** — visible on a label/silkscreen or demonstrated by measurement/test.
- **PROBABLE** — geometry and context fit, but confirmation is still missing.
- **PENDING** — insufficient evidence.

A probable identification must never silently become a historical fact.

## Provenance classes

### PRINTER-AS-FOUND
Physically installed on the printer when the project began.

### LOOSE-FOUND
Found loose in boxes associated with the old 3D-printing material. It may be a spare, removed part, experiment or unused component.

### DONATED-PURCHASED
Known to have been donated or purchased at the time, but not necessarily used on this printer.

### PERIOD-UNRELATED
Contemporary hardware found with the material, with no demonstrated relationship to the Prusa.

### REVIVAL-2026
Component purchased, manufactured or designed specifically for the current rebuild.

## Teardown workflow used in Stage 01

The controlled teardown followed this reusable sequence:

1. photograph before touching the subsystem;
2. assign/retain a stable evidence ID;
3. photograph connections and orientation;
4. remove in a controlled manner;
5. clean;
6. record measurements and references;
7. perform mechanical/electrical tests where appropriate;
8. decide or defer: **REUSE / RESTORE / REPLACE / REDESIGN / ARCHIVE**;
9. record the evidence and rationale;
10. create cleaned inventory photographs without altering the original evidence files.

**Stage 01 teardown, cleaning and inventory closed on 13 September 2026.** Its photo sequence currently reaches `TD-20260913-228`.

## Reassembly workflow

Stage 02 adds a complementary rule: **reconstruct before redesigning**. The documented original geometry will first be reassembled and checked mechanically. Modernization ideas may be recorded during that work, but they should not be allowed to erase the evidence of how the original machine fit together.

## Safety

The printer will not simply be powered to see whether it still works. The PSU, mains wiring, heated bed, power connectors, insulation and protection arrangements must be inspected before electrical commissioning. The old mixed wiring harness is evidence only and is not selected for reuse.

## Photography

Original evidence files remain immutable. Crops, annotations, web-optimised images and cleaned component-inventory images are derivatives and must remain clearly separated from originals.

The cleaned Stage 01 component inventory is intentionally stored under `photos/02-teardown/derived/component-inventory/` because those JPEGs were re-encoded from pixels after orientation and privacy metadata removal.

## Traceability

Design decisions should link, whenever possible:

`original evidence → measurement/test → decision → CAD/BOM → result`

This chain is a central part of the project's value to the community.
