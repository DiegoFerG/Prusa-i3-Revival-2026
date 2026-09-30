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
- **local chassis accelerometer on the Bed Node PCB** to measure vibration at the rear lower structure;
- **second remote frame accelerometer** mounted near the top of the flat steel frame;
- local bed-heater MOSFET gate control;
- secondary temperature sensing for thermal-gradient/diagnostic use;
- 24 V voltage/current monitoring;
- local PCB/power-stage temperature monitoring;
- RGB under-bed / under-frame status and decorative lighting;
- future RID diagnostics;
- service/status indication and auxiliary expansion I/O.

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

## Structural vibration sensing

The Bed Node is also the Generation 3 **structural vibration acquisition hub**.

The target sensor set is:

1. **Toolhead accelerometer** on the EBB36 Gen2 — moving X/toolhead response.
2. **Remote bed IMU** connected to the Bed Node — moving Y/bed response.
3. **Local chassis IMU** mounted directly on the fixed Bed Node PCB — rear/lower-structure response.
4. **Remote frame-top IMU** connected to the Bed Node — response of the upper region of the original flat steel frame.

Conceptual topology:

```text
                    FRAME-TOP IMU
                         |
                         | dedicated robust link
                         |
EBB36 IMU ----> Klipper/RID <---- Bed Node local IMU
   |                                      |
 toolhead                           lower/rear chassis
                                          |
                                          +---- remote BED IMU
                                                moving Y bed
```

The purpose is not to replace normal Klipper Input Shaper tuning. The **bed IMU** remains the Y-axis tuning sensor, while the chassis and frame-top IMUs provide structural reference channels for RID and engineering analysis.

### Multi-sensor comparison goals

RID may compare simultaneous or repeatable captures to distinguish:

- motion dominated by the bed;
- motion dominated by the toolhead;
- structural amplification in the flat steel frame;
- energy transmitted into the lower threaded-rod structure;
- new resonances caused by loose fasteners, rail alignment changes, belt tension changes or component ageing;
- changes between an empty bed and a heavy printed part.

The project should preserve baseline spectra so later captures can be compared over time.

### Electrical interface

The bed IMU is close enough for a short flexible SPI connection.

The frame-top IMU is much farther away. The board should therefore reserve a **separate interface** for it instead of assuming that a long unbuffered high-speed SPI cable will always be reliable.

Design provisions should include:

- independent chip select / bus assignment;
- configurable lower SPI speed where supported;
- series damping resistors;
- ground-referenced twisted conductors;
- robust keyed connector;
- PCB footprints or an adapter option for buffered/differential signalling if real-machine tests show it is necessary.

The exact physical signalling method for the frame-top IMU remains open until cable-length/EMI testing is performed.

## RGB status / decorative lighting

The Bed Node will provide a dedicated output for **under-bed / under-structure RGB lighting**.

The preferred implementation is a 24 V common-anode/common-supply analogue RGB strip driven by three local MOSFET PWM channels:

```text
24 V RGB strip
   |
   +-- R --> MOSFET --> Bed Node PWM
   +-- G --> MOSFET --> Bed Node PWM
   +-- B --> MOSFET --> Bed Node PWM
```

This keeps the lighting compatible with the printer's 24 V distribution and avoids requiring addressable LED electronics for the basic status function.

The RGB lighting has two roles:

- decorative ambient lighting beneath the bed / historical lower structure;
- machine-status indication.

Initial status language:

- green — print completed;
- red — error / fault;
- amber/yellow — paused / operator attention;
- blue — heating / preparation;
- white or subdued neutral — normal/ready state;
- other colours — maintenance, diagnostics or future RID states.

The exact colours and transitions remain a UI decision and may be refined later.

Klipper should expose the output through a normal RGB LED abstraction where practical, allowing macros to change the state without custom MCU firmware.

## Sensor and telemetry capacity

The Bed Node should collect as much **useful, actionable** information as practical without compromising heater safety or adding fragile complexity.

High-priority measurements:

- primary bed NTC for Klipper control;
- secondary bed temperature channel for thermal-gradient/diagnostic comparison;
- local PCB/power-stage temperature;
- heater current;
- local 24 V rail voltage;
- heater command/PWM state;
- local chassis acceleration;
- moving-bed acceleration;
- frame-top acceleration.

This enables derived values such as:

- heater electrical power;
- apparent heater resistance trend;
- warm-up/cooldown rate;
- voltage sag under heater load;
- commanded-heater versus measured-current mismatch;
- long-term thermal and vibration signatures.

Example derived calculations:

```text
R_heater = V / I
P_heater = V * I
```

These values are diagnostic only and do not replace electrical protection.

The PCB should also reserve:

- spare ADC input(s);
- spare digital GPIO;
- auxiliary I2C;
- optional fast digital input;
- 3.3 V / 5 V / GND service pins;
- status LEDs and test points.

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
             |- bed thermistor(s)
             |- remote bed IMU
             |- local chassis IMU
             |- remote frame-top IMU
             |- local MOSFET control
             |- voltage/current/temperature telemetry
             |- RGB status lighting
             |- auxiliary diagnostics
```

The heater, thermal fuse, bed plate and magnetic/PEI stack should not need to be redesigned merely because control moves to the Bed Node.

## RID opportunities

The Bed Node is a useful sensor source for **Revival Intelligence & Diagnostics**, but RID remains supervisory.

Potential data:

- commanded heater state;
- primary and secondary bed temperatures;
- warm-up slope;
- cooldown slope;
- 24 V supply voltage;
- heater current;
- calculated heater power/resistance trend;
- local PCB/power-stage temperature;
- bed acceleration;
- lower-chassis acceleration;
- frame-top acceleration;
- cross-sensor resonance / vibration history;
- RGB/status state history where useful.

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
- it includes a **local chassis accelerometer** and a **remote frame-top accelerometer interface**;
- it controls the local bed-heater power stage;
- it provides **24 V RGB under-bed/under-frame status lighting control**;
- it reserves telemetry for heater current, 24 V rail and local thermal monitoring;
- high-current heater power remains a separate 24 V moving pair;
- safety-critical thermal protection remains independent of Klipper/USB;
- the printer may initially operate with conventional separate bed wiring before the custom board exists;
- the custom Bed Node must be a migration/upgrade, not a commissioning blocker.

## Open decisions

- exact MCU / RP2040 implementation;
- exact LIS2DW or alternative accelerometer parts and daughterboard connector/cable choices;
- final long-distance frame-top IMU signalling method (direct SPI at reduced speed vs buffered/differential adapter after testing);
- USB connector family and cable/strain-relief scheme;
- 24 V connector and wire gauge;
- MOSFET and gate-driver topology;
- PCB copper/current-path implementation;
- primary thermistor type;
- exact secondary temperature sensor implementation;
- exact voltage/current monitor implementation;
- RGB strip connector, MOSFETs, current budget and mechanical routing;
- local DC/DC topology;
- PCB dimensions and mounting holes;
- final Klipper pin map and config include file;
- whether the original S2DW remains useful as a temporary/diagnostic spare after Bed Node commissioning.
