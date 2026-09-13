# Initial archaeology inventory

**Date:** 12 September 2026

This document records what can be identified visually before dismantling the printer.

## Provisional identification

Family: **classic Prusa i3 / Rework-era / RepRap derivative**.

The exact variant remains pending until measurements can be taken and compared with historical documentation.

## Observed components

### Structure
- Flat metal vertical frame.
- Y base built from threaded rods, nuts and printed parts.
- Smooth-rod linear guides.

### Z axis
- Two NEMA17 motors.
- Smooth vertical guide rods.
- Conventional threaded rods used for Z motion.
- Flexible aluminium couplers between motors and threaded rods.

**Revival decision:** replace the old threaded Z rods with proper leadscrews selected after the actual geometry is measured and the desired lead is defined.

### Extruder
- Direct geared extruder from the Wade / Greg's Wade family.
- Large printed driven gear and motor pinion.
- Spring-loaded idler system.
- Historical configuration compatible with approximately 3 mm filament.

**Revival Phase 1 decision:** attempt to preserve/rebuild this architecture to consume the Legacy 3 mm filament stock.

### Hotend
- The owner remembers the hotend as an E3D.
- Side photographs show a recognisable E3D-family heatsink.
- Exact V5/V6 generation and exact 3 mm variant remain pending until teardown.

### Electronics
- Arduino Mega / RAMPS-era architecture or equivalent.
- Plug-in stepper drivers with heatsinks.
- RepRapDiscount / BigTreeTech Full Graphic Smart Controller 12864.
- Open-frame metal power supply with exposed terminals.

**Revival decision:** document the original electronics, but redesign control, power distribution, wiring, enclosures and safety to current standards.

### Loose controller hardware discovered during archaeology batch 02
- Panucatt Devices **Re-ARM** ARM controller in Arduino Mega-compatible form factor.
- **RAMPS 1.4sb** shield photographed separately and installed on the Re-ARM.
- These boards are loose recovered hardware; they are **not yet attributed to the printer's original configuration**.
- Power-up, firmware identification and electrical checks remain pending.

### Bed
- Heated bed with a glass print surface.
- Four-point screw-and-spring levelling arrangement.

### X/Y transmission
- Old toothed belts.
- Pulleys and tensioning system to be inspected.

## Data required during teardown

1. Diameter and length of X/Y/Z smooth rods.
2. Diameter and pitch of the current Z threaded rods.
3. Diameter of structural Y rods.
4. Frame dimensions.
5. Full labels of all installed NEMA17 motors.
6. Straight-on high-resolution photograph of the controller board.
7. Power supply label and specifications.
8. Exact E3D hotend identification.
9. Full inventory of loose parts and motors found in boxes.
10. Condition of linear bearings, pulleys, belts, guides and bed.

## Safety rule

Do not power the old electronics until the power supply, mains wiring, bed, connectors, insulation and protection arrangements have been inspected.
