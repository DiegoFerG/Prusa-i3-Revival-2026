# Final build architecture — Generation 3

> Frozen architectural baseline for the **Revival 2026 final build**. Agreed 13 September 2026. Implementation remains deferred until the original and transitional generations have been documented and tested.

## Scope and generation model

This document defines the target control, electrical, thermal, sensing, user-interface and internal-network architecture for the final machine.

The project generations are:

1. **Original Hardware Revival** — Arduino Mega 2560 + RAMPS-era electronics and the legacy 3 mm / 2.85 mm machine.
2. **Re-ARM transitional study** — Panucatt Re-ARM + RAMPS-era hardware as the period 32-bit intermediate generation.
3. **Revival 2026 final build** — Manta/CB2/Klipper, 24 V, CAN toolhead and modern sensing while preserving the classic i3 character.

`Stage` in `docs/ROADMAP.md` means restoration workflow stage. **Generation 3** here is the final machine configuration and is not Roadmap Stage 03.

## Non-negotiable constraints

- Preserve the original steel frame, classic i3 silhouette and machine envelope.
- Preserve the historical lower threaded-rod structure as functional final hardware: **2× M10×350 mm longitudinal rods and 4× M8×200 mm transverse rods**. Do not replace this base with a modern aluminium-extrusion chassis.
- Preserve the **original heated-bed footprint and travel envelope**; do not enlarge the printer to fit a modern standard bed.
- Preserve original bed mounting geometry unless a hidden equivalent adapter is required.
- Hide modern electronics/cable management where practical.
- Give the 5-inch touchscreen a deliberately retro industrial enclosure/theme.
- Give any integrated camera a deliberate **retro video-surveillance / CCTV visual language**, rather than exposing a modern bare camera board or generic webcam shell.
- Build all mains and low-voltage wiring from scratch; the recovered harness remains archival evidence.
- Safety-critical protection must not depend solely on Linux, Klipper or CAN.

## Visual identity and colour policy

The final machine preserves the historical **red-and-black** visual identity of the original build without requiring an exact colour match to the filament used thirteen years earlier.

- All newly manufactured **mechanical and structural printed parts are red**.
- The exact shade of red is **not constrained**; consistency of the red/black language matters more than matching a specific historical filament, manufacturer or colour code.
- The **steel frame, rods and other exposed structural metalwork are black** where the design/material permits.
- **ASA is the preferred final material** for red printed mechanical/structural parts where suitable and available. Material choice must still respect mechanical, thermal and dimensional requirements.
- Electronics enclosures, camera housings, touchscreen housings and other newly introduced non-historical assemblies are **not bound to the red-printed-parts rule**. Their colour and material remain open until their design stage and will be selected according to function, thermal behaviour, ventilation, manufacturability and overall aesthetics.
- New enclosures may deliberately introduce another colour or material if doing so improves the final industrial/retro design language without weakening the historical red-and-black identity of the printer itself.

This is a design identity rule, not a requirement to reproduce the exact appearance or material of every original printed part.

## Core controller stack

### Main controller

**BIGTREETECH Manta M8P V2.0 + CB2 + TMC2209** is the frozen Generation 3 controller family. The Manta M8P V2.0 and six BTT TMC2209 V1.3 plug-in modules have been purchased; CB2 remains the frozen final host but is intentionally deferred until a sensibly priced unit is available. Four Manta drivers are expected for X/Y/Z0/Z1, with the Roto driven by the TMC2209 integrated on the EBB36 Gen2.

Initial Manta driver allocation:

| Channel | Function |
|---|---|
| X | X motor |
| Y | Y motor |
| Z0 | left Z motor |
| Z1 | right Z motor |
| Remaining sockets | spare/future documented expansion |

The extruder motor is driven locally by the EBB36 Gen2 onboard TMC2209. Z0 and Z1 remain independent for probe-assisted gantry alignment.

### Host software

The **CB2** runs:

- Klipper host;
- Moonraker;
- Mainsail;
- KlipperScreen;
- Crowsnest;
- Klipper resonance-analysis tools.

A separate Raspberry Pi is not part of the target architecture.

### Bench-test host before CB2

The Manta M8P V2.0 may be bench-tested before the CB2 is purchased by using a temporary Linux PC or Raspberry Pi as the Klipper host over USB. This is explicitly a commissioning/learning aid and does not change CB2 as the frozen final host.

## Local display

Use a **BIGTREETECH HDMI5 5-inch capacitive touchscreen** running KlipperScreen.

Integration requirements:

- custom ASA enclosure attached cleanly to the original frame;
- period/industrial visual language rather than a tablet-like mount;
- subdued default colours and no permanent gaming/RGB aesthetic;
- no significant increase in the printer envelope.

Mainsail remains available remotely from desktop, tablet or phone.

### RASS local spool touchscreen

A second, **smaller touchscreen** is mounted beside the RASS/spool assembly. It is a dedicated spool HMI rather than a second full KlipperScreen desktop.

The preferred implementation is a self-rendering **serial HMI with a wired connection to the Linux host**, normally through USB-to-serial or equivalent. This avoids relying on a second CB2 graphical-display pipeline while the primary BIGTREETECH HDMI5 remains the main KlipperScreen display.

The local panel shows spool identity/material/colour, remaining material, RFID/tag state, RASS/feed status, relevant warnings and nozzle readiness. It provides touch **LOAD** and **UNLOAD** requests.

The local panel has no direct authority over the RASS motors. CB1 during bench development and CB2 in the final machine own the UI state and command policy. LOAD/UNLOAD controls are enabled only when the host determines that no print is active and the extrusion/RASS state is safe; every touch request is revalidated on the host immediately before the corresponding macro/action is executed.

## CAN bus

CAN is a permanent internal bus in Generation 3, used where it reduces moving wiring and improves modularity.

- Manta M8P V2.0 provides the primary CAN interface.
- **BIGTREETECH CEB V1.0** is the protected CAN distribution/breakout point and physical backbone in the electronics bay.
- **BIGTREETECH EBB36 Gen2** is the permanent toolhead CAN node.
- The custom **Revival Bed Node** is a permanent CAN node connected through the CEB; it also retains USB-C for first flash, recovery, bench diagnostics and optional alternate USB runtime operation.
- The custom **RASS CAN Node** is a permanent Klipper-compatible CAN node connected through the CEB for active spool/feed control and local RASS sensing. It may interface the physical RFID/NFC reader, but forwards only low-level reader observations; tag/vendor/material decoding runs on the Linux host (CB1 during bench work, CB2 in the final machine).
- Both Revival-designed CAN nodes — Bed Node and RASS Node — run **unmodified upstream Klipper MCU firmware**. Revival-specific semantics remain in normal configuration/macros or Linux-host software; private MCU firmware forks are not part of the production architecture.
- Both custom nodes must physically expose **every remaining electrically usable MCU pin** after baseline functions are assigned. Alternate SPI/I2C/UART/ADC/GPIO/PWM capabilities are documented per pin; BOOT/RESET/debug remain separately accessible; only pins with a documented hardware reason may remain unavailable.
- The finished bus must have exactly two 120-ohm terminations at its physical ends; jumper positions are to be recorded during commissioning.
- CAN uses a twisted differential pair and a documented shielding/ground strategy.

CAN does **not** carry bed-heater power, camera video, touchscreen video or mains control.

## EBB36 Gen2 toolhead node

The moving toolhead harness is reduced to 24 V, ground, CAN-H and CAN-L, plus any required shield/drain arrangement.

The frozen Generation 3 extrusion/probing direction is **BIGTREETECH EBB36 Gen2 + E3D Roto + Revo + BIGTREETECH Eddy Duo**, documented in [`../hardware/generation-3-extrusion-toolhead.md`](../hardware/generation-3-extrusion-toolhead.md). The machine is quality-first for PLA, with occasional ABS/ASA capability but no heated-chamber requirement.

The EBB36 Gen2 locally manages:

- extruder stepper motor/driver;
- hotend heater;
- hotend temperature sensor;
- hotend heatsink fan;
- part-cooling fan;
- third auxiliary fan/output if required;
- BIGTREETECH Eddy Duo probe/scanner interface;
- filament sensor interface if selected;
- toolhead work/status lighting;
- toolhead sensors.

## Revival Bed Node

The final Generation 3 bed uses a custom **Revival Bed Node**, documented in [`../hardware/generation-3-bed-node.md`](../hardware/generation-3-bed-node.md). The board is fixed in a printed enclosure on the rear cross-member of the historical lower frame; it is not carried by the moving bed.

The implementation is deliberately staged:

1. **Initial commissioning:** conventional separate wiring — bed thermistor to Manta, external MOSFET controlled from the main electronics, and a separate USB S2DW-class bed accelerometer.
2. **Final architecture:** CAN-connected custom bed MCU near the moving Y assembly, integrating bed thermistor acquisition, permanent bed accelerometer and local heater power-stage control. Normal runtime communication is through the CEB; USB-C remains available for first flash, recovery, bench diagnostics and optional alternate runtime operation.

The fixed/semi-fixed communication feed into the Bed Node is **CAN through the CEB**, plus the required local logic supply. USB-C is an additional service/fallback interface, not the normal production data path. Only the short Bed Node-to-bed harness is continuously flexed and carries heater power, thermistor and the remote moving IMU connection. Neither CAN nor USB carries heater power; the heater retains its dedicated fused 24 V high-current path.

The Bed Node is a normal secondary Klipper MCU. Beyond bed control, it is also the local acquisition hub for a moving-bed IMU, a chassis IMU on the fixed PCB and a remote frame-top IMU, plus RGB status lighting and electrical/thermal telemetry. Safety-critical bed protection remains independent of it: dedicated branch fuse and independent thermal fuse remain mandatory even after migration.

## Permanent accelerometers

Generation 3 uses **two permanently installed accelerometers** because X and Y are different moving masses on a bed-slinger.

### X / toolhead

Use the **LIS2DW associated with the EBB36 Gen2**. It remains permanently installed and is read through the toolhead MCU/CAN node.

### Y / bed

During initial commissioning, use a permanent/semi-permanent **BIGTREETECH S2DW V1.0 (RP2040 + LIS2DW)** or equivalent USB accelerometer rigidly mounted to the moving bed/Y-carriage assembly. In the final architecture, the Bed Node remains fixed and a tiny LIS2DW-class IMU daughterboard remains rigidly attached to the moving bed/carriage.

During the transitional S2DW stage, connection is **USB directly to the CB2**. In the final architecture the moving-bed IMU is only a tiny sensor daughterboard; the fixed Bed Node acquires it locally and communicates with Klipper over CAN through the CEB. No CAN MCU or USB electronics are added to the moving bed.

The bed sensor mount must be rigid, electrically isolated where required, clear of heater/insulation and replaceable without disturbing bed alignment. The final moving harness carries only the short remote-IMU connection and bed-local power/sensor wiring; it does not require the transitional S2DW USB cable.

Klipper configuration will expose separate toolhead/X and bed/Y accelerometers so resonance tests require no sensor relocation.

## Heated bed — original footprint, modern layered construction

The final bed keeps the **exact original heated-bed footprint and machine travel envelope**. The currently catalogued Y carriage is approximately 220 × 220 mm and the old removable mirrors are 200 × 200 mm, but final plate CAD must use measurements from the original heated-bed PCB itself. The rule is: **match the original bed; do not enlarge it**.

Final stack, top to bottom:

1. removable spring-steel build sheet;
2. PEI surface (smooth/textured sheets may be separate consumables);
3. high-temperature magnetic base;
4. precision aluminium plate matching the original bed footprint and mounting geometry;
5. custom 24 V silicone heater;
6. integrated bed temperature sensor;
7. independent thermal fuse physically coupled to the bed/heater assembly;
8. thin thermal insulation where clearance permits.

The bed system is fixed at **24 V**. Heater wattage is selected only after the original PCB is accurately measured; current target range is approximately **150–200 W**.

The Manta controls the bed but the high-current heater path uses a **dedicated external DC MOSFET/power stage**. The bed circuit gets its own fuse, suitable wiring/connectors and an independent thermal fuse effective even if Klipper, CB2, Manta MCU or MOSFET fails.

## Camera architecture

Camera integration is part of the Generation 3 concept. The primary camera selection is now frozen as the **Innomaker U30CAM-4K-S1**, using a Sony IMX415 STARVIS sensor and USB/UVC. The earlier CSI-first/model-open direction is obsolete for the main frame camera. Optical framing and clean mechanical integration remain to be validated on the rebuilt printer. See [`../hardware/generation-3-main-camera.md`](../hardware/generation-3-main-camera.md).

### Main frame camera

The baseline requirement is one **fixed camera mounted to the printer frame**, never to the moving bed or toolhead.

Frozen implementation:

- **Innomaker U30CAM-4K-S1 over USB/UVC** is the primary frame camera;
- it is intended to work first with the CB1 bench host and remain the same camera through the future CB2 or CM4 host migration;
- advertised headline modes are 3840 × 2160 at 30 fps and 1920 × 1080 at 60 fps; delivered-unit V4L2 modes and sustainable host performance must be bench-verified.

Requirements:

- fixed, stable view of the bed/nozzle work area;
- wide enough field of view to remain inside the original printer envelope where practical;
- integration with Crowsnest/Mainsail;
- suitable for live monitoring, project documentation and timelapse;
- custom ASA enclosure inspired by **late-1980s/1990s industrial CCTV/video-surveillance cameras**;
- no exposed modern camera PCB and no generic consumer-webcam appearance.

The sensor and interface are frozen. Final mount position, focus, framing and normal operating mode are selected after physical tests with the delivered U30CAM-4K-S1.

### Possible future upgrade — fixed nozzle camera

A second camera is explicitly documented as a **possible future upgrade**, not part of the frozen base build.

Concept:

- a very small camera fixed to the toolhead/nozzle assembly;
- optical axis arranged so the nozzle remains at a stable position in the image;
- intended especially for timelapses in which the nozzle appears fixed while the printed part/bed moves through the frame;
- same retro CCTV visual language, miniaturised for the toolhead rather than left as an exposed board.

The likely implementation is **USB/UVC**, which would require an additional moving USB connection to the toolhead. This is intentionally deferred because it affects moving-harness flexibility, bend life, strain relief, electromagnetic routing, toolhead mass and available USB topology.

The nozzle camera must not be allowed to compromise the primary 24 V + CAN toolhead harness. If later adopted, its USB routing will be designed and tested as a separate moving service, or replaced by another suitable camera transport if a cleaner solution exists at that time.

The nozzle camera is **not** carried over CAN.

## Lighting

### Frame work light

- 24 V diffused COB/LED strip integrated discreetly into the frame;
- neutral-to-warm white, approximately 3500–4000 K preferred;
- dimmed by a Manta-controlled MOSFET output;
- Klipper macros may set idle/heating/printing/completed brightness states.

### Toolhead work/status light

- driven from the EBB36 Gen2 lighting/RGB interface;
- white work light at the nozzle during printing;
- restrained status colours for heating/completed/error states;
- no permanent rainbow effects by default.

## Fan architecture

| Function | Controller | Requirement |
|---|---|---|
| Hotend heatsink fan | EBB36 Gen2 | 24 V, tachometer-capable preferred; RPM monitoring in Klipper |
| Part cooling | EBB36 Gen2 | 24 V PWM blower sized after duct/hotend design |
| Auxiliary toolhead fan | EBB36 Gen2 | reserved for second cooling/toolboard need |
| Electronics enclosure | Manta | one or more large, low-RPM, temperature-controlled fans |
| CB2 cooling | local/Manta | fitted only if thermal tests require it |

Electronics airflow must be designed through the enclosure rather than relying on several permanently fast small fans.

## Power architecture

Generation 3 is a **24 V DC machine**.

```text
230 V AC
   |
   +-- fused / switched / filtered mains entry
   +-- protective earth -> steel frame / required exposed conductive parts
   |
   v
24 V PSU
   |
   +-- fused branch -> Manta / CB2
   +-- fused branch -> external bed MOSFET -> silicone bed heater
   +-- fused branch -> EBB36 toolhead power/CAN harness
   +-- fused branch -> frame lighting / auxiliaries
```

The PSU family remains Mean Well 24 V. Exact continuous wattage is selected after final bed-heater and hotend power are frozen, with real operating margin rather than simply matching arithmetic peak load.

## Software responsibility split

```text
Slicer
  |
  v
Mainsail / Moonraker
  |
  v
Klipper host on CB2
  |
  +-- Manta M8P V2 MCU -> X / Y / Z0 / Z1 / bed / enclosure I/O
  +-- CAN -> CEB V1.0 CAN backbone/distribution
  |      +-- EBB36 Gen2 -> extruder / hotend / fans / LEDs / X accelerometer
  |      |      +-- CAN passthrough -> Eddy Duo (separate 5 V CAN MCU/node)
  |      +-- Revival Bed Node -> bed control / Y IMU / structural IMUs / telemetry
  |      |      +-- USB-C service/recovery/optional alternate runtime
  |      +-- RASS CAN Node -> feeder / spool assist / buffer / encoders / local feed sensing
  |             +-- RFID/NFC reader acquisition -> raw observations -> host decoder service
  +-- USB -> BTT S2DW -> transitional Y/bed accelerometer before Bed Node
  +-- CSI preferred or USB fallback -> fixed frame camera
  +-- future USB/other link -> optional nozzle camera
```

Final configuration, macros and calibration data must be versioned under `firmware/` rather than living only on printer storage.

## Revival Intelligence & Diagnostics

**Revival Intelligence & Diagnostics (RID)** is the Generation 3 supervisory-intelligence and diagnostic umbrella hosted primarily on the CB2. It provides a common framework for future pre-flight checks, maintenance history, condition monitoring, vision, anomaly capture, sensor fusion and diagnostic user experience.

The concept and subsystem boundary are documented in [`../hardware/generation-3-revival-intelligence-diagnostics.md`](../hardware/generation-3-revival-intelligence-diagnostics.md). The prioritised feature backlog remains in [`../hardware/generation-3-enhancement-candidates.md`](../hardware/generation-3-enhancement-candidates.md).

RID does **not** move deterministic motion/heater control away from Klipper/Manta/EBB36/Eddy and does not replace independent hardware safety. Individual RID features remain candidates until separately promoted.

The intended responsibility split is:

- CB2/RID: observation, correlation, history, vision, diagnostics, notifications and tested reversible high-level actions;
- Klipper/Manta/EBB36/Eddy: deterministic machine control and normal firmware protections;
- independent hardware: mains, over-current, protective-earth, thermal-fuse and emergency-energy-removal functions.

RID should be local-first and should reuse already-frozen data sources before new hardware is added.

## Safety boundaries

The following must remain effective independently of normal host communication:

- mains fuse/switching and protective earth;
- correctly rated wire/connectors and branch protection;
- heated-bed thermal fuse;
- physical strain relief on all moving harnesses;
- hardware over-current protection independent of CAN/Klipper.

Klipper heater checks, fan RPM monitoring, temperature limits and watchdog behaviour are additional protections, not substitutes for electrical protection.

## Frozen architectural decisions

- original flat steel frame, original M8/M10 threaded-rod base and original machine/bed envelope;
- commercial aluminium T-slot extrusion as the local X/Y MGN12 support structure, with exact 2020/2040-class sections deferred to measured CAD;
- Z MGN12 mounting hierarchy: direct to the steel frame when metrology permits, thin aluminium backing plate if required, and T-slot extrusion only when necessary;
- historical red-and-black machine identity: red printed mechanical/structural parts, black frame/rods, with no exact red shade requirement;
- 24 V final system;
- Manta M8P V2.0 + CB2 + TMC2209 controller architecture; Manta and 6× TMC2209 are already purchased, CB2 pending;
- Klipper + Moonraker + Mainsail + KlipperScreen + Crowsnest;
- HDMI5 5-inch touchscreen with retro enclosure/theme;
- dedicated small RASS/spool touchscreen for local material status and host-guarded filament LOAD/UNLOAD controls;
- CAN as the permanent internal Generation 3 communications backbone;
- CEB V1.0 CAN distribution/protection and backbone for toolhead, Bed Node and RASS CAN Node;
- EBB36 Gen2 toolhead node;
- E3D Roto + Revo direct-drive extrusion stack;
- BIGTREETECH Eddy Duo for fast/dense eddy-current bed-surface scanning as an independent 5 V CAN node downstream of the EBB36 Gen2 passthrough;
- permanent X/toolhead LIS2DW;
- staged Y/bed sensing: initial USB S2DW-class accelerometer, final custom Revival Bed Node over CAN through the CEB with USB-C retained for service/recovery and optional alternate runtime;
- Bed Node and RASS Node use unmodified upstream Klipper MCU firmware and expose every remaining electrically usable MCU pin after final pin allocation, with alternate peripheral capabilities documented;
- one fixed **Innomaker U30CAM-4K-S1 Sony IMX415 USB/UVC** frame camera as the frozen primary imaging device;
- retro CCTV/video-surveillance enclosure language for all cameras;
- 24 V dimmable frame light and toolhead work/status light;
- tachometer-monitored hotend cooling architecture;
- temperature-controlled electronics ventilation;
- layered original-footprint aluminium/silicone/magnetic/flexible-PEI bed;
- external bed MOSFET and independent thermal fuse;
- complete new wiring.

## Possible future upgrades

- fixed toolhead/nozzle camera for nozzle-centred timelapse, likely USB/UVC but intentionally not frozen;
- additional CAN nodes only where they solve a demonstrated wiring/sensing problem rather than merely because CAN is available.

## Component-level selections still open

These selections do not change the architecture and will be frozen after their mechanical interfaces are known:

- exact Roto/Revo SKU/revision, toolplate geometry and final cooling integration;
- exact Eddy Duo mount, offsets, connector pinout, physical CAN harness and calibration/thermal-compensation strategy;
- exact filament sensor;
- exact fan models and duct geometry;
- exact frame-light strip/diffuser;
- final aluminium bed thickness;
- final silicone-heater dimensions/wattage after measuring the original bed PCB;
- exact PSU wattage;
- connector families, wire gauges and harness routing;
- U30CAM-4K-S1 frame-camera mount position, framing/focus and validated normal runtime mode;
- optional nozzle-camera implementation, if the future upgrade is adopted.


## RID computation policy

RID remains a local-first supervisory subsystem, but **LLM inference is not required locally**.

The CB2 runs the deterministic/specialist RID stack: sensor acquisition, feature extraction, anomaly detection, lightweight ML/vision, history and sensor fusion.

Any LLM is optional and may run on:
- a local-network server; or
- a configured external provider.

The machine remains fully printable and diagnostically useful when no LLM provider is available.

A future higher-performance compute module is not required merely to host an LLM.
