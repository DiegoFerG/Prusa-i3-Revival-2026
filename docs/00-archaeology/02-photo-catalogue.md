# Photo catalogue — ARQ archaeology archive

**Primary capture date:** 12 September 2026  
**Current archive total:** 80 photographs  
**Path:** `photos/00-archaeology/originals/`  
**Status:** frozen Stage 00 evidence set

## Catalogue rules

The `ARQ-YYYYMMDD-NNN` identifier is a legacy permanent photo ID. It is retained as an opaque technical identifier for traceability even though all descriptive paths and new filenames are standardised in English. Later teardown findings may refine an identification, but the Stage 00 photo IDs never change.

A loose object is never attributed to the printer solely because it was found in the same storage area.

## Documentary blocks

| Range | Context | Provenance |
|---|---|---|
| 001–005 | Initial discovery/storage views | PRINTER-AS-FOUND |
| 006–019 | Visual inspection: structure, Y, electronics, Z, extruder and general views | PRINTER-AS-FOUND |
| 020–021 | Cooling / E3D-family hotend details | PRINTER-AS-FOUND |
| 022–027 | Loose material: wiring, consumables and period parts | LOOSE-FOUND |
| 028–034 | Loose components/spares found in boxes | LOOSE-FOUND |
| 035–043 | Raspberry Pi 2, damaged Waveshare display and other period hardware | PERIOD-UNRELATED / LOOSE-FOUND |
| 044 | 2× Alhambra II Open FPGA Board V1.0A | PERIOD-UNRELATED |
| 045–051 | Batch of printed parts donated or purchased at the time | DONATED-PURCHASED |
| 052–056 | RAMPS 1.4SB and Panucatt Devices Re-ARM controller material | LOOSE-FOUND |
| 057–059 | Heater cartridges, Ethernet interface and assorted heatsinks | LOOSE-FOUND |
| 060–061 | LCD modules, Arduino-class boards, RAMPS-style hardware and related electronics | LOOSE-FOUND / PERIOD-UNRELATED |
| 062 | Assorted cooling fans and wiring | LOOSE-FOUND |
| 063–072 | Additional loose electronics, thermal/cooling hardware and documentary views | LOOSE-FOUND |
| 073–080 | Additional archaeology photographs preserved in the frozen archive | Stage 00 evidence; no new provenance should be inferred retrospectively |

The detailed per-photo table currently covers ARQ 001–072 in [05-detailed-photo-inventory.md](05-detailed-photo-inventory.md). ARQ 073–080 remain preserved without invented per-image descriptions; later technical conclusions are documented in Stage 01 rather than retroactively guessed into the archaeology record.

## Stage 00 observations

The as-found printer showed:

- classic Prusa i3 / Rework-era / RepRap-derived architecture;
- single-sheet metal vertical frame;
- threaded-rod Y structure;
- smooth-rod guides;
- dual-Z arrangement with flexible couplers and conventional threaded rods;
- Wade/Greg's-Wade-family geared direct extruder;
- E3D-family hotend;
- Mega/RAMPS-era electronics with a 12864-style graphic controller;
- heated bed and removable glass/mirror surface.

Loose archaeology material also included the Panucatt Devices Re-ARM, another RAMPS 1.4SB, heater cartridges, Raspberry Pi 2, broken Waveshare display, FPGA boards, fans, heatsinks and other period hardware. These remain separate from the proven installed configuration.

## Resolution provided by Stage 01

The teardown/inventory completed on 13 September 2026 established the installed controller as an **Arduino Mega 2560 with StaticBoards RAMPS 1.4SB**, identified the five installed motors as **Wantai 42BYGHW811**, identified the main PSU as **JCPOWER JC-360-12 (12 V / 30 A)**, measured the principal rods and Y carriage, documented the T2.5 transmission and catalogued the hotend, bearings, build surfaces and bed hardware.

The Stage 01 photo archive now reaches `TD-20260913-228`. See [the teardown archive](../../photos/02-teardown/README.md) and [hardware baseline](../../hardware/README.md) for the current technical state.

## Still deliberately unresolved

- exact historical Prusa i3 sub-variant;
- exact E3D hotend revision;
- exact thermistor type/curve;
- exact clone/revision of the A4988-family driver modules;
- bench-tested functional condition of old electrical hardware.

These are open engineering questions, not missing archaeology records.
