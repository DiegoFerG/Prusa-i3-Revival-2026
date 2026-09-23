# Generation 3 enhancement candidates

This document is the canonical backlog for non-frozen improvements to the Revival 2026 Generation 3 machine. It records candidate functions, their relative study priority and promotion history without silently turning ideas into requirements.

**Eddy Duo probing has already been promoted** into the frozen architecture; its current requirements belong to the [toolhead architecture](generation-3-extrusion-toolhead.md).

The objective is to improve reliability, print-failure detection, automatic preparation, diagnostics, maintenance visibility and operator safety while preserving the classic i3 character and avoiding complexity that does not earn its place.

## Evaluation rule

A candidate may be promoted into the frozen Generation 3 architecture only after the relevant integration, software support, failure modes, maintenance burden and safety implications have been reviewed.

The preferred design philosophy remains:

> mechanical correctness first, independent hardware safety second, software automation third.

Candidate status means **study later**, not purchase, installation or guaranteed implementation.

## Prioritisation model

Candidates are ordered primarily by **functional value**, using **implementation complexity as the tie-breaker**. The intent is to investigate high-value, low-complexity features first.

Scores are deliberately coarse and are only planning aids:

- **Functional value:** 5 = very high, 1 = marginal.
- **Complexity:** 1 = straightforward, 5 = substantial integration/research.
- **Hardware:** none means no hardware beyond the already frozen Generation 3 baseline; minimal means one small sensor/interface or similarly limited addition.
- Safety-critical functions are not allowed to depend solely on CB2/Linux/Klipper software even if they score highly.

The priority order may be revised after real commissioning data exists.

# A. Software-only candidates

These candidates require **no additional hardware beyond the frozen Generation 3 baseline**. Vision candidates assume the already-frozen fixed frame camera is installed. Condition-monitoring candidates use the already-frozen permanent X/toolhead and Y/bed accelerometers plus normal Klipper/Manta/EBB telemetry.

| Priority | Candidate | Value | Complexity | Main benefit |
| ---: | --- | :---: | :---: | --- |
| S01 | Automated pre-flight / pre-print self-check | 5 | 2 | Prevent avoidable starts by checking homing, Z alignment, Eddy, temperatures, fans, spool state and available validated sensors before printing |
| S02 | Maintenance counters and service history | 5 | 2 | Track printer/print hours, heater cycles, fan runtime, nozzle throughput, lubrication and service events |
| S03 | Startup subsystem health check | 4 | 2 | Verify expected Klipper MCUs, CAN/USB nodes, sensors, cameras and sane temperature readings before use |
| S04 | Smart notifications and fault escalation | 4 | 1 | Send useful alerts for intervention, completion or abnormal state without adding local hardware |
| S05 | Post-print report and diagnostic event log | 4 | 2 | Record job result, temperatures, duration, material, warnings, calibration state and selected images/telemetry |
| S06 | Heater warm-up / thermal-response trend analysis | 4 | 2 | Detect gradual changes in bed/hotend heating behaviour using existing temperature and heater-duty data |
| S07 | Resonance and mechanical-condition trend tracking | 5 | 3 | Compare permanent accelerometer measurements over time for clues about belts, fasteners, rails and structural changes |
| S08 | Automated belt-frequency / tension trend check | 4 | 3 | Reuse the permanent accelerometers to compare belt-related response against the machine's own baseline |
| S09 | Camera-based general print-failure detection | 5 | 3 | Detect likely spaghetti, detached parts, gross layer shifts or abnormal print appearance using the fixed camera |
| S10 | First-layer visual inspection | 5 | 4 | Combine camera evidence with Eddy/Z state to detect poor adhesion, missing extrusion or dragged first-layer lines |
| S11 | Machine-health baseline and condition score | 4 | 3 | Summarise trends from resonance, thermal response, failure history and maintenance state into actionable diagnostics |
| S12 | Sensor-fusion fault confidence engine | 5 | 4 | Combine camera, accelerometers, temperatures, Klipper state, filament data when available and other validated telemetry instead of trusting one sensor |
| S13 | Automatic anomaly snapshot / local black-box capture | 4 | 3 | Preserve images and recent telemetry around pauses, errors or detected anomalies for later diagnosis |
| S14 | Visual fiducial / homing geometry sanity check | 4 | 4 | Use fixed-camera reference marks to detect gross pose, frame or homing discrepancies independently of commanded coordinates |
| S15 | Expected-geometry / G-code versus camera comparison | 4 | 5 | Compare what should exist at a layer/position with what the fixed camera observes to detect geometric deviations |
| S16 | Automated maintenance recommendations | 4 | 4 | Convert measured trends and service history into specific prompts such as inspect Y belt or re-run resonance baseline |
| S17 | State-aware frame/toolhead lighting | 3 | 1 | Reuse the frozen controllable lights for inspection brightness, camera capture and restrained print/error/completion signalling |
| S18 | Local digital-twin / diagnostic dashboard | 3 | 3 | Present axes, temperatures, sensors, maintenance state, current job and anomaly history in one CB2-hosted view |

## Software-candidate notes

### S01 — Automated pre-flight

The target is an orchestrated Klipper/Moonraker workflow, not one giant opaque macro. It should only test hardware that actually exists and has passed commissioning.

Possible sequence:

```text
configuration/version sanity
        |
MCU / CAN / USB node presence
        |
temperature plausibility
        |
home axes
        |
Z gantry alignment
        |
Eddy health + scan/reference
        |
fan checks where RPM feedback exists
        |
spool/material checks where available
        |
optional nozzle-cleaning workflow
        |
READY TO PRINT
```

Optional/non-critical telemetry faults should degrade gracefully rather than creating an unsafe or unrecoverable state.

### S02 / S07 / S08 / S11 / S15 — condition history

The Revival should be compared primarily against **its own commissioned baseline**. A resonance shift or thermal trend is diagnostic evidence, not automatic proof of one specific fault.

Useful retained history may include:

- powered and printing hours;
- heater hours/cycles and warm-up curves;
- fan runtime/RPM events where feedback exists;
- filament throughput by nozzle/material;
- nozzle install/change date;
- rail lubrication/service date;
- belt checks;
- X/Y resonance measurements;
- PID/calibration history;
- jam/run-out/failed-print events;
- user-confirmed maintenance actions.

Data should remain locally exportable. Important configuration/calibration records should be versioned where practical.

### S09 / S10 / S12 / S14 — vision and sensor fusion

The first study should use the already-planned fixed frame camera before adding a second moving camera.

Possible visual states include:

- normal print;
- detached or shifted object;
- spaghetti-like extrusion;
- major layer-shift suspicion;
- first-layer adhesion failure;
- no visible extrusion where extrusion is expected;
- material accumulation/blob suspicion.

Any automatic pause policy must be conservative, logged and reversible. Vision must not become a safety system for heaters or mains power.

Local CB2 inference is desirable if performance and software support prove adequate, but candidate status does not freeze an AI runtime, model family or cloud dependency.

### S14 — visual fiducial / homing sanity check

Simple fixed reference marks on the frame/bed may allow the baseline camera to verify that the observed machine pose remains broadly consistent with Klipper's expected homed geometry. This is a diagnostic cross-check, not closed-loop axis control and not a replacement for endstops/probing.

### S17 — state-aware lighting

The frozen frame and toolhead lighting can be software-orchestrated without new hardware. Candidate behaviours include:

- consistent high-brightness illumination during camera inspection;
- lower print brightness;
- nozzle-focused light during first-layer analysis;
- restrained completion/warning/error indication;
- automatic restoration of normal light state after diagnostic capture.

### S18 — local digital twin / diagnostic dashboard

A CB2-hosted dashboard may combine current machine state with historical context: commanded/actual-known positions, temperatures, MCU/CAN node status, spool identity/estimate, camera state, resonance history, maintenance counters and active warnings. It is an operator/diagnostic view, not a second motion controller.

# B. Minimal-hardware or high-impact hardware candidates

These additions are candidates because they either require very little extra hardware or could provide a sufficiently large reliability/safety/diagnostic improvement to justify dedicated study.

| Priority | Candidate | Value | Complexity | Added hardware / reason to study |
| ---: | --- | :---: | :---: | --- |
| H01 | Filament-motion / jam sensor | 5 | 2 | Small encoder/pulse sensor; directly detects commanded extrusion without actual filament motion |
| H02 | Hardware emergency stop plus essential physical controls | 5 | 3 | High safety/operability value; E-stop must act independently of CB2/Linux/Klipper |
| H03 | Nozzle cleaning / purge station | 5 | 3 | Small mechanical station; improves probe/reference reliability and unattended preparation |
| H04 | DC power/energy monitoring | 4 | 2 | Small current/voltage monitor; enables PSU/heater diagnostics and energy history |
| H05 | Ambient temperature/humidity sensor | 3 | 1 | Very small sensor; useful context for print records, materials and diagnostics |
| H06 | Dedicated abnormal-air/smoke monitoring | 4 | 2 | Small independent sensor path for warning/diagnostics; never substitutes for electrical/thermal protection |
| H07 | Additional motor/electronics temperature sensing | 3 | 2 | Small sensors can identify overheating or changing operating conditions |
| H08 | Build-sheet identification | 3 | 2 | Small tag/sensor scheme could confirm the installed PEI/surface profile before a job starts |
| H09 | Audible local alert / buzzer | 2 | 1 | Minimal hardware for intervention/error/completion alerts when the operator is near the printer |
| H10 | Nozzle/toolhead camera | 4 | 3 | Significant first-layer/nozzle visibility; moving USB/power, mass and strain relief require study |
| H11 | CB2 hold-up / graceful-shutdown power support | 4 | 3 | Small UPS/supercapacitor-class subsystem could preserve logs and shut Linux down cleanly after input loss |
| H12 | Independent nozzle/contact Z-reference | 5 | 4 | Additional physical reference could cross-check/calibrate the Eddy-to-nozzle relationship if the benefit justifies mechanics and wiring |
| H13 | Independent axis-position verification / encoders | 5 | 5 | Larger integration burden but potentially strong detection of lost motion or true-position errors |
| H14 | Acoustic condition monitoring microphone | 2 | 2 | Very small hardware addition; experimental detection of fan/bearing/periodic mechanical changes |
| H15 | Low-resolution thermal imaging | 3 | 4 | Potential heater/bed/nozzle diagnostic value, but cost, mounting and interpretation require proof before promotion |

## Hardware-candidate notes

### H01 — filament motion / jam detection

The sensor should verify that filament is **actually moving**, rather than only detecting presence.

Target faults:

- run-out;
- filament break;
- extruder grinding/slipping;
- blocked or partially blocked hotend;
- spool/feed-path obstruction.

A compact encoder/wheel-style Klipper-compatible sensor is the reference concept. Exact hardware and mounting remain open and must not add excessive drag, especially for flexible filament.

### H02 — hardware emergency stop and controls

A physical panel may include pause/resume/function controls, but the emergency-stop function is different: if adopted, hazardous actuator/heater energy must be removable without relying on Linux, Klipper, Moonraker, CAN or a software macro.

The E-stop does not replace mains fusing, protective earth, branch fusing, bed thermal fuse or firmware heater protections.

### H03 — nozzle cleaning / purge station

Potential functions:

- purge position;
- heat-resistant brush/wiper;
- controlled wipe sequence;
- removable debris collection;
- optional purge catcher.

It should remain within or very close to the historical envelope and must not contaminate guides/electronics or compromise usable travel.

### H04 — electrical power and health monitoring

Candidate measurements:

- 24 V bus voltage;
- total DC current;
- selected branch current if useful;
- power/energy;
- heater warm-up behaviour;
- voltage sag or abnormal trends.

Electrical telemetry is diagnostic only and never replaces fuses, rated wiring/connectors, thermal protection or protective earth.

### H06 — abnormal-air/smoke monitoring

If studied, this is an additional warning layer, not the primary fire-safety system. Sensor placement, contamination, false-positive behaviour and independent response paths must be reviewed before any promotion.

### H08 — nozzle/toolhead camera

The baseline fixed frame camera should be exhausted first. A second moving camera is only justified if it materially improves nozzle/first-layer inspection.

The study must include:

- moving cable bend life;
- strain relief;
- USB topology/bandwidth;
- toolhead mass;
- EMI/routing alongside CAN and 24 V;
- field of view and lighting.

### H10 — independent axis-position verification

Linear/rotary encoders could provide true-motion verification, but this is deliberately low in the initial study order because it adds mechanics, wiring, calibration and software complexity. It should only advance if tests show that the diagnostic value justifies the integration cost.

### H08 — build-sheet identification

A small coded tag, RFID/NFC marker or other robust identification method could let pre-flight logic confirm that the selected print profile matches the physically installed sheet/surface. The mechanism must not interfere with Eddy probing or the magnetic build surface.

### H09 — audible local alert

A simple buzzer/sounder is only a candidate because the hardware burden is negligible. It should use restrained, distinct patterns and remain user-disableable; remote notifications are preferred for richer information.

### H12 — independent nozzle/contact Z-reference

This candidate exists to test whether a second physical reference materially improves long-term Eddy/nozzle offset confidence. It must not be added merely for redundancy. The study should first establish whether normal Eddy thermal calibration and nozzle-cleaning procedures already meet repeatability requirements.

# C. Candidate study order

The recommended first pass is:

1. S01 pre-flight checks;
2. S02 maintenance/service history;
3. S03 startup subsystem health;
4. S04 notifications;
5. S05 post-print/event reporting;
6. S06 thermal-response trends;
7. S17 state-aware lighting;
8. H01 filament-motion sensor;
9. S07/S08 resonance and belt trends;
10. H05 ambient temperature/humidity;
11. H02 hardware emergency stop / essential controls;
12. H03 nozzle cleaning;
13. S09 fixed-camera failure detection;
14. H04 power monitoring;
15. S10 first-layer vision;
16. S11/S12 condition scoring and sensor fusion;
17. S13/S14 diagnostic capture and visual geometry cross-check;
18. H06/H07/H08 low-burden environmental, temperature and sheet-ID studies;
19. S15/S16/S18 advanced geometry comparison, maintenance advice and digital-twin UI;
20. H10–H15 higher-integration hardware candidates in table order.

This is a **study order**, not a purchasing order and not an architecture commitment.

# D. Study protocol

Each candidate should be reviewed independently before promotion. Record at least:

1. exact problem being solved;
2. existing baseline hardware/data it can reuse;
3. required new hardware, if any;
4. software integration path;
5. expected benefit and measurable success criteria;
6. false-positive / false-negative behaviour where relevant;
7. failure mode if the feature itself stops working;
8. safety implications;
9. maintenance burden;
10. mechanical envelope, mass and wiring impact;
11. prototype result;
12. promote / defer / reject outcome with rationale.

A candidate that can be implemented in software should normally be prototyped before adding hardware intended to solve the same problem.

# E. Promoted candidate history

## Eddy-current Z probe / fast bed scanning — promoted

Eddy-current probing has been promoted into the frozen Generation 3 architecture.

The selected direction is **BIGTREETECH Eddy Duo** integrated with the frozen E3D Roto + Revo toolhead stack.

Remaining work is implementation engineering rather than candidate selection:

- final mount geometry and adjustability;
- X/Y/Z probe offsets;
- connector pinout and physical harness for the frozen independent 5 V CAN node downstream of the EBB36 Gen2 passthrough;
- thermal calibration/compensation;
- repeatability validation on the final spring-steel/magnetic bed;
- interaction with nozzle cleaning and the final Z-reference workflow.

Canonical source: [Generation 3 extrusion/toolhead target](generation-3-extrusion-toolhead.md).
