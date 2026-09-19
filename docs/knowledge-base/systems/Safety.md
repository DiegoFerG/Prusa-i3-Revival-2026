---
type: system
area: safety
status: active
phase: stage-02
priority: high
updated: 2026-09-19
---

# Safety

## Current Stage 02 boundary

The [Stage 02 scope](../../02-reassembly/README.md) and [original reassembly manual](../../02-reassembly/original-reassembly-manual.md) define an unpowered mechanical reconstruction. No mains-powered component is energized in this stage. Historical electronics may be placed mechanically; the old mixed harness remains archival evidence.

The [hardware baseline](../../../hardware/README.md) explicitly requires separate electrical/safety inspection before commissioning. An intact appearance or a photograph does not constitute electrical clearance. The manual's final mechanical gate must be recorded separately from evidence of assembly progress.

## Generation 3 requirements

The [final-build architecture](../../final-build-architecture.md) requires new wiring and protections that remain effective independently of Linux, Klipper or CAN, including mains protection and protective earth, suitable conductors/connectors and branch protection, an independent bed thermal fuse and strain relief. Its software heater checks and watchdogs are supplementary protections.

Detailed ratings, wiring diagrams and commissioning records belong in the canonical hardware and firmware documentation as they are developed. This page is an index to existing project requirements, not a commissioning approval.

The [enhancement register](../../../hardware/generation-3-enhancement-candidates.md) treats a hardware emergency stop as a high-priority safety-design candidate, with power-cut topology still open. Its specified independence from host software does not establish that it has been implemented. Proposed electrical telemetry remains diagnostic, and automated checks await validated hardware. The [smart-spool requirements](../../../hardware/generation-3-smart-spool-system.md) preserve manual fallback and prohibit silent replacement of safety-critical settings by tag data.

[Build](../build/Build.md) · [Electronics](Electronics.md) · [Heated bed](Heated-Bed.md) · [Open issues](../project/Open-Issues.md) · [Systems](Systems.md)
