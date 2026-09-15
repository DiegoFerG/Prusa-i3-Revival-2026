# Historical references — Stage 02 reassembly

This index records period sources used to reconstruct how a Prusa i3 of this family would have been assembled around 2012–2014. The project manual does not assume that any generic i3 source exactly matches this printer; repository photographs and measured inventory remain authoritative when they disagree.

## Reference policy

- **Observed project evidence wins** over generic historical instructions.
- Period sources are used to reconstruct assembly logic, naming, orientation and contemporary practice.
- Exact dimensions from external sources are not copied into the build unless confirmed against this printer.
- Documents are stored locally only when redistribution terms are sufficiently clear; otherwise only the external reference is recorded.

## Core sources

### SpainLabs — "Manual de montaje Prusa i3" (3 August 2013)

- URL: https://www.spainlabs.com/foros/showthread.php?tid=228
- Date: 2013-08-03
- Language: Spanish
- Local copy: **not stored**; no explicit redistribution license was identified.
- Importance: **very high** for this specific machine family.
- Why it matters: its published BOM lists 2× M5×310 mm, 4× M8×200 mm, 2× M10×350 mm, 10× LM8UU and 3× 608ZZ — an unusually close match to the recovered printer. The thread also discusses 2.5 A / 1.8° motors and 5-to-5 mm Z couplers, again matching the recovered hardware family.
- Caution: the thread mixes variants and contains known inconsistencies/typos; dimensions and transmission type must be checked against project evidence.

### RepRap Magazine Issue 2 — "Prusa i3 visual instructions" (June 2013)

- Archive page: https://xyzdims.com/3d-printing/reprap-magazine-archive/
- PDF: https://xyzdims.com/wp-content/uploads/2018/07/reprap-magazine-21.pdf
- Original date: 2013-06
- License reported by archive: Creative Commons CC BY-NC-ND.
- Local copy: stored unchanged in `historical-manuals/` when available.
- Importance: high as a contemporary visual assembly source; SpainLabs explicitly states that its August 2013 guide began as a translation/adaptation of this article.
- Caution: the magazine article covers a specific single-plate/Einstein-style configuration and is not dimensionally identical to the recovered printer.

### RepRap / Clone Wars — Prusa iteration 3

- URL: https://reprap.org/wiki/Clone_wars:Prusa_iteración_3
- Period context: Spanish Clone Wars community documentation from the original Prusa i3 era.
- Importance: high for historical context and contemporary Spanish build practice.
- Notable content: links to step-by-step frame, X, Y, Z, heated-bed, extruder and electronics instructions; references the Josef Prusa repository and contemporary video tutorials.
- Local copy: not stored as a webpage snapshot; linked here instead.

### RepRap Wiki — Prusa i3 Build Manual

- URL: https://wiki.reprap.org/wiki/Prusa_i3_Build_Manual
- Importance: high for canonical i3 dimensions, variants and links to original Josef Prusa source files.
- Local copy: not stored as a webpage snapshot; linked here instead.
- Caution: the page covers multiple variants and its generic dimensions do not fully match this printer.

### Josef Prusa — Prusa3 repository

- URL: https://github.com/josefprusa/Prusa3
- License: GPLv3.
- Importance: primary upstream design source for the era.
- Files of interest: historical build notes/manual, dimensions and CAD/reference assemblies.
- Local copies: selected text documentation may be stored in `historical-manuals/` with upstream attribution and license notice.

### RepRap Wiki — Prusa Mendel Assembly (iteration 2)

- URL: https://wiki.reprap.org/wiki/Prusa_Mendel_Assembly_(iteration_2)
- Importance: useful for period assembly conventions inherited by the i3, especially Wade-style geared extruder mounting, belt tension and free-motion checks.
- Local copy: not stored; referenced by URL.

### RepRap Wiki — Prusa i3 Rework Extruder assembly

- URL: https://wiki.reprap.org/wiki/Prusa_i3_Rework_Extruder_assembly
- Importance: useful secondary period-family reference for Wade extruder body, idler, 608 bearings, springs and carriage connection.
- Local copy: not stored; referenced by URL.

### Clone Wars / RepRap — "MONTAJE PRUSA i3 MARCO DE MADERA"

- PDF: https://reprap.org/mediawiki/images/4/46/Prusai3boxframeconstruction.pdf
- Attribution in document: translation/adaptation by Juampe López and Ariadna Trueba from Kliment's i3 photographic documentation.
- License stated in document: GFDL.
- Importance: secondary source for period assembly technique, Y-frame alignment, Z assembly, heated bed, endstops and Jonas extruder.
- Local copy: stored unchanged in `historical-manuals/` when available.
- Caution: this is a box-frame build and dimensions differ significantly from the recovered single-sheet machine.

## Video-era references

The period RepRap/Clone Wars pages also point to:

- "Montando la Prusa Mendel i3" (Spanish): https://www.youtube.com/watch?v=-31Zn7wY7jk
- OverCraft3D aluminium-body Prusa i3 assembly series, linked from the contemporary Clone Wars/RepRap pages.

These are retained as contextual references; the project manual relies on still photographs and measured evidence for any orientation or dimension that must be reproduced exactly.

## Project evidence to consult alongside historical sources

Primary visual evidence is in:

- `photos/00-archaeology/`
- `photos/02-teardown/originals/`
- `photos/02-teardown/derived/component-inventory/`

Especially relevant early references include `TD-20260913-003` through `012` for Z geometry, `TD-20260913-005`, `021`, `032`, `038` for the Y structure and drive, `TD-20260913-023` through `030` for X/extruder geometry, `TD-20260913-039` and `040` for the installed hotend, and `TD-20260913-160` through `228` for cleaned component identification and measurements.
