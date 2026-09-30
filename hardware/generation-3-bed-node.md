# Generation 3 Revival Bed Node

This document defines the planned **Revival Bed Node**, a custom USB-connected Klipper MCU mounted on or near the moving Y/bed assembly.

The design follows the same distributed-control philosophy used by the EBB36 Gen2 on the toolhead, but it is intentionally optimized for the heated bed rather than reusing a toolhead board with unused functions.

## Architectural decision

The final Generation 3 bed architecture is split into two implementation stages.

### Stage A — conventional wiring first

The printer may be commissioned before the custom Bed Node PCB exists.

Initial bed wiring remains conventional:

- bed heater power switched by an external MOSFET controlled from the main electronics;
- bed thermistor wired back to the Manta;
- permanent bed accelerometer provided by the existing/selected USB S2DW-class solution;
- dedicated bed branch fuse;
- independent thermal fuse physically attached to the bed/heater assembly.

This stage is deliberately valid and supported. The Bed Node must **not** block Generation 3 commissioning.

### Stage B — custom Revival Bed Node

After the custom PCB is designed, assembled and validated, bed-local functions migrate to a dedicated MCU connected to the CB2 over USB.

Target moving services:

```text
electronics bay
   |
   +-- 24 V high-current pair -------------------+
   |                                             |
   +-- USB data/power ----------------------+    |
                                            |    |
                                      Revival Bed Node
                                            |
                    +-----------------------+-------------------+
                    |                       |                   |
               bed thermistor          LIS2DW/IMU        heater control
                                                                |
                                                          local MOSFET
                                                                |
                                                         silicone heater
```

The USB link carries **control/data only**. Heater energy remains on the dedicated 24 V high-current path.

## Why a custom board

A dedicated bed board avoids carrying several separate moving signal cables and lets the bed assembly become a single Klipper-controlled subsystem.

Target local functions:

- bed temperature sensing;
- permanent Y-axis accelerometer;
- local bed-heater MOSFET gate control;
- optional secondary temperature sensor;
- optional 24 V voltage/current monitoring;
- optional local PCB temperature monitoring;
- future RID diagnostics;
- service/status indication if useful.

The board must not include unnecessary toolhead-specific functions such as an extruder driver.

## MCU direction

A **USB-native MCU supported by Klipper** is preferred. RP2040 is the current reference direction because it provides:

- native USB device support;
- mature Klipper support;
- SPI for LIS2DW-class accelerometers;
- ADC inputs for thermistors and diagnostics;
- sufficient GPIO;
- low cost and wide availability.

The exact MCU and PCB implementation are not yet frozen at component level.

## Klipper integration model

The Bed Node is a normal secondary Klipper MCU.

Conceptual configuration:

```ini
[mcu bed]
serial: /dev/serial/by-id/<REVIVAL_BED_NODE_ID>
```

Klipper then references pins on that MCU by prefix:

```ini
[heater_bed]
heater_pin: bed:<HEATER_GATE_PIN>
sensor_type: <FINAL_SENSOR_TYPE>
sensor_pin: bed:<BED_THERMISTOR_PIN>
control: pid
min_temp: <SAFE_MIN>
max_temp: <SAFE_MAX>
```

The exact pins, thermistor type and temperature limits remain placeholders until the PCB, heater and sensor are released.

### Bed accelerometer

The final custom node should integrate a LIS2DW-class accelerometer or equivalent supported sensor rigidly coupled to the moving bed/carriage.

Conceptual Klipper structure:

```ini
[lis2dw bed_accel]
cs_pin: bed:<CS_PIN>
spi_bus: <BED_NODE_SPI_BUS>
axes_map: <MEASURED_ORIENTATION>
```

and:

```ini
[resonance_tester]
accel_chip_x: <toolhead accelerometer>
accel_chip_y: lis2dw bed_accel
probe_points:
    <safe test point>
```

The final syntax must be validated against the Klipper version in use when the board is commissioned.

## USB behavior and failure handling

The Bed Node is a Klipper MCU, not an autonomous heater controller.

If the Bed Node disconnects or stops communicating, Klipper must treat this as an MCU failure and stop the print/heating process.

The design must never depend on USB/Klipper alone for thermal safety.

Independent safety remains mandatory:

```text
24 V PSU
   |
bed branch fuse
   |
local heater power path
   |
MOSFET
   |
independent thermal fuse
   |
heater
```

The thermal fuse must interrupt heater energy even if:

- Klipper crashes;
- CB2 crashes;
- USB disconnects;
- Bed Node firmware locks;
- MOSFET fails short.

## Heater power stage

The final Bed Node may place the bed MOSFET physically near the bed to shorten the switched high-current path.

Design rules:

- do not route heater current through small MCU-board traces/connectors;
- use a power stage explicitly sized for the final 24 V bed current with thermal margin;
- use suitable copper area / bus structure / connector rating;
- keep logic and thermistor routing away from the high-current switching loop;
- provide strain relief for the moving 24 V pair;
- retain a dedicated branch fuse upstream;
- retain the independent thermal fuse at the heater/plate.

The exact MOSFET, gate driver, connector and PCB copper geometry remain open.

## Mechanical placement

The Bed Node should mount below the Y carriage / heated-bed assembly, thermally separated from the heater and rigidly coupled where required for accelerometer accuracy.

The board should not be attached directly to the hottest heater surface.

Design goals:

- short thermistor wiring;
- short accelerometer connection;
- short MOSFET-to-heater wiring;
- protected USB and 24 V connectors;
- strain relief suitable for repeated Y motion;
- easy board replacement without dismantling the complete bed stack.

## Initial-to-final migration

The custom node is designed so that the printer remains usable before it exists.

Migration plan:

```text
INITIAL
Manta -> bed thermistor
Manta -> external bed MOSFET
CB2 USB -> S2DW

             becomes

FINAL
CB2 USB -> Revival Bed Node
             |- bed thermistor
             |- integrated bed accelerometer
             |- local MOSFET control
             |- optional diagnostics
```

The heater, thermal fuse, bed plate and magnetic/PEI stack should not need to be redesigned merely because control moves to the Bed Node.

## RID opportunities

The Bed Node is a useful sensor source for **Revival Intelligence & Diagnostics**, but RID remains supervisory.

Potential data:

- commanded heater state;
- measured bed temperature;
- warm-up slope;
- cooldown slope;
- 24 V supply voltage;
- heater current;
- local PCB temperature;
- accelerometer/resonance history.

Potential diagnostic correlations include:

- heater commanded on but current absent;
- current present but temperature rise abnormal;
- heater commanded off but current still present;
- gradual warm-up degradation;
- unusual Y-axis resonance changes.

These are diagnostic aids and do not replace physical protection.

## Frozen decisions

- a custom **Revival Bed Node** will be designed for the final Generation 3 bed;
- it communicates with CB2 by **USB** as a secondary Klipper MCU;
- it integrates bed temperature sensing and the permanent Y accelerometer;
- it controls the local bed-heater power stage;
- high-current heater power remains a separate 24 V moving pair;
- safety-critical thermal protection remains independent of Klipper/USB;
- the printer may initially operate with conventional separate bed wiring before the custom board exists;
- the custom Bed Node must be a migration/upgrade, not a commissioning blocker.

## Open decisions

- exact MCU / RP2040 implementation;
- exact LIS2DW or alternative accelerometer part;
- USB connector family and cable/strain-relief scheme;
- 24 V connector and wire gauge;
- MOSFET and gate-driver topology;
- PCB copper/current-path implementation;
- primary thermistor type;
- optional secondary temperature sensor;
- optional voltage/current monitor;
- local DC/DC topology;
- PCB dimensions and mounting holes;
- final Klipper pin map and config include file;
- whether the original S2DW remains useful as a temporary/diagnostic spare after Bed Node commissioning.
