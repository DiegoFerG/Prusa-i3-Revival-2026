# Generation 3 enhancement candidates

This document records improvement candidates and their promotion history for the Revival 2026 Generation 3 build. Unpromoted candidates remain separate from the frozen architecture so they can be evaluated at the correct mechanical/electrical design stage without silently becoming requirements. **Eddy Duo probing has been promoted**; its current requirements belong to the [toolhead architecture](generation-3-extrusion-toolhead.md).

The objective is to improve fault detection, automatic preparation, maintenance visibility and operator safety without turning the Revival into an unnecessarily complex machine.

## Evaluation rule

A candidate may be promoted into the frozen Generation 3 architecture only after its mechanical integration, wiring, software support, failure modes and maintenance burden have been reviewed.

The preferred design philosophy is:

> mechanical correctness first, independent hardware safety second, software automation third.

## 1. Filament motion / jam detection

### Goal

Add a physical filament-motion sensor that verifies that filament is **actually moving** when the extruder commands motion.

This is separate from:

- spool RFID/NFC identification;
- spool weighing;
- slicer-predicted filament consumption;
- a simple filament-presence switch.

### Target failure detection

- filament run-out;
- filament break;
- extruder grinding/slipping;
- blocked or partially blocked hotend;
- spool unable to rotate;
- feed path obstruction.

### Candidate implementation

A compact encoder/wheel-style motion sensor mounted in the filament path, with Klipper-compatible pulse monitoring. A BTT Smart Filament Sensor-class implementation is a reference candidate, but the exact sensor is not frozen.

The sensor must not add excessive drag or compromise flexible-material feeding.

### Status

**Strong candidate for promotion to base Generation 3 hardware.** Exact sensor and mounting remain open.

---

## 2. Eddy-current Z probe / fast bed scanning — promoted

This candidate has been **promoted into the frozen Generation 3 architecture**.

The selected direction is **BIGTREETECH Eddy Duo** integrated with the frozen E3D Roto + Revo toolhead stack.

The remaining work is no longer a component-selection question; it is implementation engineering:

- final mount geometry and adjustability;
- X/Y/Z probe offsets;
- connector pinout and physical harness for the frozen independent 5 V CAN node downstream of the EBB36 Gen2 passthrough;
- thermal calibration/compensation;
- repeatability validation on the final spring-steel/magnetic bed;
- interaction with the nozzle-cleaning strategy and final Z-reference workflow.

Canonical source: [Generation 3 extrusion/toolhead target](generation-3-extrusion-toolhead.md).

---

## 3. Nozzle cleaning / purge station

### Goal

Provide a compact fixed station that can clean the nozzle before probing and, where useful, before printing.

### Possible functions

- purge position;
- heat-resistant brush or wiping surface;
- controlled nozzle wipe sequence;
- removable debris collection area;
- optional purge catcher.

### Design constraints

- remain inside or very close to the original machine envelope;
- not reduce useful bed travel unnecessarily;
- be easy to remove and clean;
- tolerate nozzle temperatures safely;
- avoid dropping debris into electronics or linear guides;
- integrate with Klipper macros only after the mechanical geometry is proven.

This feature becomes especially valuable if the final Z reference requires a clean nozzle.

### Status

**Strong candidate**, linked to the final probe/toolhead decision.

---

## 4. Retro physical control panel and hardware emergency stop

### Goal

Complement the HDMI5/KlipperScreen interface with a small physical control panel that reinforces the Revival aesthetic and provides immediate hardware control.

### Candidate controls

- illuminated main power control;
- PAUSE button;
- RESUME button;
- user-programmable function button;
- rotary encoder or selector if useful;
- hardware emergency-stop control.

### Emergency-stop requirement

If implemented, the emergency-stop function must **not depend on Linux, Klipper, Moonraker, CAN or a software macro** to remove hazardous actuator/heater energy.

The exact power architecture must be designed later, but the target is a latching hardware mechanism that places the machine in a safe state and requires deliberate reset.

The emergency-stop function is not a substitute for mains fusing, protective earth, branch fuses, thermal protection or firmware heater checks.

### Aesthetic direction

Industrial/retro instrumentation rather than a modern gaming/control-panel appearance: physical buttons, restrained indicator lamps and lab/industrial visual language consistent with the HDMI5 enclosure and CCTV camera styling.

### Status

**Candidate subsystem. Hardware emergency-stop functionality has high priority during the final safety design.**

---

## 5. Maintenance and condition telemetry

### Goal

Use the sensors already present in Generation 3 to build a local maintenance record and detect gradual degradation.

### Candidate data

- total printer powered hours;
- total printing hours;
- hotend heater hours and heating cycles;
- bed heater hours and cycles;
- individual fan runtime;
- hotend-fan RPM history and low-RPM events;
- total filament consumed by material/profile;
- rail/lubrication maintenance date;
- nozzle install date and estimated filament throughput;
- belt service/tension checks;
- resonance-test history;
- temperature-calibration/PID history;
- jam/run-out events;
- failed or cancelled print history.

### Resonance trend tracking

Because X/toolhead and Y/bed accelerometers are permanently installed, repeated resonance tests may be stored and compared over time. Large changes can be used as a maintenance clue for:

- loose fasteners;
- rail/block degradation;
- belt-tension changes;
- toolhead changes;
- bearing/roller problems;
- frame looseness.

This is diagnostic telemetry, not automatic proof of a specific mechanical fault.

### Storage policy

Maintenance data should remain exportable and locally stored. Important configuration/calibration data belongs in version-controlled project files where practical rather than existing only in a printer-local database.

### Status

**Software-oriented candidate with low hardware cost.** Evaluate once the final sensor set is known.

---

## 6. Electrical power and health monitoring

### Goal

Add non-safety-critical measurement of DC power behaviour for diagnostics, energy logging and degradation detection.

### Candidate measurements

- 24 V bus voltage;
- total DC current;
- selected branch current where useful;
- calculated power/energy;
- bed heater warm-up time;
- hotend warm-up time;
- abnormal current or voltage trends.

### Potential uses

- energy-per-print statistics;
- detect unexpected PSU voltage sag;
- identify a heater that is taking progressively longer to reach temperature;
- correlate electrical behaviour with thermal faults;
- log abnormal operating conditions.

### Safety boundary

Electrical telemetry is **diagnostic only**. It must never replace:

- fuses;
- properly rated wiring/connectors;
- thermal fuse on the bed;
- protective earth;
- hardware emergency-stop design;
- Klipper heater protections.

### Status

**Candidate**, exact sensor topology and whether per-branch measurement is worthwhile remain open.

---

## 7. Automated pre-print self-check sequence

These candidates can ultimately be combined into a controlled pre-print workflow. The sequence itself is a software concept and will only be enabled for hardware that has been installed and validated.

Possible future flow:

```text
spool detected
   |
RFID/NFC identity + remaining mass
   |
filament-motion sensor ready
   |
home axes
   |
Z gantry alignment
   |
nozzle clean / purge
   |
fast bed scan / Z reference
   |
verify temperatures / fans / selected sensors
   |
print
```

During printing the machine may monitor:

```text
filament motion
hotend-fan RPM
temperatures
spool inventory estimate
selected electrical telemetry
```

The machine should fail gracefully: optional telemetry or identification subsystems must not turn a recoverable non-critical sensor fault into an unsafe state.

## Promotion priorities

When Generation 3 design reaches the relevant subsystems, evaluate in approximately this order:

1. filament-motion/jam sensor;
2. hardware emergency-stop and physical controls;
3. nozzle-cleaning station and its interaction with the frozen Eddy Duo probe and final Z-reference workflow;
4. maintenance telemetry;
5. electrical monitoring;
6. integrated automated pre-print/self-check workflow.

This order is not a purchasing order and may change with the final mechanical design.
