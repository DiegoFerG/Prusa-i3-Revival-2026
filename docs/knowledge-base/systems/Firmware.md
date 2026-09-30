---
type: system
area: firmware
status: planned
phase: stage-07
priority: normal
updated: 2026-09-30
---

# Firmware

The current [firmware directory](../../../firmware/README.md) is a placeholder for legacy 3 mm and future 1.75 mm configurations. No commissioned configuration is established by that placeholder.

[Roadmap Stage 07](../../ROADMAP.md) covers configuration, electrical checks, motion and endstop tests, heater safety, PID tuning, calibration and first controlled prints. The current Stage 02 reconstruction is unpowered.

## Future software architecture

The [Generation 3 architecture](../../final-build-architecture.md) freezes Klipper on CB2 with Moonraker, Mainsail, KlipperScreen and Crowsnest. CB2 is not yet purchased; until it is available, a temporary Linux PC/Raspberry Pi may run the Klipper host and connect to the Manta M8P V2.0 by USB for bench testing without changing the final architecture. Manta manages machine axes and enclosure/bed I/O; EBB36 manages local toolhead functions; Eddy Duo is a separate 5 V CAN MCU/node downstream of the EBB36 passthrough; the permanent bed accelerometer connects over USB.

Final configuration, macros and calibration data must be versioned under `firmware/`. The temporary [Generation 3 electronics bench-test pack](../../../hardware/bench-tests/generation-3-electronics/README.md) intentionally keeps its disposable acceptance-test templates beside the hardware procedure; they are not commissioned printer configuration. Any future files should identify the machine generation and actual hardware they were validated against. The architecture is a target, not evidence that this software is already deployed.

## Revival Bed Node integration

The custom Bed Node is treated as an ordinary secondary Klipper MCU over USB.

Conceptual structure:

```ini
[mcu bed]
serial: /dev/serial/by-id/<REVIVAL_BED_NODE_ID>

[heater_bed]
heater_pin: bed:<HEATER_GATE_PIN>
sensor_pin: bed:<BED_THERMISTOR_PIN>
sensor_type: <FINAL_SENSOR_TYPE>
```

The remote moving Y accelerometer is connected electrically to the fixed `bed:` MCU and is defined as a sensor on that MCU for Y resonance measurements.

Exact pins and syntax belong to the future released PCB/configuration and must be validated against the Klipper version used at commissioning.

### Custom-board firmware build and first flash

The Revival Bed Node should use an MCU supported by upstream Klipper so no private firmware fork is required.

Reference workflow:

```text
cd ~/klipper
make menuconfig
make
        |
        v
firmware image
        |
BOOT/DFU/UF2 recovery mode
        |
Revival Bed Node
        |
USB
        |
/dev/serial/by-id/<stable-id>
```

For an RP2040 implementation, the PCB should expose convenient BOOTSEL/RESET access or recovery test pads. The exact `menuconfig` selections, first-flash procedure, pin map and validated firmware hash will be versioned in the repository when the PCB is released.

 Loss of the Bed Node must be treated as an MCU failure; physical thermal protection remains independent of firmware.

During the initial non-Bed-Node stage, the Manta remains responsible for bed temperature/heater control and the separate USB S2DW-class accelerometer is configured independently.

## Dependencies

The [smart-spool architecture](../../../hardware/generation-3-smart-spool-system.md) adds a target local service, decoder registry, assisted unknown-tag learning and mappings to calibrated Revival profiles. The [RASS architecture](../../../hardware/generation-3-rass.md) adds a local active-feed controller whose upstream feeder follows toolhead demand through buffer/dancer feedback; exact control implementation and calibration remain future work. Real-tag validation is required before claiming decoder support. The [Revival Intelligence & Diagnostics subsystem](../../../hardware/generation-3-revival-intelligence-diagnostics.md) defines the CB2 supervisory boundary and the [RID candidate backlog](../../../hardware/generation-3-enhancement-candidates.md) prioritises software-only work that can reuse the frozen baseline: pre-flight checks, service history, subsystem-health checks, notifications, job/event reports, thermal-response trends, resonance/belt trends, fixed-camera failure detection, first-layer vision, health scoring and later sensor fusion. Candidate status does not imply implementation, and automatic safety actions remain bounded by the independent hardware-safety architecture.

- [Electronics](Electronics.md) — controller, drivers, sensors and wiring.
- [Mechanics](Mechanics.md) — alignment before software compensation.
- [Safety](Safety.md) — software checks supplement physical protections.
- [Filament system](Filament-System.md) — measured material data and later profiles.

[Systems](Systems.md) · [Roadmap](../project/Roadmap.md)


## RID and LLM integration

RID core software on CB2 is independent of any LLM.

Local CB2 responsibilities:

- collect and normalise machine telemetry;
- perform deterministic checks;
- run signal-processing / anomaly-detection pipelines;
- run validated lightweight vision where practical;
- maintain machine history and baseline data;
- perform sensor fusion;
- expose provider-neutral diagnostic context.

Optional LLM responsibilities:

- explain RID findings in natural language;
- answer historical and maintenance questions;
- perform high-level reasoning over already-processed evidence;
- summarise incidents and suggested inspection sequences.

The LLM may be a service on the local network or an external provider. Provider choice is configuration, not firmware architecture.

No machine safety authority is delegated to the LLM.
