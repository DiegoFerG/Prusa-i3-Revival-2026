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

## CAN bus

CAN is a permanent internal bus in Generation 3, used where it reduces moving wiring and improves modularity.

- Manta M8P V2.0 provides the primary CAN interface.
- **BIGTREETECH CEB V1.0** is the protected CAN distribution/breakout point in the electronics bay.
- **BIGTREETECH EBB36 Gen2** is the permanent toolhead CAN node.
- The finished bus must have exactly two 120-ohm terminations at its physical ends; jumper positions are to be recorded during commissioning.
- CAN uses a twisted differential pair and a documented shielding/ground strategy.

CAN does **not** carry bed-heater power, camera video, touchscreen video or mains control.

## EBB36 Gen2 toolhead node

The moving toolhead harness is reduced to 24 V, ground, CAN-H and CAN-L, plus any required shield/drain arrangement.

The frozen Generation 3 extrusion/probing direction is **E3D Roto + Revo + BIGTREETECH Eddy Duo**, documented in [`../hardware/generation-3-extrusion-toolhead.md`](../hardware/generation-3-extrusion-toolhead.md). The machine is quality-first for PLA, with occasional ABS/ASA capability but no heated-chamber requirement.

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

## Permanent accelerometers

Generation 3 uses **two permanently installed accelerometers** because X and Y are different moving masses on a bed-slinger.

### X / toolhead

Use the **LIS2DW associated with the EBB36 Gen2**. It remains permanently installed and is read through the toolhead MCU/CAN node.

### Y / bed

Use a permanent **BIGTREETECH S2DW V1.0 (RP2040 + LIS2DW)** rigidly mounted to the moving bed/Y-carriage assembly.

Connection: **USB directly to the CB2**, not another CAN toolboard. This avoids adding unnecessary mass and electronics under the moving bed while still providing an independent Klipper MCU for the Y sensor.

The bed sensor mount must be rigid, electrically isolated where required, clear of heater/insulation and replaceable without disturbing bed alignment. Its USB cable is part of the bed moving harness and must have proper strain relief.

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

Camera integration is part of the Generation 3 concept, but the **camera model and physical data interface are deliberately not frozen yet**. Optical framing and clean mechanical integration take priority over forcing a particular interface.

### Main frame camera

The baseline requirement is one **fixed camera mounted to the printer frame**, never to the moving bed or toolhead.

Preferred implementation order:

1. **CSI/MIPI camera to the CB2** if a practical ribbon length and routing can reach the selected frame position cleanly;
2. migrate to a **USB UVC camera** if CSI ribbon routing proves too restrictive, fragile or visually intrusive.

Requirements common to either interface:

- fixed, stable view of the bed/nozzle work area;
- wide enough field of view to remain inside the original printer envelope where practical;
- integration with Crowsnest/Mainsail;
- suitable for live monitoring, project documentation and timelapse;
- custom ASA enclosure inspired by **late-1980s/1990s industrial CCTV/video-surveillance cameras**;
- no exposed modern camera PCB and no generic consumer-webcam appearance.

The final sensor, lens/FOV, CSI cable length or USB camera are selected only after physical framing mock-ups on the rebuilt printer.

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
  +-- CAN -> EBB36 Gen2 -> extruder / hotend / fans / probe / LEDs / X accelerometer
  +-- USB -> BTT S2DW -> permanent Y/bed accelerometer
  +-- CSI preferred or USB fallback -> fixed frame camera
  +-- future USB/other link -> optional nozzle camera
```

Final configuration, macros and calibration data must be versioned under `firmware/` rather than living only on printer storage.

## Safety boundaries

The following must remain effective independently of normal host communication:

- mains fuse/switching and protective earth;
- correctly rated wire/connectors and branch protection;
- heated-bed thermal fuse;
- physical strain relief on all moving harnesses;
- hardware over-current protection independent of CAN/Klipper.

Klipper heater checks, fan RPM monitoring, temperature limits and watchdog behaviour are additional protections, not substitutes for electrical protection.

## Frozen architectural decisions

- original frame and original machine/bed envelope;
- historical red-and-black machine identity: red printed mechanical/structural parts, black frame/rods, with no exact red shade requirement;
- 24 V final system;
- Manta M8P V2.0 + CB2 + TMC2209 controller architecture; Manta and 6× TMC2209 are already purchased, CB2 pending;
- Klipper + Moonraker + Mainsail + KlipperScreen + Crowsnest;
- HDMI5 5-inch touchscreen with retro enclosure/theme;
- CAN as permanent toolhead bus;
- CEB V1.0 CAN distribution/protection;
- EBB36 Gen2 toolhead node;
- E3D Roto + Revo direct-drive extrusion stack;
- BIGTREETECH Eddy Duo for fast/dense eddy-current bed-surface scanning as an independent 5 V CAN node downstream of the EBB36 Gen2 passthrough;
- permanent X/toolhead LIS2DW;
- permanent Y/bed BTT S2DW/LIS2DW over USB;
- one fixed frame camera as part of the final concept, with **CSI preferred and USB permitted**; exact model/interface remains open;
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
- exact Eddy Duo mount, offsets, connection mode and calibration/thermal-compensation strategy;
- exact filament sensor;
- exact fan models and duct geometry;
- exact frame-light strip/diffuser;
- final aluminium bed thickness;
- final silicone-heater dimensions/wattage after measuring the original bed PCB;
- exact PSU wattage;
- connector families, wire gauges and harness routing;
- frame-camera sensor/lens/FOV and final CSI-versus-USB choice;
- optional nozzle-camera implementation, if the future upgrade is adopted.
