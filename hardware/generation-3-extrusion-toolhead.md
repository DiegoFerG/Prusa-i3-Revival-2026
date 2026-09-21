# Generation 3 extrusion and toolhead target

This document records the preferred Generation 3 extrusion concept for the Revival 2026 final build.

The Revival is **not intended to be the user's primary production printer**. Its target use is:

- excellent-quality PLA printing as the normal operating case;
- PETG/TPU support where practical;
- occasional ABS/ASA printing when geometry, ambient conditions and part size make it reasonable;
- no requirement for a heated chamber or engineering-polymers workflow;
- no attempt to compete with enclosed high-temperature machines.

## Preferred extrusion combination

The frozen Generation 3 combination is:

- **E3D Roto** direct-drive extruder;
- **E3D Revo** hotend ecosystem;
- **BIGTREETECH Eddy Duo** eddy-current probe;
- 1.75 mm filament;
- 24 V heater system;
- approximately 300 °C maximum operating class;
- modular toolhead integration around the EBB36 Gen2 CAN node.

This **EBB36 Gen2 + Roto + Revo + Eddy Duo** functional stack is frozen as the Generation 3 toolhead direction. The EBB36 Gen2 has already been purchased. Current purchase preference for the remaining extrusion hardware is **Roto Sensored + Revo 24 V / 40 W**. Exact retail SKU/revision, physical mounts, offsets and final cooling/electrical routing remain engineering details to validate before release.

## Why Roto + Revo

The combination is preferred because the Revival prioritises print quality, maintainability and a compact toolhead over extreme volumetric throughput.

### Roto

Target advantages:

- compact direct-drive layout;
- dual-drive filament grip;
- low moving mass relative to full-size NEMA17 extruder systems;
- good match for a rail-based X axis;
- suitable for a toolhead where EBB36, probe, fans, lighting and future sensors also consume mass/space;
- compatible with the RASS architecture because RASS removes spool inertia and long-path drag from the toolhead extruder.

### Revo

Target advantages:

- simple cold nozzle changes;
- integrated nozzle/heatbreak architecture that reduces leak-prone joints;
- broad nozzle ecosystem;
- conventional and high-flow nozzle options;
- suitable temperature range for PLA/PETG/TPU/ABS/ASA use;
- maintenance-oriented design appropriate for a secondary/project printer.

The Revival does not need the absolute maximum flow available from larger high-flow hotends because bed-slinger dynamics and the original machine envelope are expected to become limiting factors first.

## Material priorities

### Primary material — PLA

PLA is the normal operating target.

The machine should be tuned for:

- dimensional accuracy;
- clean surface finish;
- low ringing/ghosting;
- reliable first layers;
- controlled cooling;
- predictable filament profiles;
- reasonable print speed without sacrificing quality.

Input Shaper, Pressure Advance, permanent accelerometers and calibrated Revival material profiles support this quality-first objective.

### Secondary materials

PETG and TPU should remain practical targets.

RASS must not create excessive feeder pressure or drag that harms flexible-material feeding.

### Occasional ABS / ASA

ABS and ASA are intentionally supported only as **occasional materials**.

Constraints:

- the Revival remains an open-frame printer;
- no heated chamber is part of the frozen Generation 3 architecture;
- large ABS/ASA parts may warp or split;
- draught-sensitive jobs may require temporary environmental control or may simply be unsuitable for this machine;
- no permanent enclosure should be assumed unless separately designed and evaluated later.

The 24 V bed, PEI/spring-steel surface and approximately 300 °C hotend class should provide enough thermal capability for smaller/moderate ABS/ASA work, but chamber-dependent performance is outside the design goal.

## Toolhead architecture

Conceptual stack:

```text
MGN12 X carriage
      |
  toolplate
      |
 +----+-----------------------------+
 |                                  |
Roto direct drive                EBB36 Gen2
 |                                  |
Revo hotend                    CAN / local I/O
 |
nozzle
```

Additional toolhead functions may include:

- hotend heatsink fan with tachometer feedback;
- part-cooling blower;
- optional auxiliary cooling;
- BTT Eddy Duo probe;
- permanent X accelerometer;
- nozzle work/status light;
- future optional nozzle camera.

The toolhead should remain modular: extruder/hotend, probe, cooling and electronics should be replaceable without redesigning the entire X axis.

## Eddy probing and surface scanning

Generation 3 uses a **BIGTREETECH Eddy Duo** as the bed-surface probe/scanner.

Target functions:

- rapid/dense Klipper bed-mesh acquisition using eddy-current scanning;
- non-contact surface mapping over the final spring-steel/magnetic bed stack;
- repeatable cold/hot bed characterisation during commissioning;
- support for the final Z-reference strategy after calibration and nozzle-cleaning integration are validated.

The mount must be mechanically adjustable and serviceable. Eddy Duo is treated as an independent 5 V CAN MCU/node downstream of the EBB36 Gen2 passthrough, not as an I2C peripheral of the EBB36. Final X/Y offset, Z height, thermal compensation/calibration procedure, connector pinout and physical CAN harness remain to be determined during CAD and bench testing.

The Eddy does not replace the requirement for good mechanical bed/rail alignment; software mesh compensation is for residual surface variation.

## Cooling target

### Hotend cooling

Use a 24 V heatsink fan with tachometer feedback if the selected fan and EBB36 configuration permit it.

The goal is to detect loss of hotend cooling rather than relying only on commanded fan state.

### Part cooling

A 24 V blower and custom bilateral duct are the preferred starting direction.

The duct should:

- cool the printed part from more than one direction where practical;
- avoid excessive direct airflow onto the heater block/nozzle;
- remain serviceable;
- preserve probe and camera sight lines;
- avoid unnecessary toolhead mass.

Exact fan model and duct geometry remain open.

## Nozzle strategy

The expected working set is:

- **0.4 mm** as the normal quality nozzle;
- **0.6 mm** as an optional productivity/nozzle-size alternative;
- wear-resistant nozzle option for abrasive materials.

High-flow Revo nozzles may be evaluated, but high-flow capability is not itself a design requirement.

## Temperature sensing

The exact Revo heater/sensor cartridge selection remains open.

A standard supported Revo temperature sensor is acceptable. PT1000 may be considered if it provides a clear integration or service advantage, but the project should not complicate the toolhead solely to change sensor technology.

## Relationship with RASS

RASS supplies filament upstream and removes unnecessary spool load from the moving toolhead.

Control hierarchy:

```text
RASS spool drive / feeder
        |
     buffer
        |
     PTFE
        |
   E3D Roto
  (extrusion master)
        |
      Revo
        |
      nozzle
```

Roto remains responsible for extrusion precision.

RASS must not directly impose nozzle flow or replace Klipper extrusion control.

## Performance philosophy

The Revival target is **quality-first, not benchmark-first**.

Do not optimise the toolhead around headline speed or volumetric-flow numbers if doing so increases:

- moving mass;
- noise;
- maintenance;
- heat;
- complexity;
- loss of classic i3 character.

A well-calibrated PLA print with clean surfaces and predictable repeatability is more important than maximum speed.

## Status

### Preferred / selected direction

- 1.75 mm final extrusion;
- direct drive;
- **E3D Roto + Revo + BTT Eddy Duo as the frozen Generation 3 extrusion/probing stack**;
- PLA quality as primary design target;
- occasional ABS/ASA support without heated-chamber requirement;
- modular toolhead;
- EBB36 Gen2 integration;
- 24 V cooling/heating architecture.

### Still open

- exact Roto/Revo retail SKU/revision at purchase time; current preference is Roto Sensored + Revo 24 V / 40 W;
- exact Eddy Duo mounting, offset, connector pinout, physical CAN harness and calibration strategy;
- exact Revo heater/sensor cartridge;
- exact nozzle set;
- exact fans;
- duct geometry;
- probe mount;
- final EBB36 placement;
- toolplate/carriage CAD;
- exact thermal limits configured in Klipper;
- whether any temporary/open-frame ABS/ASA wind shielding is useful.
