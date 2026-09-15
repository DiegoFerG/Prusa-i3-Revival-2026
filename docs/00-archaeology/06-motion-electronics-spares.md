# Recovered motion-electronics spare box

**Recovery date:** 15 September 2026  
**Provenance:** loose spare-parts box found with the stored printer material  
**Status:** recovered, visually identified where possible, **untested**

This batch is not treated merely as historical archaeology. It is a useful reserve of period motion-control electronics for the staged revival, especially Generation 1, where preserving the original machine before introducing modern hardware is the priority.

## Recovered parts

| Component | Observed quantity | Identification confidence | Intended disposition |
|---|---:|---|---|
| Mechanical endstop modules | at least 5 | High | Generation 1 spare stock; bench-test before installation |
| A4988 StepStick drivers | 3 | High; A4988 marking visible | Preferred period-style replacement if an original driver fails |
| DRV8825 stepper drivers | 5 | High; DRV8825 marking visible | Secondary spare / controlled experiment |
| TMC2130 StepStick modules | 5 | High; TMC2130/staticboards.com markings visible | Reserve for Generation 2 experimentation; SPI features require deliberate integration |

Total visually identified stepper-driver reserve: **13 modules**.

## Revival policy

### Generation 1 — original-hardware revival

The goal is to prove that the historical printer can operate using its original architecture. Recovered spare parts may be used to replace failed components without unnecessarily modernising the machine.

If a plug-in stepper driver is found defective, the preferred substitution order is:

1. electrically compatible original/period driver already installed or recovered;
2. recovered A4988, after identification, orientation and Vref checks;
3. DRV8825 only after confirming pin compatibility, current configuration, microstepping implications and firmware/mechanical consequences.

TMC2130 modules are **not** a default Generation-1 substitution because using their advanced capabilities changes the historical control architecture.

### Generation 2 — RAMPS/Re-ARM-era upgrade and experimentation

The recovered TMC2130 modules are potentially valuable here. Their SPI configuration and diagnostics make them useful experimental hardware while retaining the visible RepRap/Prusa-i3 character of the machine.

No module is considered serviceable until tested.

### Generation 3 — final autonomous 1.75 mm machine

These recovered drivers are not assumed to be part of the final electronics. Generation 3 will use contemporary hardware selected for the final autonomous architecture. Period modules may nevertheless be retained as documentary artefacts, test hardware, or deliberately visible retro elements if electrically isolated from critical functions.

## Mandatory bench-test procedure

Before fitting any recovered driver:

- inspect PCB, solder joints, headers, potentiometer and components under magnification;
- identify the exact module and pin orientation;
- check for obvious shorts between power rails and ground;
- confirm logic and motor supply compatibility;
- establish a conservative initial current/Vref setting using documentation for the exact carrier;
- test with a known-good stepper motor and current-limited bench supply where practical;
- verify direction, enable and step operation;
- monitor driver temperature;
- label the tested module with its result and measured configuration.

For endstops:

- inspect lever and microswitch mechanically;
- continuity-test COM/NO/NC as applicable;
- verify the PCB connector pinout before connecting it to a controller;
- test repeatability before installing it as a machine limit switch.

## Historical interpretation

The coexistence of A4988, DRV8825 and TMC2130 modules is useful evidence of several generations of RepRap-era experimentation. It suggests that motion-electronics upgrades were considered or accumulated during the printer's earlier life, although the recovered parts alone do **not** prove that any particular module was ever installed in this printer.

That distinction is important to the archaeology record: recovered proximity is evidence of project context, not proof of original configuration.

## Photo archive

The new photographs belong under:

`photos/00-archaeology/originals/`

Permanent photo IDs assigned: `ARQ-20260915-081` through `ARQ-20260915-089`. The published files use the archive naming convention and the `SRCSPARE01`–`SRCSPARE09` source tokens because the sanitised recovery copies no longer retain the original camera filename metadata.

The nine published images were metadata-sanitised before repository upload; filenames and documentation remain in English.
