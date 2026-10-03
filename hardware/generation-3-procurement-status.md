# Generation 3 procurement status

This document tracks **actual Generation 3 purchases and near-term acquisition decisions** separately from the target BOM.

It must not be used as evidence that a purchased component has been electrically tested, installed or commissioned.

Last reviewed: **27 September 2026**.

## Purchased

| Component | Quantity | Purchase state | Intended Generation 3 role |
|---|---:|---|---|
| BIGTREETECH Manta M8P V2.0 | 1 | Purchased | Main motion/control MCU board |
| BIGTREETECH EBB36 Gen2 | 1 kit | Purchased | CAN toolhead MCU/driver board; kit includes its Gen2 adapter/protection board |
| BIGTREETECH TMC2209 V1.3 | 6 | Purchased | Manta axis drivers plus spares |

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

## Frozen but not yet purchased

| Component | State | Procurement note |
|---|---|---|
| BIGTREETECH CB2 | Frozen host choice | Wait for a reasonable price/availability; do not buy a CM4 merely because CB2 is temporarily harder to source |
| E3D Roto + Revo | Frozen extrusion architecture | Current purchase preference is **Roto Sensored + Revo 24 V / 40 W**; exact retail bundle/SKU to confirm at purchase |
| BIGTREETECH Eddy Duo | Frozen probe/scanner | Buy when a good offer is found; final mount/routing remains future CAD work |
| BIGTREETECH CEB V1.0 | Frozen CAN backbone/distribution for EBB36/Eddy, Revival Bed Node and RASS CAN Node | Not yet purchased |
| Custom Revival RASS CAN Node | Frozen production controller architecture | Custom PCB to design; Klipper-compatible CAN MCU, exact MCU/transceiver/drivers open |
| BIGTREETECH HDMI5 | Frozen local display | Not yet purchased |
| BIGTREETECH S2DW V1.0 | Transitional USB bed accelerometer for commissioning/bench work before the custom Bed Node | Not yet purchased |
| Mean Well LRS-600-24 | Preferred final PSU | 24 V / 25 A / 600 W; future purchase; Amazon Spain reference: https://www.amazon.es/dp/B0D173X5V3 |

## Existing 24 V PSU for prototype use

An existing **NUOFUWEI S-24-600, 24 V / 25 A / 600 W** supply can be recovered from a previous project and may be used for bench/prototype work after inspection and electrical validation.

It is **not** the preferred final PSU. The final-machine target is the Mean Well LRS-600-24 above.

## Host decision: CB2 versus CM4

The frozen final host remains **BIGTREETECH CB2**.

A Raspberry Pi CM4 is technically viable on the Manta M8P V2.0 and remains a fallback/alternative, but the project will not pay a large premium solely for current Amazon availability.

Current procurement rule:

> Wait for a sensibly priced CB2 unless a later engineering reason justifies switching the frozen host architecture.

CM5 is not the target host.

## Bench-test pack

A versioned acceptance-test pack for the purchased Manta M8P V2.0, six TMC2209 V1.3 modules and EBB36 Gen2 kit is stored at [`bench-tests/generation-3-electronics/`](bench-tests/generation-3-electronics/README.md).

The pack defines receiving inspection, Raspberry Pi 2 temporary-host setup, conservative driver tests, all-eight-socket Manta coverage, EBB36 USB validation and a two-node Manta/EBB36 CAN test. It also provides an acceptance CSV and evidence-capture scripts.

**The existence of the test pack does not change any component to Tested.** That status requires reviewed evidence and a recorded PASS.

## Manta bench testing before CB2 purchase

The Manta M8P V2.0 can be checked before the CB2 arrives.

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
CB2 / Klipper host
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
