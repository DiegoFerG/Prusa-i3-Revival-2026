# Blog source notes — Chapter 0

This file is the evidence-backed source notebook for the bilingual archaeology article. The public blog is maintained continuously as the project advances rather than written only after the build is finished.

## Working title

**Chapter 0 — Basement Archaeology**

The public blog will maintain equivalent Spanish and English editions, while repository documentation remains in English.

## Core idea

A self-built Prusa i3 from more than a decade ago reappears in storage alongside boxes of parts, motors, electronics and other hardware from the same period. Instead of powering it or immediately replacing components, the project begins by documenting the technological ecosystem around it.

## Opening scene

The first photographs were taken while the printer was still in storage. They are not product photographs; they document the genuine zero point of the project. The printer was then observed more closely and the visual inventory began, still without dismantling it.

## What Stage 00 could see

- recognisable Prusa i3 / RepRap-era architecture;
- flat single-sheet metal frame;
- threaded-rod Y structure;
- conventional threaded Z drive with flexible couplers;
- Wade/Greg's-Wade-family geared extruder;
- E3D-family hotend;
- Mega/RAMPS-era electronics and graphic display;
- heated bed and removable glass/mirror build surface;
- hand-built wiring typical of a machine assembled and modified by its owner.

## The boxes tell a different story

The search also uncovered motors, endstops, wiring, heaters, printed parts, a Raspberry Pi 2, a broken Waveshare display, Alhambra II FPGA boards, a Panucatt Re-ARM and other technological remnants.

An important editorial rule emerged: **being in the same box does not mean an item was part of the printer**. Installed components remain separate from spares, experiments and unrelated period hardware.

## The nostalgia details worth preserving

The project is not only about electronics and dimensions. Some of the most characteristic evidence is mundane: IKEA SÖRLI mirrors used as 200 × 200 mm build surfaces, and springs taken from clothes pegs for the bed-levelling system. These improvised solutions are part of the practical RepRap culture in which the machine was built and deserve to appear in the story rather than being silently replaced by modern parts.

## Stage 01 changed the story from guesswork to evidence

The teardown and cleaned inventory completed on 13 September 2026 confirmed the installed Arduino Mega 2560 / StaticBoards RAMPS 1.4SB stack, five Wantai 42BYGHW811 motors, the JCPOWER JC-360-12 12 V / 30 A PSU, T2.5 transmission, principal rod dimensions, LM8UU-family and FAG 608Z bearings, the original build surfaces and the legacy E3D-family hotend.

The Stage 01 photo sequence now reaches `TD-20260913-228`.

Some identifications remain deliberately incomplete. The hotend is probably V5-era but the exact revision is not proven; the thermistor still needs electrical identification; and the A4988-family driver clone/revision is not treated as known without legible evidence.

## This is not a museum restoration

The machine will be rebuilt and then modernized in controlled generations. Historical value does not automatically mean reuse, particularly for safety-critical electrical hardware.

The next narrative chapter begins with **reassembly of the original mechanical geometry**. That step is important because it lets the project understand the machine before redesigning it.

Later modernization will address, among other things:

- proper Z leadscrews;
- printed parts, primarily ASA;
- electronics and firmware;
- power distribution and electrical safety;
- complete new wiring and connectors;
- enclosures;
- eventual 1.75 mm extrusion.

The legacy 3 mm / 2.85 mm stage remains important so the recovered filament stock can be evaluated and, where practical, used.

## Visual material

The frozen archaeology archive contains **80 original ARQ photographs**. Stage 01 adds **159 teardown originals** plus **69 cleaned component-inventory derivatives**, for a `TD-` sequence that currently runs through `228`.

Originals must never be overwritten by publication derivatives.

## Publication rules

- Spanish and English editions are equivalent editorial versions, not blind real-time machine translation.
- Use the same photo IDs and technical references in both languages.
- Clearly separate personal recollection from verified technical identification.
- Explicitly mark unresolved identifications.
- Link each article to the repository/commit containing the underlying evidence and technical files when useful.
- Update the technical repository before promoting a new technical conclusion into the blog.
