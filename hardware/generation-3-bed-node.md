# Generation 3 Revival Bed Node

This document defines the planned **Revival Bed Node**, a custom USB-connected Klipper MCU mounted in a printed enclosure on the **fixed rear cross-member of the historical lower frame**, close to the moving Y/bed assembly.

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

After the custom PCB is designed, assembled and validated, bed-local functions migrate to a dedicated MCU connected to the CB2 over USB. The Bed Node itself remains **fixed to the chassis**; only the short output harness from the rear cross-member to the moving bed must be highly flexible.

Target topology:

```text
electronics bay / CB2
   |
   +-- fixed/semi-fixed 24 V feed ------------------+
   |                                                |
   +-- fixed/semi-fixed USB --------------------+   |
                                               |   |
                                  Revival Bed Node
                                fixed rear cross-member
                                               |
                     short flexible bed harness
                     +-----------+-----------+-----------+
                     |           |           |           |
                  heater      thermistor   remote IMU  thermal fuse path
                     |           |           |
                     +-----------+-----------+----> moving bed
```

The 24 V + USB **feed into the Bed Node does not need to be highly flexible** because the board is fixed to the rear cross-member. Only the short Bed Node-to-bed harness sees continuous Y-axis motion.

The USB link carries **control/data only**. Heater energy remains on the dedicated 24 V high-current path.

## Why a custom board

A dedicated bed board avoids carrying several separate moving signal cables and lets the bed assembly become a single Klipper-controlled subsystem.

Target local functions:

- bed temperature sensing;
- permanent Y-axis accelerometer through a **small remote IMU PCB mounted rigidly on the moving bed/carriage**;
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

Because the Bed Node PCB is fixed to the rear frame cross-member, the accelerometer must **not** be mounted on the main Bed Node PCB. A small remote IMU daughterboard is mounted rigidly on the moving bed/Y-carriage and connected to the Bed Node by a short flexible cable.

Preferred topology:

```text
Revival Bed Node (fixed)
        |
      SPI
        |
short flexible cable
        |
Revival Bed IMU (moving)
        |
      LIS2DW
```

The remote IMU PCB should contain as little as practical beyond the accelerometer, decoupling and connector so moving mass remains negligible.

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

## Building and flashing Klipper firmware

The custom board does **not** require a special Revival fork of Klipper if it uses an MCU already supported by upstream Klipper.

For an RP2040-class design, the normal process is:

1. Install/maintain the Klipper source tree on the CB2 or temporary Linux host.
2. Run `make menuconfig`.
3. Select the MCU family matching the Bed Node hardware, for example RP2040.
4. Select the required communication interface, normally **USB** for the Bed Node.
5. Build with `make`.
6. Flash the resulting firmware using the MCU's supported bootloader/recovery method.
7. Reconnect the board and identify its stable Linux serial path under `/dev/serial/by-id/`.
8. Add that path to the printer configuration as `[mcu bed]`.
9. Restart Klipper and verify MCU communication before enabling any heater output.

For an RP2040 reference implementation, initial flashing is expected to use the ROM USB mass-storage boot mode (BOOTSEL) or a documented equivalent. The exact boot/reset buttons or test pads will be designed into the custom PCB so recovery does not require desoldering.

Conceptually:

```text
Klipper source
   |
make menuconfig
   |
select MCU + USB
   |
make
   |
klipper firmware image
   |
BOOT/DFU/UF2 method
   |
Revival Bed Node
   |
USB enumeration
   |
/dev/serial/by-id/...
   |
[mcu bed]
```

### Firmware-update strategy

The PCB should support **two levels of recovery**:

- normal in-system firmware update over the supported USB bootloader path;
- hardware recovery using accessible BOOT/RESET controls or test pads.

The design must never require heater power to be connected merely to flash or recover the MCU.

The repository should eventually contain:

- the exact `make menuconfig` selections;
- generated/validated firmware-build instructions;
- the Bed Node pin map;
- the Klipper include file;
- first-flash and recovery procedures;
- firmware revision/hash used during validation.

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

The Bed Node is mounted in a **printed fixed enclosure on the rear transverse member of the original threaded-rod structure**.

This location is preferred because:

- the incoming 24 V and USB harness can be fixed or only gently flexed;
- the power stage and MCU do not add moving Y mass;
- the board can be larger and better cooled than a bed-mounted PCB;
- service access is easier;
- only a short harness must flex with the bed;
- the local MOSFET remains close to the heater while still being chassis-mounted.

The moving harness from Bed Node to bed carries only the functions that physically terminate on the moving assembly:

- heater power pair;
- thermistor pair;
- remote-IMU cable;
- thermal-fuse/heater series path as required by final wiring.

The printed enclosure must provide protected connectors, strain relief, ventilation appropriate to the MOSFET losses and finger-safe separation from any exposed power terminals.

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
- it integrates bed temperature sensing and interfaces to a **remote moving Y accelerometer daughterboard**;
- it controls the local bed-heater power stage;
- high-current heater power remains a separate 24 V moving pair;
- safety-critical thermal protection remains independent of Klipper/USB;
- the printer may initially operate with conventional separate bed wiring before the custom board exists;
- the custom Bed Node must be a migration/upgrade, not a commissioning blocker.

## Open decisions

- exact MCU / RP2040 implementation;
- exact LIS2DW or alternative accelerometer part and remote IMU daughterboard connector/cable;
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
