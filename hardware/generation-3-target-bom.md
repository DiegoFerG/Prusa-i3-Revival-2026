# Generation 3 target hardware BOM

This is the target hardware set for the **Revival 2026 final build**. It records architectural selections early so later purchases and CAD decisions remain consistent. It is **not** an instruction to skip the original Arduino/RAMPS or Re-ARM generations.

See [`../docs/final-build-architecture.md`](../docs/final-build-architecture.md) for the full architecture and safety boundaries.

## Frozen selections

| Subsystem | Target component / architecture | Status |
|---|---|---|
| Main controller | BIGTREETECH Manta M8P V2.0 | Frozen |
| Linux host | BIGTREETECH CB2 | Frozen |
| Main stepper drivers | 8× TMC2209 purchased as the Manta/CB2 bundle | Frozen |
| Local display | BIGTREETECH HDMI5, 5-inch capacitive touchscreen | Frozen |
| Display integration | Custom retro/industrial ASA enclosure + KlipperScreen theme | Frozen concept |
| Toolhead MCU | BIGTREETECH EBB36 Gen2 | Frozen |
| Toolhead network | CAN bus | Frozen |
| CAN distribution | BIGTREETECH CEB V1.0 in electronics bay | Frozen |
| Toolhead accelerometer | permanent LIS2DW associated with EBB36 Gen2 | Frozen |
| Bed accelerometer | BIGTREETECH S2DW V1.0 (RP2040 + LIS2DW), permanent | Frozen |
| Bed accelerometer link | USB to CB2 | Frozen |
| Main camera concept | fixed frame-mounted camera, CSI preferred and USB UVC permitted | Frozen architecture, model/interface open |
| Camera styling | custom retro late-1980s/1990s CCTV/video-surveillance enclosure | Frozen concept |
| Main DC voltage | 24 V | Frozen |
| Heated-bed construction | original footprint; aluminium + silicone heater + magnetic base + flexible PEI sheet | Frozen architecture |
| Bed switching | external DC MOSFET controlled by Manta | Frozen architecture |
| Bed protection | dedicated fuse + independent thermal fuse | Frozen architecture |
| Frame lighting | dimmable 24 V diffused white work light | Frozen architecture |
| Toolhead lighting | EBB36-controlled nozzle work/status light | Frozen architecture |
| Hotend cooling | 24 V fan with tachometer feedback preferred | Frozen architecture |
| Electronics cooling | large low-RPM temperature-controlled enclosure fan(s) | Frozen architecture |
| Wiring | completely new harnesses | Frozen |

## Possible future upgrades

| Upgrade | Concept | Status |
|---|---|---|
| Nozzle camera | tiny camera fixed to toolhead/nozzle for nozzle-centred timelapse; likely USB/UVC and therefore requiring a separate moving USB service to the toolhead | Possible future upgrade only |
| Nozzle-camera styling | miniature retro CCTV/video-surveillance enclosure, not an exposed PCB | Frozen aesthetic if upgrade is adopted |

The nozzle camera is deliberately excluded from the base moving-harness design until cable flexibility, bend life, strain relief, toolhead mass, EMI and USB topology can be evaluated on the final head.

## Selections intentionally deferred

These items must fit the frozen architecture but their exact model or rating depends on later measurement/CAD/testing:

- direct-drive extruder and hotend;
- Z probe;
- filament sensor;
- exact bed aluminium thickness;
- exact silicone-heater dimensions and power, after measuring the original heated-bed PCB;
- exact Mean Well 24 V PSU wattage after heater loads are frozen;
- fan makes/models and final duct geometry;
- frame-light strip/diffuser;
- connector families and wire gauges;
- final electronics enclosure and airflow geometry;
- main frame-camera sensor, lens/FOV and final CSI-versus-USB choice;
- optional nozzle-camera hardware/interface if that future upgrade is adopted.

## Bed size rule

Do not order a 220/235/250 mm standard modern bed merely because it is convenient. The Generation 3 bed is to match the **original heated-bed footprint and travel envelope**. The catalogued approximately 220 × 220 mm Y carriage and 200 × 200 mm original mirror surfaces are reference evidence only; the original heated-bed PCB must be measured before releasing the final aluminium/heater CAD.
