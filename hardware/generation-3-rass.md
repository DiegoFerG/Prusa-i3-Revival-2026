# RASS — Revival Active Spool System

This document defines the **RASS (Revival Active Spool System)** architecture for the Generation 3 build.

RASS extends the Generation 3 smart-spool subsystem with **active filament delivery and spool rotation assistance** for a single loaded spool. It deliberately does **not** implement automatic material switching, multi-spool selection or an AMS-style hub.

## Purpose

The target behaviour is:

- identify the loaded spool;
- measure remaining filament mass;
- actively assist spool rotation;
- actively feed filament from close to the spool;
- maintain low, controlled tension in the filament path;
- avoid making the toolhead direct-drive extruder pull against spool inertia;
- detect feed anomalies using multiple independent signals;
- keep the complete system usable with one spool and one filament path.

The toolhead extruder remains the **master extrusion actuator**. RASS only manages upstream supply.

## Functional architecture

```text
                         SPOOL
                           |
                 +---------+---------+
                 |                   |
            RFID/NFC reader       load cell
                 |                   |
                 +---------+---------+
                           |
                    RASS controller
                    (ESP32-S3 class)
                           |
          +----------------+----------------+
          |                |                |
   spool-drive motor   feeder motor     buffer/dancer
          |                |                |
          |                +--------+-------+
          |                         |
          +-------------------------+
                                    |
                               PTFE path
                                    |
                             toolhead extruder
                                    |
                                  nozzle
```

## Single-spool rule

RASS is intentionally a **single-spool active feeder**.

It does not require:

- filament selector;
- cutter for material change;
- multi-spool hub;
- automatic spool switching;
- purge tower logic for colour changes.

This keeps the mechanism mechanically simpler and allows the design effort to focus on smooth, measurable and reliable filament delivery.

## Spool drive

The spool holder uses an assisted-drive mechanism so that the toolhead extruder does not need to accelerate the full spool mass through filament tension.

Preferred concept:

```text
          SPOOL
       +---------+
       |         |
       +---------+
        O       O
        |       |
        |       +-- passive support roller
        |
        +---------- driven roller
```

The exact implementation remains open and may use:

- geared DC motor;
- compact stepper;
- compliant friction roller;
- driven axle/adapter if later testing shows it is more universal.

The spool drive must provide **assistance**, not rigid speed enforcement.

Its control objective is to keep the spool rotating freely with slight positive control while avoiding overfeeding or pulling filament backwards unexpectedly.

## Active feeder near the spool

A compact dual-drive feeder is mounted close to the spool.

Its role is to push filament into the downstream PTFE path so the toolhead direct-drive extruder does not have to overcome:

- spool inertia;
- spool bearing/roller friction;
- heavy full-spool acceleration;
- poor cardboard-spool rolling;
- long-path drag.

The upstream feeder must never replace the toolhead extruder as the source of extrusion precision.

The toolhead extruder still owns:

- commanded extrusion distance;
- pressure advance;
- retraction;
- flow calibration;
- volumetric-flow control.

## Buffer / dancer mechanism

A mechanical or sensorised buffer is required between the active feeder and the toolhead extruder.

Purpose:

- decouple the upstream feeder from instantaneous extrusion motion;
- prevent two motors from fighting each other;
- absorb short acceleration/retraction differences;
- provide an independent tension/position signal.

Conceptual state logic:

```text
buffer pulled/tensioned
        -> feeder speeds up

buffer centred
        -> feeder tracks nominal supply

buffer relaxed/overfilled
        -> feeder slows or stops

reverse/retract condition
        -> feeder may reverse gently if required
```

The exact buffer implementation is intentionally open. Candidate mechanisms include:

- spring-loaded dancer arm;
- linear floating guide;
- short compliant filament loop with optical/Hall sensing;
- multi-position sensor rather than simple binary detection.

## Toolhead relationship

The toolhead direct-drive extruder remains the master.

RASS must therefore operate as a **follower supply system** rather than as a second synchronous extruder.

Preferred control hierarchy:

```text
Klipper extrusion command
        |
        v
toolhead direct drive
        |
        v
buffer position/tension changes
        |
        v
RASS feeder adjusts upstream delivery
        |
        v
spool-drive motor assists rotation
```

Nozzle-side extrusion calibration must remain independent of small RASS control errors.

## Integration with Smart Spool System

RASS reuses the Generation 3 smart-spool hardware and data model.

Shared functions include:

- RFID/NFC identification;
- vendor decoder registry;
- adaptive unknown-tag learning;
- brand/material database;
- spool tare data;
- load-cell weighing;
- remaining filament calculation;
- local spool inventory;
- UI integration.

RASS adds:

- driven spool support;
- feeder motor;
- feeder motion sensing;
- buffer/dancer sensing;
- active tension management;
- additional feed-fault diagnostics.

## Weighing architecture

The weighing system remains authoritative for stable remaining-filament measurements.

All parts that mechanically carry the spool must be included in the calibrated load path.

Preferred arrangement:

```text
       spool
         |
  driven/passive rollers
         |
  RASS spool platform
  - motor
  - reader
  - rollers
         |
      load cell
         |
       frame
```

The tare model therefore includes the RASS holder assembly separately from the empty-spool tare.

The design must avoid mechanical bypasses that transfer spool weight directly to the frame.

## Sensors and diagnostics

RASS should expose enough independent signals to distinguish different failure modes.

Target signals:

- RFID/NFC spool identity;
- stable spool mass;
- feeder motor command;
- feeder motion/encoder feedback;
- buffer/dancer position;
- spool-drive command;
- optional spool rotation feedback;
- filament-present sensor;
- toolhead filament-motion sensor if that Generation 3 candidate is adopted;
- commanded toolhead extrusion.

Example diagnostic cases:

```text
toolhead commands extrusion
+ buffer becomes increasingly tensioned
+ feeder does not advance
=> probable feeder fault or upstream jam

feeder motor turns
+ feeder encoder reports no filament motion
=> feeder slip / filament grinding

feeder advances
+ buffer remains tensioned
=> spool blocked or spool-drive assistance insufficient

spool-drive turns
+ expected rotation feedback absent
=> spool/roller slip

calculated consumption changes
+ stable scale mass does not reconcile later
=> weighing/tare/inventory anomaly
```

These diagnoses are advisory until validated experimentally.

## Controller and host link

Preferred RASS controller:

- ESP32-S3-class MCU;
- local RFID/NFC interface;
- HX711-class or better load-cell ADC;
- motor drivers sized for spool-drive and feeder motors;
- buffer/dancer sensor inputs;
- encoder inputs;
- service/status LEDs;
- USB device connection to the CB2.

USB remains the preferred normal host link.

Wi-Fi may be used for setup, diagnostics or OTA, but normal operation must not require cloud access.

RASS is not assigned to CAN by default. CAN may be reconsidered only if later wiring/topology analysis demonstrates a clear benefit.

## Motor selection philosophy

Exact motors are not frozen.

### Feeder motor

Requirements:

- controllable low-speed torque;
- smooth reversal;
- compact size;
- low heat;
- sufficient force for PTFE-path assistance without crushing filament.

A compact stepper is currently the most likely direction because it gives measurable feed motion and deterministic low-speed control.

### Spool-drive motor

Requirements:

- low speed;
- compliant/forgiving torque delivery;
- low noise;
- safe stall behaviour;
- minimal disturbance to load-cell readings.

A geared DC motor or compact stepper are both candidates.

#### Prototype candidate already on hand — 28BYJ-48 5 V + ULN2003

A **28BYJ-48 5 V geared stepper** with its common **ULN2003 driver board** is available from existing parts and is now the preferred **prototype candidate for spool-rotation assistance**.

Why it is worth testing:

- integrated reduction gives useful low-speed torque;
- naturally suited to slow spool rotation;
- direction can be reversed under MCU control;
- the ULN2003 board is already available for early bench tests;
- its cost to prototype is effectively zero because the parts are already on hand.

Intended use:

```text
ESP32-S3
   |
IN1..IN4
   |
ULN2003
   |
28BYJ-48 5 V
   |
driven spool roller / spool assist
```

This motor is **not a feeder candidate**. The gearbox backlash and modest dynamics make it unsuitable for the filament-feeder function that must respond accurately to buffer demand. The upstream filament feeder still targets a compact stepper, likely NEMA14-class or equivalent, with a dual-drive filament mechanism.

The 28BYJ-48 remains a **prototype candidate**, not frozen production hardware. It must be validated with a full 1 kg spool, the real roller geometry and the final load-cell arrangement. Acceptance criteria include sufficient torque, acceptable noise, controlled reversing, no harmful vibration into the weighing system and graceful freewheel/disengagement behaviour if RASS is disabled.

## Filament compatibility

RASS must be designed to work with:

- PLA;
- PETG;
- ASA;
- ABS where used;
- TPU/flexible materials.

The feeder path must minimise drag and avoid excessive pinch force.

TPU compatibility is a design constraint, not an optional afterthought.

## Failure and fallback behaviour

RASS must fail gracefully.

If RASS is unavailable, the printer should still be capable of manual/passive spool operation where mechanically possible.

Examples:

- RFID failure -> allow manual spool/profile selection;
- scale failure -> use software consumption estimate and manual inventory;
- spool-drive failure -> disengage or freewheel;
- feeder failure -> disable active feed and allow passive/manual path if safe;
- buffer sensor failure -> disable active-follow mode rather than guessing.

RASS failure must not force unsafe extrusion behaviour.

## User experience

Target normal workflow:

```text
install spool
   |
tag identified
   |
stable mass measured
   |
remaining filament shown
   |
RASS feeder/path self-check
   |
load filament
   |
active tension control enabled
   |
print
```

During printing, the HDMI5/Mainsail interface may expose:

- spool identity;
- remaining mass;
- RASS state;
- buffer position;
- feeder status;
- spool-drive status;
- warnings/faults.

Normal printing should not require the user to manually tune feeder speed.

## Frozen architectural decisions

- the name is **RASS — Revival Active Spool System**;
- RASS is a single-spool system;
- RASS extends the Generation 3 Smart Spool System;
- spool identification and automatic weighing remain integrated;
- the spool receives active rotation assistance;
- a dedicated feeder near the spool actively supplies filament into the PTFE path;
- the toolhead direct-drive extruder remains the master extrusion actuator;
- an intermediate buffer/dancer decouples the upstream feeder from toolhead extrusion;
- RASS uses sensor feedback rather than fixed feeder/spool speeds;
- the complete spool-support mechanism remains inside the calibrated load-cell path;
- RASS diagnostics compare multiple signals to detect feed anomalies;
- RASS is controlled by a local MCU, with wired USB to CB2 preferred;
- RASS is not assigned to CAN by default;
- passive/manual fallback remains a design requirement;
- exact motors, motor drivers, buffer geometry and spool-drive mechanism remain open until mechanical prototyping.

## Open component-level decisions

- feeder motor type/model;
- spool-drive production motor type/model; **28BYJ-48 5 V + ULN2003 is the preferred prototype candidate**;
- motor-driver topology;
- dual-drive feeder geometry;
- feeder encoder/motion sensor;
- buffer/dancer mechanical design;
- buffer position sensor technology;
- spool-rotation sensor/encoder if required;
- PTFE path length and routing;
- drive-roller material and diameter;
- freewheel/disengagement mechanism;
- exact ESP32-S3 board or custom PCB;
- final interaction with the future toolhead filament-motion sensor;
- calibration procedure for active tension control;
- mechanical filtering required to keep motor activity from corrupting load-cell readings.
