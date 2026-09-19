---
type: system
area: extrusion
status: in-progress
phase: stage-02
priority: high
generation: original
updated: 2026-09-19
---

# Extrusion

The [hardware baseline](../../../hardware/README.md) identifies a Wade/Greg's-Wade-family geared extruder and a legacy E3D-family groove-mount hotend for 3 mm / 2.85 mm stock. The hotend is probably V5-era; its exact revision is deliberately unconfirmed.

## Current boundaries

[Manual Stage H](../build/Phase-H.md) describes mechanical reconstruction only. The heater cartridge remains captive because the retaining screw head is damaged; the source manual defers destructive removal. Thermistor type requires measurement. No heater is energized during Stage 02.

Assembly photographs currently indexed for Stage 02 reach manual Stage G. The index does not establish completion of Stage H or a working extrusion system. See the [reassembly evidence index](../../../photos/03-reassembly/INDEX.md).

## Later work

[Roadmap Stage 06](../../ROADMAP.md) restores or modularly rebuilds legacy extrusion; Stage 09 provides the later 1.75 mm conversion. The [Generation 3 target BOM](../../../hardware/generation-3-target-bom.md) leaves the exact direct-drive extruder and hotend open. The toolhead node architecture is frozen separately in the [final-build architecture](../../final-build-architecture.md).

Filament-motion/jam detection and a nozzle cleaning/purge station are [Generation 3 candidates](../../../hardware/generation-3-enhancement-candidates.md). Their sensor, mounting and relationship to the final probe/toolhead require evaluation before adoption.

[Filament system](Filament-System.md) · [Electronics](Electronics.md) · [Safety](Safety.md) · [Systems](Systems.md)
