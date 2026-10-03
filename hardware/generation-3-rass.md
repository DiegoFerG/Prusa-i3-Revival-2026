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
          Smart-spool reader / weighing service
                 |
                 +------------ host data / context ------------+
                                                                |
CEB V1.0 CAN -------------------------------------------- RASS CAN Node
                                                                |
                                              +-----------------+----------------+
                                              |                 |                |
                                       spool-drive motor    feeder motor    buffer/encoders
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

The **production RASS motion/sensing controller is a custom Klipper-compatible CAN node** designed specifically for the Revival and connected to the Generation 3 CAN backbone through the BIGTREETECH CEB V1.0. It follows the common [custom CAN-node design rules](generation-3-custom-can-node-design-rules.md).

Production-controller requirements:

- MCU supported by upstream Klipper with a validated CAN transport;
- dedicated CAN transceiver and suitable bus protection;
- selectable 120-ohm termination so the board can be correctly placed at a physical bus end if required;
- motor-driver interfaces sized for the spool-drive and feeder motors;
- buffer/dancer sensor inputs;
- feeder encoder/motion inputs;
- filament-presence and optional spool-rotation feedback inputs;
- physical exposure of **every remaining electrically usable MCU pin** under the common custom-node rules after the feeder, spool-drive, RFID reader, buffer, encoder and production sensors are allocated;
- service/status LEDs;
- dedicated **BOOT/BOOTSEL and RESET tactile pushbuttons** where applicable to the selected MCU, following the EBB36-style service model;
- dedicated native debug/programming access (for example SWD header/pads on STM32);
- USB-C service/recovery preferred where the selected MCU supports it cleanly.

Normal production communication is **CAN through the CEB V1.0**. Wi-Fi is not part of the production RASS control path.

The RASS CAN Node may host the **physical RFID/NFC reader interface** and acquire the tag traffic needed by the Smart Spool subsystem, but it must remain **interpretation-free**. Its responsibility is to read and forward low-level tag data/events to the Linux host over the machine data path. It must not decide manufacturer, material, colour, profile, spool identity semantics or vendor format.

All RFID/NFC interpretation belongs to the host service: **CB1 during bench/prototype work and CB2 in the final Generation 3 machine**. The host owns decoder plugins, vendor-format interpretation, Revival Spool Tag parsing, database/inventory logic and profile mapping.

The exact upstream-compatible transport for variable RFID/NFC payloads over the RASS CAN/Klipper link remains an implementation item. Prefer a host-side service/extension and standard upstream Klipper bus/MCU mechanisms. **The production RASS MCU shall run unmodified upstream Klipper firmware.** If a proposed RFID reader or transport would require patched Klipper MCU C code or a private MCU protocol command, change the reader/interface/host architecture instead of embedding that requirement in the production firmware.

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
temporary bench MCU
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

### Local RASS Spool Panel

Generation 3 also includes a **second small touchscreen mounted locally next to the RASS/spool assembly**. This is a dedicated spool-status/control HMI, not a second copy of the full KlipperScreen interface.

The preferred architecture is a **small self-rendering serial HMI** connected by a wired host link (normally USB-to-serial or equivalent) to the Linux host. It does **not** consume the CB2's primary HDMI display path and is not driven by the RASS MCU.

Target information shown locally:

- spool manufacturer/product where known;
- material and colour;
- tag/identification state;
- remaining mass and percentage, plus estimated length where available;
- RASS state;
- filament-present state;
- buffer/dancer state;
- feeder/spool-drive warnings;
- current nozzle temperature and whether filament handling is permitted.

The panel provides touch controls for at least:

- **LOAD / CARGAR FILAMENTO**;
- **UNLOAD / DESCARGAR FILAMENTO**.

These controls are **requests to the Linux host**, never direct motor commands. The display may show a button as enabled only when the host says the action is currently allowed, but the host must independently re-check all interlocks when the touch event arrives.

The load/unload action is permitted only when all applicable conditions are true:

- Klipper is connected and in a normal ready state;
- there is **no active print**, including no paused print that could later resume;
- no homing, probing, calibration or other incompatible motion/action is active;
- required extrusion/RASS MCUs and sensors are online and not reporting a fault;
- the toolhead/extrusion path is stationary and in a known-safe state;
- the hotend is at or above the configured safe extrusion/minimum-extrude temperature and within valid temperature limits;
- RASS buffer/filament state is compatible with the requested direction;
- any additional interlock introduced later by validated RASS hardware also passes.

When a condition is not met, the corresponding button remains disabled and the panel should show a short reason such as **PRINT ACTIVE**, **HOTEND COLD**, **RASS FAULT**, **FILAMENT ALREADY LOADED** or **NO FILAMENT TO UNLOAD**.

The host-side RASS/Spool service owns this gating policy. The HMI firmware/layout is presentation only and must not be treated as a safety boundary.

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
- RASS is controlled by a **custom Klipper-compatible CAN MCU** connected through the CEB V1.0;
- the RASS MCU runs **unmodified upstream Klipper firmware**; Revival-specific semantics and decoding remain on the Linux host;
- CAN is the normal production RASS host link;
- the RASS node acquires RFID/NFC reader data but performs **no tag/vendor/material interpretation**;
- raw/low-level RFID/NFC observations are forwarded to the Linux host for decoding and inventory/profile logic;
- a dedicated **local RASS Spool Panel** touchscreen is mounted beside the spool/RASS assembly for spool information and guarded LOAD/UNLOAD requests;
- the local panel never directly actuates motors; the Linux host owns action gating and re-validates interlocks at execution time;
- passive/manual fallback remains a design requirement;
- after all production functions are allocated, the RASS PCB exposes **every remaining electrically usable MCU pin**, with SPI/I2C/UART/ADC/GPIO/PWM alternate functions documented and any unavailable pins justified;
- exact MCU, CAN transceiver, motors, motor drivers, buffer geometry and spool-drive mechanism remain open until electrical/mechanical prototyping.

## Open component-level decisions

- production RASS MCU/package selection that satisfies the frozen RASS functions while allowing all remaining electrically usable MCU pins to be physically exposed;
- CAN transceiver/protection implementation;
- exact RFID/NFC reader electrical interface on the RASS PCB;
- exact host transport/API for forwarding raw RFID/NFC observations over the CAN/Klipper path without embedding decoder logic in the MCU;
- CAN connector family, physical bus position/stub length and termination-jumper policy;
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
- smart-spool reader/controller board remains a separate decision in the Smart Spool subsystem;
- final interaction with the future toolhead filament-motion sensor;
- calibration procedure for active tension control;
- mechanical filtering required to keep motor activity from corrupting load-cell readings;
- exact RASS Spool Panel model, size, enclosure and wired host interface; a compact serial HMI is the preferred direction.
