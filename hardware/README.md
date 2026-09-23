# Hardware baseline

This directory is the home for mechanical/electrical documentation, schematics and future bills of materials for **Prusa i3 Revival 2026**.

The Stage 01 teardown and physical inventory was completed on **13 September 2026**. The table below records the current original-hardware baseline before reassembly and modernization.

## Mechanical inventory

| Item | Quantity / measurement | Current identification / status |
|---|---|---|
| Main vertical frame | 1 | Single-sheet steel frame from a classic Prusa i3 / Rework-era / RepRap-derived machine; detailed measurement photos exist in `TD-160…170` |
| Y bed carriage/support | 1 | approximately 220 × 220 mm; approximately 210 mm hole spacing horizontally and vertically; approximately 6 mm thick; M3 threaded mounting holes |
| Structural threaded rods | 2 | M10 × 350 mm |
| Structural threaded rods | 4 | M8 × 200 mm |
| Z threaded rods | 2 | M5 × 310 mm; original conventional threaded-rod drive |
| Smooth rods | 2 | Ø8 × 350 mm; probable Y pair |
| Smooth rods | 2 | Ø8 × 330 mm; probable Z pair |
| Smooth rods | 2 | Ø8 × 317 mm; probable X pair |
| Linear bearings | 10 | LM8UU-family, approximately 8 mm bore × 15 mm OD × 24 mm long |
| Radial bearings | 3 | FAG 608Z, 8 × 22 × 7 mm family |
| Z flexible couplers | 2 | Aluminium helical couplers; bore dimensions still to be confirmed before reuse |
| Drive pulleys | 2 | Aluminium T2.5-compatible, approximately 20 teeth and approximately 15 mm outside diameter |
| Open timing belt | 1 documented loose belt | approximately 800 mm, T2.5 trapezoidal profile |
| Bed/build surfaces | 4 | IKEA SÖRLI mirrors, 200 × 200 × 3 mm; one original label preserved |
| Bed levelling hardware | mixed | Long screws, washers and springs; the characteristic springs were repurposed from clothes pegs |
| Fasteners | mixed lots | Screws, nuts, washers and spacers intentionally not individually counted |

## Motors

**5× Wantai 42BYGHW811 NEMA17** motors were recovered from the printer and catalogued as the same model.

Visible label data:

- 1.8° per step;
- 2.5 A current marking.

Electrical condition, winding resistance and bearing condition still need controlled testing before any reuse decision.

## Original electronics

| Item | Quantity | Identification / status |
|---|---:|---|
| Main controller | 1 | Arduino Mega 2560 |
| Motion/power shield | 1 | StaticBoards RAMPS 1.4SB |
| Stepper modules | 4 | A4988-family plug-in drivers; exact clone/revision not fully proven |
| Graphic controller | 1 | RepRapDiscount-style full graphic smart controller |
| LCD adapter | 1 | RAMPS smart adapter, EXP1/EXP2 style |
| SD card | 1 | Panasonic SDHC, 16 GB; contents not yet treated as trusted/project documentation |
| PSU | 1 | JCPOWER JC-360-12, 110/220 VAC ±15% input, 12 V / 30 A output, open-frame fan-cooled unit |
| Endstops | several original modules | Mechanical switch modules documented in teardown photos `TD-147…154`; individual electrical testing pending |

The old mixed wiring harness was photographed and archived but **will not be reused**. Stage 05 will design and build new wiring from scratch.

## Extrusion system

### Geared extruder

The original carriage uses a direct geared extruder from the **Wade / Greg's Wade family**, compatible with the machine's legacy 3 mm / 2.85 mm filament stage.

### Hotend

Current identification: **legacy E3D-family, probable V5-era**, groove-mount style, for the original large-diameter filament system.

Documented parts include:

- aluminium heatsink;
- threaded heatbreak / hot-side connection;
- heater block;
- installed heater cartridge;
- separate bead thermistor and wiring.

The exact E3D revision is intentionally not claimed yet. The heater cartridge is currently captive because the retaining screw head in the heater block is stripped. It was deliberately left in place rather than damaging the block during inventory.

The thermistor is probably a common 100 kΩ NTC type for the period, but this remains **unconfirmed** until its room-temperature resistance and response are measured.

## Heated bed

The original heated-bed PCB is documented in the Stage 01 original teardown archive, including close-ups around `TD-138…141`. Electrical resistance, flatness, insulation and wiring condition must be checked before power testing.

## Reassembly policy

Stage 02 will first reconstruct the original mechanical machine using the evidence in `photos/02-teardown/`.

During reassembly each component should be classified as needed:

- **REUSE** — acceptable as-is after inspection;
- **RESTORE** — clean/lubricate/repair, then reassess;
- **REPLACE** — functionally equivalent replacement required;
- **REDESIGN** — intentionally changed for the Revival;
- **ARCHIVE** — retained primarily as historical evidence.

Modernization ideas should be recorded during Stage 02, but the original geometry should be understood before it is altered.

## Electrical safety

No mains-powered component is cleared for use merely because it looks intact. The JCPOWER PSU, heated bed, RAMPS power stage, connectors and all mains-side arrangements require separate electrical/safety inspection before commissioning.

## Generation 3 vendor reference documentation

Official BIGTREETECH manuals, pinouts, schematics, connection diagrams, reference Klipper configurations and self-contained wiki snapshots for the purchased Manta M8P V2.0, EBB36 Gen2 / USB adapter and TMC2209 V1.3 are preserved in the [BIGTREETECH vendor reference archive](reference/bigtreetech/README.md).

These are pinned third-party references. They do not change any component from purchased to tested or commissioned.
