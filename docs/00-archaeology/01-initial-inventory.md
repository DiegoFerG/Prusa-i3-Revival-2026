# Initial archaeology inventory

**Original observation date:** 12 September 2026  
**Stage status:** historical Stage 00 baseline; superseded for technical identification by the completed Stage 01 teardown/inventory.

This document records what could be identified visually **before dismantling** the printer. It intentionally preserves the uncertainty that existed at the time. Confirmed teardown findings are recorded separately below rather than rewriting the original observations as if they had been known in advance.

## Original provisional identification

Family: **classic Prusa i3 / Rework-era / RepRap derivative**.

The exact variant was not established during non-invasive archaeology and remains intentionally unclaimed where the evidence does not justify a narrower historical designation.

## What the as-found inspection showed

### Structure
- Flat single-sheet metal vertical frame.
- Y base built from threaded rods, nuts and printed parts.
- Smooth-rod linear guides.

### Z axis
- Two NEMA17 motors.
- Smooth vertical guide rods.
- Conventional threaded rods used for Z motion.
- Flexible aluminium couplers between motors and threaded rods.

### Extruder and hotend
- Direct geared extruder from the Wade / Greg's Wade family.
- Large printed driven gear and motor pinion.
- Spring-loaded idler system.
- Historical configuration for the legacy approximately 3 mm filament system.
- E3D-family hotend visible, exact generation unresolved at Stage 00.

### Electronics
- Mega/RAMPS-era controller architecture.
- Plug-in stepper drivers with heatsinks.
- RepRapDiscount-style full graphic controller.
- Open-frame metal power supply.

### Bed and motion
- Heated bed with removable glass/mirror print surface.
- Four-point screw-and-spring levelling arrangement.
- Toothed-belt X/Y transmission.

## Stage 01 resolution — 13 September 2026

The controlled teardown, cleaning and component inventory resolved most of the Stage 00 questions:

| Subject | Current documented result |
|---|---|
| Controller | **Arduino Mega 2560** |
| Main shield | **StaticBoards RAMPS 1.4SB** |
| Stepper drivers | **4× A4988-family plug-in modules**; exact clone/revision not claimed |
| Installed motors | **5× Wantai 42BYGHW811 NEMA17**, labelled 2.5 A and 1.8°/step |
| Main PSU | **JCPOWER JC-360-12**, 110/220 VAC input, 12 V / 30 A output |
| LCD / storage | RepRapDiscount-style graphic controller + RAMPS smart adapter + Panasonic 16 GB SDHC |
| Y carriage | approximately **220 × 220 mm**, approximately **210 mm hole spacing** in both axes, **6 mm** thick, M3 threaded mounting holes |
| Structural threaded rods | **2× M10 × 350 mm** and **4× M8 × 200 mm** |
| Original Z threaded rods | **2× M5 × 310 mm** |
| Smooth rods | **2× Ø8 × 350 mm**, **2× Ø8 × 330 mm**, **2× Ø8 × 317 mm** |
| Linear bearings | **10× LM8UU-family** |
| Radial bearings | **3× FAG 608Z**, standard 8 × 22 × 7 mm family |
| Belt transmission | **T2.5**, with approximately **20-tooth** aluminium drive pulleys; one documented open belt is approximately 800 mm long |
| Build surfaces | **4× IKEA SÖRLI mirrors**, 200 × 200 × 3 mm |
| Bed levelling | Screw-and-spring system; the improvised clothes-peg springs are preserved and documented |
| Hotend | Legacy **E3D-family**, probably V5-era, for the 3 mm / 2.85 mm stage; exact revision still unconfirmed |
| Hotend sensor | Legacy bead thermistor; likely 100 kΩ class, but exact type remains pending electrical measurement |
| Heater cartridge | Still installed in the heater block; retaining screw head is stripped, so removal was deliberately deferred |
| Wiring | Original mixed wiring harness documented but **not selected for reuse**; the revival will be rewired from scratch |

The original heated-bed PCB, geared extruder and mechanical endstop modules are also documented in the Stage 01 original photo archive.

## Remaining uncertainties

Teardown completion does not justify pretending every exact part number is known. The following remain deliberately open until measurement or bench testing provides evidence:

- exact historical Prusa i3 sub-variant;
- exact E3D hotend generation/revision;
- exact thermistor curve/type;
- exact manufacturer/revision of each A4988-family driver module;
- electrical and mechanical condition of components not yet bench-tested.

## Evidence

Stage 00 evidence remains under `photos/00-archaeology/`.  
Stage 01 teardown and inventory evidence is under `photos/02-teardown/` and currently reaches `TD-20260913-228`.

## Safety rule

Do not power the old electronics until the PSU, mains wiring, heated bed, connectors, insulation and protection arrangements have been inspected. Mechanical reassembly comes before electrical commissioning.
