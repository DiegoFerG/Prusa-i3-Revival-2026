# Generation 3 electronics bench fixture — dimensional survey

Status: **measurement plan / not yet released for CAD**  
Created: **23 September 2026**

## Purpose

Define the dimensions that must be recorded before designing a reusable open bench fixture for the currently available Generation 3 electronics.

The first fixture is a **bench/workstand**, not the final printer electronics enclosure. Its purpose is to hold the electronics securely, keep connectors accessible and allow repeated low-risk test work without components moving around on the table.

Initial fixture population:

- BIGTREETECH Manta M8P V2.0;
- temporary Raspberry Pi 2 Klipper host;
- 24 V bench power supply used for Generation 3 tests;
- BIGTREETECH EBB USB Adapter V1.0 / EBB36 Gen2 adapter-protection board.

The EBB36 itself remains a movable test device/toolhead node and is **not required to be permanently fixed to this first bench plate** unless later testing shows a clear benefit.

## Measurement conventions

Use millimetres.

For every component, define one mechanical datum:

- **X = left-to-right** when the component is viewed in its intended bench orientation;
- **Y = front-to-back**;
- **Z = height above the mounting surface**.

Record dimensions from the physical part whenever possible. Vendor drawings are references, but the fixture CAD should ultimately match the exact hardware in hand.

For PCB mounting-hole coordinates:

- use the centre of the lower-left mounting hole as the preferred local datum when practical;
- otherwise use the lower-left PCB corner and record every hole centre as an X/Y coordinate;
- record hole diameter separately from centre position.

Do not infer hole locations from photographs.

## Global dimensions required for every component

For each item record:

| Measurement | Why it is required |
|---|---|
| Overall X width | base-plate envelope and component spacing |
| Overall Y depth | base-plate envelope and component spacing |
| Maximum Z height | standoff, guard and cable-clearance design |
| PCB/chassis thickness | mounting-stack calculation |
| Number of mounting points | fixture fastener count |
| Mounting-hole diameter | screw/insert selection |
| Mounting-hole X/Y coordinates or centre spacing | exact CAD hole pattern |
| Minimum safe standoff height | avoid underside solder/component contact |
| Maximum underside protrusion | confirm base-plate clearance |
| Connector protrusion beyond nominal outline | avoid connector collisions |
| Plug/cable insertion direction | define service clearances |
| Minimum plug-removal clearance | permit maintenance without removing neighbouring parts |
| Cable bend/strain-relief envelope | prevent sharp bends at connectors |
| Button/jumper/service access zones | keep BOOT/RESET/jumpers usable |
| Cooling/airflow keep-out | avoid blocking regulators, heatsinks or PSU ventilation |
| Preferred orientation on bench | consistent layout and readable silkscreen |
| Fastener head/washer clearance | prevent collision with components or traces |

## 1. BIGTREETECH Manta M8P V2.0

### Known reference dimensions

Official BIGTREETECH documentation gives the PCB overall size as approximately:

- **X: 170.0 mm**
- **Y: 102.7 mm**

Canonical local vendor references:

- [Manta M8P V2.0 size drawing](../../reference/bigtreetech/manta-m8p-v2.0/BIGTREETECH-MANTA-M8P-V2.0-SIZE.pdf)
- [Manta M8P V2.0 pinout](../../reference/bigtreetech/manta-m8p-v2.0/BIGTREETECH-MANTA-M8P-V2.0-PinOut.png)
- [Manta M8P V2.0 connection diagram](../../reference/bigtreetech/manta-m8p-v2.0/M8P-V2.0-connect.png)

The physical purchased board must still be checked before releasing fixture CAD.

### Measurements to record

- [ ] exact PCB X width
- [ ] exact PCB Y depth
- [ ] PCB thickness
- [ ] number of mounting holes
- [ ] mounting-hole diameters
- [ ] X/Y coordinates of every mounting-hole centre
- [ ] maximum underside component/solder-pin protrusion
- [ ] required standoff height
- [ ] maximum height with TMC2209 installed
- [ ] maximum height with TMC2209 heatsink installed
- [ ] maximum height in the future with CB2 fitted to the BTB connector
- [ ] USB-C connector centre position and cable exit direction
- [ ] Ethernet connector position/clearance if the future CB2 installation uses it
- [ ] microSD/MCU-card insertion/removal clearance
- [ ] BOOT and RESET button access zones
- [ ] driver M1–M8 insertion/removal clearance above board
- [ ] motor-connector cable exit zones
- [ ] main 24 V / motor / bed terminal-block screwdriver access
- [ ] fan/thermistor/endstop connector cable-exit zones
- [ ] CAN connector/cable-exit zone
- [ ] BTB/core-board keep-out rectangle
- [ ] airflow keep-out around regulator/driver area

### Design note

The fixture must allow TMC modules to be inserted and removed without unbolting the Manta. The Manta should therefore have generous free space above the driver sockets and around the power terminals.

## 2. Raspberry Pi 2 — temporary Klipper host

The exact Raspberry Pi 2 model/revision in hand must be confirmed before final CAD. Do not release a mounting pattern based only on generic Raspberry Pi dimensions.

### Measurements to record

- [ ] exact model/revision marking
- [ ] PCB X width
- [ ] PCB Y depth
- [ ] PCB thickness
- [ ] number of mounting holes
- [ ] mounting-hole diameters
- [ ] X/Y coordinates of mounting-hole centres
- [ ] maximum underside protrusion
- [ ] minimum standoff height
- [ ] maximum component Z height
- [ ] USB connector bank position and plug-removal clearance
- [ ] Ethernet connector position and plug/removal clearance
- [ ] micro-USB power connector position and cable bend radius
- [ ] HDMI connector position
- [ ] microSD insertion/removal direction and clearance
- [ ] GPIO header keep-out area
- [ ] activity/power LED visibility requirement
- [ ] any heatsink/fan fitted for the bench

### Design note

This Raspberry Pi is temporary. Its mounting zone should therefore be easy to replace later with a different host or a removable adapter plate rather than making the complete bench fixture Pi-2-specific.

## 3. 24 V bench power supply

The exact power-supply model is not yet recorded in the Generation 3 bench documentation. Photograph and identify the unit before freezing its hole pattern.

### Measurements to record

- [ ] manufacturer/model/rating label
- [ ] overall X width
- [ ] overall Y depth
- [ ] overall Z height
- [ ] chassis mounting-hole/slot count
- [ ] mounting-hole/slot dimensions
- [ ] mounting-hole X/Y coordinates
- [ ] orientation allowed by manufacturer
- [ ] mains-input terminal position
- [ ] protective-earth terminal position
- [ ] 24 V output terminal position
- [ ] voltage-adjust potentiometer position/access
- [ ] terminal screw-driver access volume
- [ ] wire-entry and ferrule bend clearances
- [ ] fan/intake/exhaust position if fitted
- [ ] ventilation keep-out distances
- [ ] exposed-live-terminal guard requirement
- [ ] switch/fuse/IEC inlet geometry if fitted externally

### Safety note

If the bench power supply exposes mains terminals, the finished fixture must include a proper touch-safe cover/guard before powered use. Mechanical dimensions for that guard are part of the fixture design, not an optional cosmetic detail.

## 4. BIGTREETECH EBB USB Adapter V1.0 / adapter-protection board

The adapter remains on the fixed-electronics side of the test setup. It carries part of the EBB36 protection architecture and must not be bypassed.

Canonical local reference:

- [EBB36 Gen2 / USB Adapter official documentation](../../reference/bigtreetech/wiki/EBB36_GEN2.md)
- [USB Adapter interface image](../../reference/bigtreetech/wiki/img/EBB36_GEN2/en/interface_adapter.jpg)

### Measurements to record

- [ ] PCB X width
- [ ] PCB Y depth
- [ ] PCB thickness
- [ ] number of mounting holes
- [ ] mounting-hole diameters
- [ ] X/Y coordinates of mounting-hole centres
- [ ] maximum underside protrusion
- [ ] minimum standoff height
- [ ] maximum Z height including blade fuses
- [ ] USB-C connector position
- [ ] USB-C plug insertion/removal clearance
- [ ] 24 V input connector/terminal position
- [ ] 24 V wiring screwdriver/access clearance
- [ ] EBB harness connector position
- [ ] harness plug-removal clearance
- [ ] CAN/JST connector position if used
- [ ] fuse extraction clearance above the board
- [ ] status-LED visibility
- [ ] any BOOT/RESET/jumper access zones present on the exact revision
- [ ] cable bend/strain-relief envelope toward the EBB36 harness

### Design note

The adapter should be close enough to a fixture edge that USB, 24 V and the EBB36 harness can be connected without routing cables over the Manta.

## Recommended fixture-level measurements

In addition to component dimensions, decide/measure:

- [ ] desired minimum gap between Manta and Raspberry Pi
- [ ] desired minimum gap between Manta and USB Adapter
- [ ] desired minimum gap between PSU and low-voltage logic boards
- [ ] position of the fixture front edge/operator side
- [ ] preferred cable-entry side
- [ ] preferred 24 V distribution side
- [ ] minimum screwdriver access around every terminal block
- [ ] minimum finger clearance for USB plugs and jumpers
- [ ] free zone for a multimeter probe
- [ ] free zone for temporary NEMA17 and thermistor connections
- [ ] possible future zone for CEB V1.0
- [ ] possible future zone for a small passive I/O/breakout board
- [ ] rubber feet / anti-slip dimensions
- [ ] handle or carry-hole geometry if the bench is to be portable

## CAD release gate

Do not release the fixture for printing/manufacture until:

1. every physical component has been identified by exact model/revision;
2. mounting-hole patterns have been measured or verified against trusted drawings;
3. connector and screwdriver service envelopes have been checked;
4. the PSU mains side has a touch-safe mechanical concept;
5. TMC insertion/removal remains possible with Manta installed;
6. the Raspberry Pi area remains replaceable because it is only a temporary host;
7. at least one full-size paper/CAD layout has been checked against the real hardware.

## Measurement record

| Component | Exact revision/model | X | Y | Max Z | Hole pattern | Standoff | Status |
|---|---|---:|---:|---:|---|---:|---|
| Manta M8P | V2.0 purchased board; physical revision to record | 170.0 ref. | 102.7 ref. | TBD | TBD | TBD | Reference dimensions only |
| Raspberry Pi 2 | TBD from physical board | TBD | TBD | TBD | TBD | TBD | Measure |
| 24 V bench PSU | TBD | TBD | TBD | TBD | TBD | n/a / TBD | Identify + measure |
| EBB USB Adapter | V1.0 marking observed; verify exact board | TBD | TBD | TBD | TBD | TBD | Measure |

Update this table from physical measurements before CAD starts.
