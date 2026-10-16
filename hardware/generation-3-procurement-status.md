# Generation 3 procurement status

This document tracks **actual Generation 3 purchases and near-term acquisition decisions** separately from the target BOM.

It must not be used as evidence that a purchased component has been electrically tested, installed or commissioned.

Last reviewed: **16 October 2026**.

## Purchased

| Component | Quantity | Purchase state | Intended Generation 3 role |
|---|---:|---|---|
| BIGTREETECH Manta M8P V2.0 | 1 | Purchased | Main motion/control MCU board |
| BIGTREETECH EBB36 Gen2 | 1 kit | Purchased | CAN toolhead MCU/driver board; kit includes its Gen2 adapter/protection board |
| BIGTREETECH TMC2209 V1.3 | 6 | Purchased | Manta axis drivers plus spares |
| BIGTREETECH CB1 | 1 | Received; active temporary bench host | Retain for baseline comparison until CM4 is commissioned |
| Raspberry Pi CM4 CM4102016 (2 GB RAM / 16 GB eMMC, Wi-Fi/BT) | 1 | **Ordered 16 October 2026; not yet received/tested** | New intended Manta Linux host; Ethernet preferred; Raspberry Pi OS Lite 64-bit initial OS; SSD USB planned |
| BIGTREETECH CEB V1.0 | 1 | **Ordered 16 October 2026; not yet received/tested** | CAN distribution/backbone for EBB36/Eddy Duo and future Bed/RASS nodes |
| BIGTREETECH Eddy Duo | 1 | Received; USB communication and raw sensor acquisition tested | Probe/scanner; final mount/calibration/CAN pending |
| Innomaker U30CAM-4K-S1 | 1 | Received; UVC and Mainsail video tested | Main frame camera; sustained/higher-mode testing pending |

### TMC2209 allocation

The base Generation 3 machine does **not** require eight populated Manta driver sockets.

Expected base allocation:

- X;
- Y;
- Z0;
- Z1.

The E3D Roto extruder is driven by the **TMC2209 integrated on the EBB36 Gen2**, not by a Manta socket.

Therefore the six purchased plug-in TMC2209 modules provide:

- four expected base axis drivers;
- two immediate spares / future expansion modules.

Additional Manta drivers should only be purchased if a later subsystem actually requires them.

## Existing prototype stock

### RASS prototype parts already on hand

| Component | Quantity | Status | Intended test |
|---|---:|---|---|
| 28BYJ-48 5 V geared stepper | at least 1 observed | Existing part; untested for RASS | Candidate spool-drive motor only |
| ULN2003 5 V stepper driver board | at least 1 observed | Existing part; untested for RASS | Early standalone spool-drive bench prototype only; not the production CAN-node driver |

These parts are **not** frozen production selections and are **not** candidates for the precision filament feeder. They are retained as the preferred no-cost prototype for active spool rotation and must be tested with a full spool and the final load-cell/roller concept.

## Planned, alternative or not yet purchased

| Component | State | Procurement note |
|---|---|---|
| BIGTREETECH CB2 | Previous final host choice; unpurchased fallback | CM4 now ordered for evaluation; CB2 remains an option if acceptance or later requirements justify reconsideration |
| E3D Roto + Revo | Frozen extrusion architecture | Current purchase preference is **Roto Sensored + Revo 24 V / 40 W**; exact retail bundle/SKU to confirm at purchase |
| Custom Revival RASS CAN Node | Frozen production controller architecture | Custom PCB to design; Klipper-compatible CAN MCU, exact MCU/transceiver/drivers open |
| BIGTREETECH HDMI5 | Frozen local display | Not yet purchased |
| BIGTREETECH S2DW V1.0 | Transitional USB bed accelerometer for commissioning/bench work before the custom Bed Node | Not yet purchased |
| Mean Well LRS-600-24 | Preferred final PSU | 24 V / 25 A / 600 W; future purchase; Amazon Spain reference: https://www.amazon.es/dp/B0D173X5V3 |

## Existing 24 V PSU for prototype use

An existing **NUOFUWEI S-24-600, 24 V / 25 A / 600 W** supply can be recovered from a previous project and may be used for bench/prototype work after inspection and electrical validation.

It is **not** the preferred final PSU. The final-machine target is the Mean Well LRS-600-24 above.

## Host procurement and operating system — 16 October 2026

A **Raspberry Pi Compute Module 4 CM4102016 (2 GB LPDDR4, 16 GB eMMC, Wi-Fi/BT)** has been **ordered** for the Manta M8P V2.0. It is the **selected next host for commissioning**, replacing the CB1 used in the bench. Ethernet is preferred; onboard Wi-Fi is an available fallback. The previous CB2 target is **not a purchase commitment** and remains a possible alternative if testing shows a reason to revisit host selection.

**Initial operating system: Raspberry Pi OS Lite 64-bit (ARM64)** installed on eMMC. This is a **provisional, reversible deployment choice**, not a permanent operating-system freeze. DietPi, minimal Debian, Gentoo, Alpine, Buildroot or custom LFS-style builds remain future research options, to be evaluated only after the core Klipper/USB/Ethernet/CAN/camera functions work reliably. Ubuntu Server is viable but not selected for initial bring-up.

The 16 GB eMMC is reserved primarily for the OS and printer services. A **separate USB SSD is planned** for larger G-code archives, media/timelapses, diagnostics and backups. Do not assume the carrier microSD slot is available as additional CM4 storage when the CM4 has eMMC.

The ordered CM4 and CEB are **not marked received, installed, validated or commissioned** until the corresponding acceptance records exist. The canonical frozen architecture documents may contain historical CB2 wording; this dated procurement decision governs the next bench build and must be reconciled after host acceptance.

## Bench-test pack

A versioned acceptance-test pack for the purchased Manta M8P V2.0, six TMC2209 V1.3 modules and EBB36 Gen2 kit is stored at [`bench-tests/generation-3-electronics/`](bench-tests/generation-3-electronics/README.md).

The pack defines receiving inspection, Raspberry Pi 2 temporary-host setup, conservative driver tests, all-eight-socket Manta coverage, EBB36 USB validation and a two-node Manta/EBB36 CAN test. It also provides an acceptance CSV and evidence-capture scripts.

**The existence of the test pack does not change any component to Tested.** That status requires reviewed evidence and a recorded PASS.

## Manta bench testing and CM4 handover

The Manta M8P V2.0 has been checked with the existing CB1; continue bench tests before and after installing the ordered CM4.

A temporary Linux host can run Klipper and communicate with the Manta over USB:

```text
temporary Linux PC / Raspberry Pi
              |
             USB
              |
        Manta M8P V2.0
```

This permits staged verification of:

- board power-up;
- USB/MCU communication;
- firmware flashing/DFU workflow;
- Klipper MCU connection;
- TMC2209 detection after drivers are fitted;
- endstop/input tests;
- low-risk fan/output tests;
- later CAN testing once a second CAN node is available.

The final integrated CAN architecture is:

```text
CM4 / Klipper host (after acceptance)
       |
Manta M8P V2.0
       |
      CAN
       |
BIGTREETECH CEB V1.0
       |
       +-- EBB36 Gen2
       |      |
       |      +-- CAN passthrough -> Eddy Duo
       |
       +-- Revival Bed Node
       |      |
       |      +-- USB-C service / recovery / optional alternate runtime
       |
       +-- Custom RASS CAN Node
              |
              +-- feeder / spool assist / buffer / encoder sensing
```

The CEB is the Generation 3 CAN backbone/distribution point. Bed-heater power remains on its own dedicated fused 24 V high-current path and is not routed through the CEB.

## Frozen toolhead purchase direction

The Generation 3 toolhead stack is frozen as:

- BIGTREETECH EBB36 Gen2;
- E3D Roto;
- E3D Revo;
- BIGTREETECH Eddy Duo.

Current purchase preference:

- **Roto Sensored** rather than Standard;
- **Revo 24 V / 40 W** rather than 60 W for the quality-first PLA use case;
- 0.4 mm Revo nozzle as the normal starting nozzle.

Roto Sensored and the 40 W HeaterCore are procurement preferences within the frozen Roto/Revo architecture. They should be re-checked against the exact product revision available at purchase time.

## Eddy Duo electrical topology

The intended toolhead bus topology is:

```text
Manta / CEB
   |
   | 24 V + GND + CAN-H + CAN-L
   v
EBB36 Gen2 + Gen2 adapter/protection board
   |
   | CAN passthrough + regulated 5 V + GND
   v
Eddy Duo
```

Key rules:

- EBB36 receives the main toolhead 24 V supply.
- Eddy Duo must **not** be fed with 24 V.
- Eddy Duo is supplied at **5 V** and is treated as its own CAN MCU/node.
- Eddy Duo is not configured as an I2C peripheral of the EBB36; that topology applies to an Eddy Coil-class sensor, not the Duo.
- If Eddy Duo is the physical end of the CAN bus, termination is enabled at the bus ends only; the intermediate EBB36 termination must remain disabled.
- Exact connector pinout and harness implementation must be verified against the hardware revision in hand before wiring.

## Receiving inspection rule

Every Generation 3 purchase should be tested while return/warranty windows are still open.

Minimum process:

1. photograph packaging, labels and PCB revision;
2. record supplier/date;
3. inspect for transport damage;
4. verify the exact revision against the canonical architecture;
5. perform a low-risk bench test before long-term storage;
6. update this procurement file and the Obsidian knowledge base;
7. only then mark the component as **tested**.

Purchased is not the same as tested, and tested is not the same as commissioned.

## Partial test evidence — 8 October 2026

[USB bench session](bench-tests/generation-3-electronics/records/2026-10-08-usb-eddy-camera.md) records current replacement Manta, CB1, EBB36 Gen2, Eddy Duo and camera. Earlier faulty Manta was returned. Communication and limited sensor/video results are now recorded, but no blanket full-board PASS, motion/heater commissioning or CAN acceptance is claimed. CEB ordered 16 October 2026; awaiting receipt, inspection and CAN bench acceptance.
