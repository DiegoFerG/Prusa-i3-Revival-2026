# Photo catalogue — ARQ archaeology archive

**Primary capture date:** 12 September 2026  
**Current archive total:** 80 photographs  
**Path:** `photos/00-archaeology/originals/`

## Catalogue rules

The `ARQ-YYYYMMDD-NNN` identifier is a legacy permanent photo ID. It is retained as an opaque technical identifier for traceability even though all descriptive paths and filenames are now standardised in English. Technical identifications may change during teardown, but photo IDs do not.

This catalogue is based on the archaeology session sequence and the observations made while inspecting the material. No loose object is attributed to the printer without additional evidence.

## Documentary blocks

| Range | Context | Provenance |
|---|---|---|
| 001–005 | Initial discovery/storage views | PRINTER-AS-FOUND |
| 006–019 | Visual inspection: structure, Y, electronics, Z, extruder and general views | PRINTER-AS-FOUND |
| 020–021 | Additional details: cooling / E3D-family hotend | PRINTER-AS-FOUND |
| 022–027 | Loose material: wiring, consumables and period parts | LOOSE-FOUND |
| 028–034 | Loose components/spares found in boxes | LOOSE-FOUND |
| 035–043 | Raspberry Pi 2, damaged Waveshare display and other period hardware | PERIOD-UNRELATED / LOOSE-FOUND |
| 044 | 2× Alhambra II Open FPGA Board V1.0A | PERIOD-UNRELATED |
| 045–051 | Batch of printed parts donated or purchased at the time | DONATED-PURCHASED |
| 052–056 | RAMPS 1.4sb and Panucatt Devices Re-ARM controller stack | LOOSE-FOUND |
| 057–059 | Heater cartridges, Ethernet interface and assorted heatsinks | LOOSE-FOUND |
| 060–061 | LCD modules, Arduino-class boards, RAMPS-style shield and related electronics | LOOSE-FOUND / PERIOD-UNRELATED |
| 062 | Assorted cooling fans and wiring | LOOSE-FOUND |
| 063–072 | Additional loose electronics, thermal/cooling hardware and documentary views | LOOSE-FOUND |
| 073–080 | Additional archaeology photographs captured before teardown | PENDING DETAILED CLASSIFICATION |

> These ranges are an initial documentary classification. They can be refined photo by photo during review and teardown without changing the permanent IDs.

## Recorded identifications

### Installed on the printer — provisional until teardown

- Classic Prusa i3 / Rework-era / RepRap-derived family.
- Single-sheet metal vertical frame.
- Threaded-rod Y structure.
- Smooth-rod guides.
- Z axis with two NEMA17 motors, flexible couplers and conventional threaded rods.
- Direct Wade/Greg's-Wade-family geared extruder for the Legacy 3 mm stage.
- Hotend remembered as E3D and visually compatible with the E3D family; exact V5/V6 revision and variant pending.
- RepRapDiscount/BigTreeTech 12864 graphic controller.
- Mega/RAMPS-era controller architecture or equivalent; exact revision pending.
- Heated bed with glass and screw/spring levelling.

### Found loose — do not attribute to the printer

Items identified or recorded during the session include:

- Multi-core wiring and four-conductor extensions.
- Aerzetix C14222 red braided sleeve, Ø4 mm / 3–7 mm, according to the visible label.
- Loose heater cartridge; electrical specifications pending measurement.
- Longs Stepper Motor 17HS8401S1, NEMA17, labelled 2.8 A / 4 wires.
- GPLv3 mechanical endstop module; exact model/manufacturer pending.
- Wiring loom physically labelled `MOTOR EJE E0`; the original label is preserved verbatim as evidence.
- Raspberry Pi 2 Model B V1.1, candidate for reuse testing.
- Waveshare 5inch HDMI LCD V2, 800×480, XPT2046, with physically broken display.
- Arduino UNO R3-compatible board and prototyping/perfboard.
- 2× Alhambra II Open FPGA Board V1.0A, period hardware with no confirmed relationship to the printer.
- Batch of old donated/purchased printed parts, pending individual identification.
- Panucatt Devices **Re-ARM**, an ARM controller in Arduino Mega form factor, photographed separately and fitted beneath a **RAMPS 1.4sb** shield. Electrical condition and firmware status remain untested.
- **RAMPS 1.4sb** shield (`staticboards.com` marking visible), photographed from both sides and assembled with the Re-ARM.
- Loose heater cartridges/high-temperature leads, specifications pending.
- Ethernet interface module, exact chipset/model and original use pending.
- Assorted heatsinks, character LCD modules, Arduino-class electronics and cooling fans.

## Pending for teardown

Visual archaeology deliberately leaves questions that can be answered better by measurement:

1. exact i3 variant;
2. exact E3D hotend revision and filament path;
3. controller model/revision;
4. power supply specifications;
5. installed motor references;
6. diameters, lengths and pitches of all rods;
7. bearings, pulleys, belts and guide condition;
8. actual wiring topology;
9. electrical testing of loose components considered for reuse;
10. Re-ARM hardware revision, boot/firmware state and practical compatibility with the revival architecture;
11. RAMPS 1.4sb power-stage condition and suitability for bench testing or reuse.
