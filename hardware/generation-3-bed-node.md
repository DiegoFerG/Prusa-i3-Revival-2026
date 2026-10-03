# Generation 3 Revival Bed Node

This document defines the planned **Revival Bed Node**, a custom dual-interface **CAN + USB Klipper MCU** mounted in a printed enclosure on the **fixed rear cross-member of the historical lower frame**, close to the moving Y/bed assembly. Normal production communication is over the Generation 3 CAN network through the BIGTREETECH CEB V1.0; USB-C remains available for first flash, recovery, bench diagnostics and an optional alternate Klipper transport.

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

After the custom PCB is designed, assembled and validated, bed-local functions migrate to a dedicated MCU connected normally to the Generation 3 CAN network through the **BIGTREETECH CEB V1.0**. A USB-C port remains on the board for first flash, recovery, bench diagnostics and optional alternate USB runtime operation. The Bed Node itself remains **fixed to the chassis**; only the short output harness from the rear cross-member to the moving bed must be highly flexible.

Target topology:

```text
Manta M8P V2 CAN
       |
       v
BIGTREETECH CEB V1.0
       |
       +-- CAN-H / CAN-L --------------------------+
                                                     |
24 V logic / auxiliary feed ------------------------+----> Revival Bed Node
                                                     |      fixed rear cross-member
USB-C service / recovery / alternate runtime -------+             |
                                                                   |
24 V PSU -> dedicated bed fuse -> heater power stage --------------+
                                                                   |
                                                     short flexible bed harness
                                                     +---------+---------+---------+
                                                     |         |         |
                                                  heater   thermistor  remote IMU
                                                     |
                                              independent thermal fuse path
                                                     |
                                                  moving bed
```

The normal Bed Node data path is **CAN through the CEB**. The CAN/logic feed and optional USB-C service cable do not need to be highly flexible because the board is fixed to the rear cross-member. Only the short Bed Node-to-bed harness sees continuous Y-axis motion.

CAN and USB carry **control/data only**. Heater energy remains on the dedicated fused 24 V high-current path and must never be routed through the CEB or USB connector.

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

A **Klipper-supported MCU with a robust CAN implementation and native/accessible USB recovery path** is required. The Bed Node follows the common [custom CAN-node design rules](generation-3-custom-can-node-design-rules.md). The production design must support:

- normal Klipper communication over CAN;
- USB-C first-flash and recovery access;
- optional alternate Klipper communication over USB for bench/service use;
- SPI for LIS2DW-class accelerometers;
- ADC inputs for thermistors and diagnostics;
- sufficient GPIO;
- low-cost, serviceable components with good upstream support;
- a package/pinout that allows every remaining electrically usable MCU pin to be exposed after all frozen Bed Node functions are assigned.

The CAN physical layer requires a dedicated transceiver, ESD/transient protection appropriate to the final harness, and a selectable **120-ohm termination** so the Bed Node can be used correctly at an end of the physical bus. RP2040 remains a candidate only with a validated Klipper/Katapult CAN implementation; STM32 parts with well-supported CAN peripherals are also candidates. The exact MCU, transceiver and PCB implementation are not yet frozen at component level.

## Klipper integration model

The Bed Node is a normal secondary Klipper MCU.

Production CAN configuration:

```ini
[mcu bed]
canbus_uuid: <REVIVAL_BED_NODE_CAN_UUID>
```

Alternate USB bench/service configuration:

```ini
[mcu bed]
serial: /dev/serial/by-id/<REVIVAL_BED_NODE_ID>
```

The hardware exposes both transports, but the production configuration uses **CAN as the normal runtime link**. USB is retained as a recovery/diagnostic path and may be used as an alternate runtime transport with the matching Klipper firmware build; the same physical MCU must not be configured twice as if CAN and USB were two independent MCUs.

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

The PCB follows the [full unused-pin exposure policy](generation-3-custom-can-node-design-rules.md). **After** the bed heater, thermistors, current/voltage telemetry, RGB outputs and all production accelerometers are allocated, every remaining electrically usable MCU pin must be brought out to a labelled expansion connector, header position or accessible expansion pad.

Where the final pin mux permits it, exposed pins should be grouped into useful SPI, I2C, UART, ADC and GPIO/PWM expansion areas, but no otherwise-usable unused pin may be hidden merely because the minimum grouped connectors already exist.

BOOT/RESET and the native debug interface remain separately exposed as service resources. When applicable to the selected MCU, the Bed Node shall include **dedicated BOOT/BOOTSEL and RESET tactile pushbuttons**, comparable to the service controls on the EBB36. The native debug interface (for example SWDIO/SWCLK/GND/3V3 on STM32) shall be available on a dedicated header or clearly labelled service pads. Any MCU pin that cannot be exposed must be listed in the Bed Node resource ledger with the specific hardware reason.

## Building and flashing Klipper firmware

The Bed Node shall use **unmodified upstream Klipper MCU firmware**. A private Revival Klipper MCU fork, patched Klipper `src/` tree or custom MCU command is outside the frozen architecture. Revival-specific behaviour must remain in normal Klipper configuration/macros or Linux-host software wherever practical.

For an RP2040-class design, the normal process is:

1. Install/maintain the Klipper source tree on the CB2 or temporary Linux host.
2. Run `make menuconfig`.
3. Select the MCU family matching the Bed Node hardware, for example RP2040.
4. Select **CAN bus** as the normal production communication interface. Build a USB-runtime image only when intentionally using the alternate service mode.
5. Build with `make`.
6. Flash the resulting firmware using the MCU's supported USB bootloader/recovery method for first commissioning, or the validated CAN bootloader/update path once established.
7. For CAN operation, identify the Bed Node `canbus_uuid`; for alternate USB operation, identify its stable `/dev/serial/by-id/` path.
8. Add the selected transport to the printer configuration as `[mcu bed]`.
9. Restart Klipper and verify MCU communication before enabling any heater output.

For an RP2040 reference implementation, initial flashing is expected to use the ROM USB mass-storage boot mode (BOOTSEL) or a documented equivalent. Where applicable, **BOOTSEL and RESET will be real PCB pushbuttons rather than recovery-only test pads**, so normal commissioning/recovery does not require jump wires or desoldering.

Conceptually:

```text
Klipper source
   |
make menuconfig
   |
select MCU + CAN
   |         \
   |          \-> optional USB runtime/service build
   |
make
   |
klipper firmware image
   |
BOOT/DFU/UF2 method
   |
Revival Bed Node
   |
CAN UUID discovery
   |
   +-- optional USB enumeration
   |
canbus_uuid
   |
   +-- optional /dev/serial/by-id/...
   |
[mcu bed]
```

### Firmware-update strategy

The PCB should support **two levels of recovery**:

- normal in-system firmware update over a validated CAN/Katapult path where supported;
- USB-C first-flash/service update and hardware recovery using accessible BOOT/RESET controls or test pads.

The design must never require heater power to be connected merely to flash or recover the MCU.

The repository should eventually contain:

- the exact `make menuconfig` selections;
- generated/validated firmware-build instructions;
- the Bed Node pin map;
- the Klipper include file;
- first-flash and recovery procedures;
- firmware revision/hash used during validation.

## CAN / USB behavior and failure handling

The Bed Node is a Klipper MCU, not an autonomous heater controller.

If the Bed Node disconnects from its selected runtime transport (normally CAN) or stops communicating, Klipper must treat this as an MCU failure and stop the print/heating process.

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
- CAN communication is lost or the alternate USB link disconnects;
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

- the incoming CAN, logic-power and optional USB-C service harness can be fixed or only gently flexed;
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
Manta CAN -> CEB -> Revival Bed Node
                    |- optional USB-C service/recovery
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
- it communicates normally as a secondary Klipper MCU over **CAN through the BIGTREETECH CEB V1.0**;
- it retains **USB-C** for first flash, recovery, bench diagnostics and optional alternate USB runtime operation;
- its MCU firmware is built from **unmodified upstream Klipper**; no production feature depends on a private Revival MCU firmware fork;
- after all production functions are allocated, it exposes **every remaining electrically usable MCU pin** for future expansion, with alternate functions documented and any exceptions justified in the resource ledger;
- it integrates bed temperature sensing and interfaces to a **remote moving Y accelerometer daughterboard**;
- it includes a **local chassis accelerometer** and a **remote frame-top accelerometer interface**;
- it controls the local bed-heater power stage;
- it provides **24 V RGB under-bed/under-frame status lighting control**;
- it reserves telemetry for heater current, 24 V rail and local thermal monitoring;
- high-current heater power remains a separate 24 V moving pair;
- safety-critical thermal protection remains independent of Klipper/CAN/USB;
- the printer may initially operate with conventional separate bed wiring before the custom board exists;
- the custom Bed Node must be a migration/upgrade, not a commissioning blocker.

## Open decisions

- exact MCU/package selection that satisfies the frozen Bed Node functions while allowing all remaining electrically usable MCU pins to be physically exposed;
- exact LIS2DW or alternative accelerometer parts and daughterboard connector/cable choices;
- final long-distance frame-top IMU signalling method (direct SPI at reduced speed vs buffered/differential adapter after testing);
- CAN transceiver/protection implementation, connector family, bus-stub length and selectable 120-ohm termination;
- USB-C connector, ESD protection and cable/strain-relief scheme;
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
