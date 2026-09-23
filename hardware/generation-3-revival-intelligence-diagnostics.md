# Revival Intelligence & Diagnostics

> **Revival Intelligence & Diagnostics (RID)** is the Generation 3 supervisory-intelligence and diagnostic concept for Prusa i3 Revival 2026.

RID groups the machine's software intelligence, condition monitoring, vision, diagnostics, maintenance history and selected low-burden sensor extensions under one coherent subsystem.

The intent is not to turn the printer into an autonomous black box. RID should make the Revival easier to trust, inspect, maintain and diagnose while preserving the separation between deterministic machine control and supervisory software.

Individual RID features remain **candidates unless explicitly promoted elsewhere**. The concept, responsibilities and evaluation model are documented here; the prioritised feature backlog lives in [generation-3-enhancement-candidates.md](generation-3-enhancement-candidates.md).

## Core principle

RID follows a strict responsibility split:

```text
                 REVIVAL INTELLIGENCE & DIAGNOSTICS
                              |
                              v
                     CB2 supervisory layer
            observation / analysis / history / UI
                              |
         +--------------------+--------------------+
         |                    |                    |
         v                    v                    v
   Moonraker/Klipper     camera / vision      local services
   state + telemetry     and inspection       and databases
         |                    |                    |
         +--------------------+--------------------+
                              |
                              v
                     recommendations /
                   reversible high-level actions
                              |
                              v
                    Klipper / Moonraker API
                              |
                              v
                    Manta / EBB36 / Eddy
                 deterministic machine control
```

The CB2 may observe, correlate, record, advise and initiate **reversible high-level actions** such as pausing a print when confidence and policy permit.

The CB2 must not become the sole safety layer for mains power, heaters, over-current protection, protective earth, thermal fusing or other hazards that require independent protection.

## Functional layers

RID is organised into five layers:

1. **Observe** — collect Klipper/Moonraker state, temperatures, camera images, accelerometers, Eddy information, fan RPM and later promoted sensor data.
2. **Understand** — compare behaviour with the Revival's own commissioned baselines, detect trends and correlate independent signals.
3. **Decide** — classify normal, informational, maintenance, warning or intervention states with explainable evidence where practical.
4. **Act** — notify, log, capture evidence, request confirmation, run diagnostics or perform a validated reversible action such as pause.
5. **Learn and record** — retain service history, resonance trends, warm-up behaviour, print outcomes, anomaly evidence and user-confirmed diagnoses.

The Revival should primarily be compared with **its own known-good commissioned baseline**, not generic fleet assumptions.

## Baseline data already available

RID is designed first around hardware already frozen for Generation 3.

| Existing source | RID use |
| --- | --- |
| CB2 + Klipper/Moonraker | orchestration, state, history, local services and UI |
| Manta M8P V2.0 | axis/bed/enclosure state exposed through Klipper |
| EBB36 Gen2 | toolhead state, local sensing and fan/heater data |
| Eddy Duo | bed scan/reference information and diagnostic context |
| Fixed frame camera | monitoring, visual inspection and future machine vision |
| X/toolhead LIS2DW | resonance and toolhead-condition history |
| Y/bed BTT S2DW/LIS2DW | bed/Y resonance and condition history |
| Fan RPM where available | cooling-health diagnostics |
| Smart-spool/RASS data when implemented | material identity, remaining-mass and feed-state context |
| Frame/toolhead lighting | repeatable inspection illumination and state signalling |

**RID rule:** prototype software with existing data before adding hardware intended to solve the same problem.

## Functional domains

### Pre-flight and readiness

Candidate functions include configuration/version checks, MCU/CAN/USB presence, temperature plausibility, homing, Z alignment, Eddy health, fan checks, spool/material checks and integration with any later-promoted nozzle cleaning.

### Vision and print inspection

The fixed frame camera is the first vision source. Candidates include general print-failure detection, first-layer inspection, detached-part/gross-shift detection, abnormal extrusion suspicion, visual fiducials, anomaly snapshots and expected-geometry/G-code versus image comparison.

A nozzle/toolhead camera remains a separate hardware candidate and should only be added if the fixed camera cannot provide enough value.

### Mechanical condition monitoring

Permanent accelerometers may support resonance trends, belt-frequency/tension trends, loose-fastener clues, rail/carriage degradation clues and before/after maintenance comparison. These are diagnostic clues, not proof of one specific fault.

### Thermal and electrical diagnostics

Software can track hotend/bed warm-up curves, heater duty versus response, overshoot/settling and long-term thermal changes. Optional electrical monitoring hardware may later add voltage, current, power and energy.

### Maintenance intelligence

RID may track powered hours, print hours, heater cycles, fan runtime, nozzle install date/throughput, lubrication/service dates, calibration history, failure history and user-confirmed maintenance actions.

### Sensor fusion

Later RID work may combine camera evidence, accelerometers, temperatures, heater behaviour, fan RPM, spool/feed data, print/G-code state and promoted sensors. The goal is higher confidence through independent evidence, not duplication for its own sake.

### Diagnostic UX

RID should fit the Revival's retro-industrial language: concise pre-flight state, machine-health view, warnings with evidence, maintenance timeline, diagnostic history, local dashboard/digital-twin candidate, restrained lighting and remote notification.

## Data model

RID is intended to be **local-first**:

- machine history stored locally on the CB2;
- exportable documented data formats;
- important configuration/calibration artifacts versioned in the repository where practical;
- no mandatory cloud dependency for core diagnostics;
- optional external services only when they add clear value and can be disabled;
- anomaly context retained long enough for diagnosis without unnecessary indefinite recording.

Exact database/schema choices remain open.

## Autonomy levels

| Level | Behaviour | Example |
| --- | --- | --- |
| R0 | Observe only | record resonance trend |
| R1 | Inform | notify that warm-up time has degraded |
| R2 | Recommend | suggest checking Y-belt tension |
| R3 | Reversible action | pause after a validated high-confidence anomaly |
| R4 | Safety-critical energy control | **outside RID software authority**; independent hardware/protection required |

A promoted feature may be limited to a lower level even if it is technically capable of more.

## Candidate groups

The detailed priorities and scores are maintained in the [RID candidate backlog](generation-3-enhancement-candidates.md).

Current families are:

- **Software-only:** pre-flight, service history, subsystem-health checks, notifications, reports, thermal trends, resonance/belt trends, fixed-camera failure detection, first-layer vision, health scoring, sensor fusion, black-box capture, visual geometry checks, maintenance recommendations, state-aware lighting and diagnostic dashboard.
- **Minimal-hardware/high-impact:** filament-motion sensing, hardware emergency stop/controls, nozzle cleaning, DC power monitoring, ambient/abnormal-air sensing, additional temperature sensing, build-sheet identification, audible alerts, nozzle camera, CB2 graceful-shutdown support, independent Z reference, axis encoders, acoustic monitoring and low-resolution thermal imaging.

Candidate inclusion does not freeze a component, purchase or implementation.

## Moonshot research tier

RID also maintains a deliberately separate **Moonshot** tier for ideas whose research value may be high but whose expected path to the production Revival is very weak.

Moonshots:

- are assigned IDs `M01...`;
- are recorded with a **production score of 1/5** by default;
- do not enter the normal S/H study order;
- must not impose hardware, software, packaging or safety requirements on the production machine;
- are revisited only after the standard RID baseline is stable or when a practical candidate produces a clear enabling result;
- may be decomposed into smaller normal candidates if a realistic subset becomes feasible.

The current Moonshot set includes in-situ metrology, autonomous recovery, real-time process adaptation, full structural fingerprinting, self-calibrating geometry, nozzle-wear metrology, closed-loop extrusion supervision, causal diagnostics, self-experimentation, per-layer quality mapping, remaining-useful-life prediction, collision prediction, autonomous material calibration, full forensic recording and cross-print self-learning.

The canonical list and scores are maintained in the [RID candidate backlog](generation-3-enhancement-candidates.md#e-rid-moonshots--experimental--very-low-production-score).

## Candidate study protocol

Every RID candidate should record:

1. problem being solved;
2. baseline data/hardware reused;
3. additional hardware required, if any;
4. software integration path;
5. measurable success criteria;
6. false-positive / false-negative behaviour where relevant;
7. failure mode of the RID feature itself;
8. maximum autonomy level;
9. safety implications;
10. maintenance burden;
11. mechanical/wiring/mass impact;
12. prototype result;
13. promote / defer / reject decision with rationale.

## Promotion rules

A RID feature becomes part of the frozen Generation 3 architecture only through an explicit project decision and update to the relevant authoritative subsystem documents.

Promotion should establish demonstrated benefit, justified complexity, graceful failure, understandable operator behaviour, independent safety, reproducibility/maintainability and any accepted external dependency.

## Relationship to existing subsystems

RID consumes information from components selected for other primary reasons but does not redefine their responsibilities.

- Eddy Duo remains the frozen bed-scan/probe architecture; RID may use its results diagnostically.
- Permanent accelerometers remain available for Klipper resonance work; RID may compare results over time.
- The fixed frame camera remains part of the Generation 3 concept; RID gives it diagnostic/vision roles beyond monitoring.
- Smart-spool and RASS remain their own subsystems; RID may correlate their data after implementation.

## Safety boundary

RID is an **advisory and supervisory subsystem**. It must never be the only mechanism preventing or mitigating electrical over-current, loss of protective earth, bed over-temperature, heater runaway, hazardous mains conditions or emergency-stop energy removal.

Independent hardware protections and Klipper's normal heater/watchdog protections remain mandatory regardless of RID state.

## Current status

- RID concept and subsystem boundary: **documented**.
- Candidate-governance model: **established**.
- Individual software/hardware candidates: **not promoted unless separately recorded**.
- First recommended implementation study: **S01 automated pre-flight**, followed by low-complexity maintenance and health-history functions.
