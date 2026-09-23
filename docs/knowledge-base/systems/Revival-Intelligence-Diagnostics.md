---
type: system
area: intelligence-diagnostics
status: planned
phase: generation-3
priority: normal
generation: final
updated: 2026-09-23
---

# Revival Intelligence & Diagnostics

[Home](../Home.md) · [Systems](Systems.md) · [Current State](../project/Current-State.md)

**Revival Intelligence & Diagnostics (RID)** is the Generation 3 supervisory intelligence and diagnostic subsystem.

Its canonical source is [Revival Intelligence & Diagnostics](../../../hardware/generation-3-revival-intelligence-diagnostics.md). The detailed, prioritised candidate list is the [RID candidate backlog](../../../hardware/generation-3-enhancement-candidates.md).

## Responsibility split

RID is primarily hosted on the CB2 and may observe, analyse, record, notify and initiate validated reversible high-level actions. Motion/heater control remains with Klipper/Manta/EBB36/Eddy, while hazardous-energy protection remains independent hardware.

## Existing data sources

RID first reuses the fixed frame camera, permanent X/Y accelerometers, Klipper/Moonraker state, Manta/EBB36/Eddy status, fan RPM where available, smart-spool/RASS context when implemented and controllable lighting.

## Candidate domains

The backlog covers pre-flight/startup checks, maintenance history, thermal/resonance trends, fixed-camera inspection, anomaly evidence, health scoring, sensor fusion, diagnostic UI and selected minimal-hardware extensions.

Candidate inclusion is not implementation. Promotion requires the RID study protocol and a project decision.

## Autonomy boundary

RID uses R0–R3 for observe, inform, recommend and reversible action. Safety-critical energy control is outside RID software authority.

## Next study

The first recommended implementation candidate is **S01 automated pre-flight**, followed by low-complexity maintenance/history and startup-health functions.

[Firmware](Firmware.md) · [Electronics](Electronics.md) · [Safety](Safety.md)
