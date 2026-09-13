# Blog source notes — Chapter 0

This file is the evidence-backed source notebook for the bilingual archaeology article. The public blog is maintained continuously as the project advances rather than written only after the build is finished. Facts can be promoted from these notes into the article as soon as they are sufficiently verified.

## Working title

**Chapter 0 — Basement Archaeology**

The public blog will maintain equivalent Spanish and English editions, but repository documentation remains in English.

## Core idea

A self-built Prusa i3 from more than a decade ago reappears in storage alongside boxes of parts, motors, electronics and other hardware from the same period. Instead of powering it or immediately replacing components, the project begins by documenting the technological ecosystem around it.

## Opening scene

The first photographs are not product photographs. They were taken by stretching an arm into the storage space where the printer had been sitting for years. That is precisely what makes them valuable: they show the genuine zero point of the project.

The printer was later observed more closely and the visual inventory began, still without dismantling it.

## What we found on the printer

- recognisable Prusa i3 / RepRap-era architecture;
- flat metal frame;
- threaded-rod Y structure;
- Z axis with conventional threaded rods and flexible couplers;
- Wade/Greg's-Wade-family geared extruder;
- E3D-family hotend, exact model still to be confirmed;
- Mega/RAMPS-era electronics and display;
- heated bed and glass;
- hand-built wiring typical of a machine assembled and modified by its owner.

## The boxes tell a different story

The search also uncovered motors, endstops, wiring, heaters, printed parts, a Raspberry Pi 2, a broken Waveshare display, Alhambra II FPGA boards and other technological remnants.

An important editorial rule emerged: **being in the same box does not mean an item was part of the printer**. Installed components remain separate from spares, experiments and unrelated period hardware.

## The broken display and the Raspberry Pi

The Waveshare display has obvious physical damage. The Raspberry Pi 2 Model B V1.1, however, remains a candidate for testing. This illustrates the Revival philosophy: do not reuse something merely for nostalgia, but do not replace hardware that can still perform a useful role without first evaluating it.

## This is not a museum restoration

The machine will be completely dismantled and rebuilt from the ground up. Components with mechanical or historical value may remain, while the following areas will be modernised in particular:

- Z axis with proper leadscrews;
- printed parts, primarily ASA;
- electronics;
- power distribution and safety;
- wiring and connectors;
- enclosures;
- firmware and control.

The restoration deliberately has three operational generations: first revive the installed Mega/RAMPS-era machine with legacy 3 mm / 2.85 mm extrusion; then document the recovered Re-ARM as a transitional 32-bit upgrade; finally build the Revival 2026 configuration with 1.75 mm extrusion and current autonomous networked electronics.

## Transition to the next chapter

Before deciding what to buy, we need to know exactly what we have.

## Visual material

The archaeology archive currently contains 80 original photographs. Web-optimised and annotated derivatives will be generated for publication; originals will never be modified.

## Rules for the future bilingual publication

- Spanish and English editions will be equivalent editorial versions, not real-time machine translation.
- Use the same photo IDs and technical references in both languages.
- Clearly separate personal recollection from verified technical identification.
- Explicitly mark unresolved identifications.
- Link each article to the repository/commit containing the underlying evidence and technical files.

## Publication cadence

Do not wait for the end of the project to write the story. At each milestone:

1. update the technical repository first;
2. select the evidence/photos that explain what changed;
3. update the Spanish article;
4. maintain the equivalent English edition;
5. record unresolved questions explicitly rather than filling narrative gaps with assumptions;
6. link the article to the relevant repository state/commit when useful.

The archaeology article can therefore be created now and refined only when later teardown evidence resolves an identification that was explicitly left pending.
