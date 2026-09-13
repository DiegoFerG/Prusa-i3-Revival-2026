# Archaeology method and provenance

Prusa i3 Revival 2026 treats the original configuration as technical evidence. The goal is not merely to make the printer work again; we also want to explain **what was there, how it was built, what we kept, and why we changed it**.

## Primary rule

**Document before dismantling.**

Do not clean, cut wires, remove labels, alter connectors or discard parts before recording their condition and provenance.

## Confidence levels

Every technical identification uses one of these states:

- **CONFIRMED** — visible on a label/silkscreen or demonstrated by measurement.
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

## Future teardown workflow

For every subsystem:

1. photograph before touching it;
2. assign an ID;
3. photograph connections and orientation;
4. remove in a controlled manner;
5. clean;
6. record measurements and references;
7. perform mechanical/electrical tests where appropriate;
8. decide: **REUSE / RESTORE / REPLACE / REDESIGN / ARCHIVE**;
9. record the decision and rationale;
10. photograph the classified component.

## Safety

The printer will not simply be powered to see whether it still works. The PSU, mains wiring, heated bed, MOSFETs, connectors, insulation and wiring must be inspected first.

## Photography

Original files are evidence and remain immutable. Blog versions, annotations and comparisons are generated as derivatives.

## Traceability

Future design decisions should link, whenever possible:

`original evidence → measurement/test → decision → CAD/BOM → result`

This chain is a central part of the project's value to the community.
