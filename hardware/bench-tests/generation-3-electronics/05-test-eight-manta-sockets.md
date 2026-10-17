# 05 — Test all eight Manta driver sockets

After [testing all six TMC2209 modules](04-test-six-tmc2209.md), select one module that passed in M1 and use it with the same known-good unloaded NEMA17 to check every Manta M8P V2.0 driver socket, M1 through M8. This separates a socket/wiring/configuration fault from a driver fault.

The printable step-by-step worksheet is [Guia_Banco_Pruebas_TMC2209_M8P.pdf](Guia_Banco_Pruebas_TMC2209_M8P.pdf). The Klipper pin definitions are in [configs/manta-slots](configs/manta-slots/).

## Before each socket

1. Shut down Klipper, switch off and disconnect the 24 V supply, and wait until the board LEDs are off.
2. Move the known-good driver to the selected socket. Check module orientation and seating against the Manta silkscreen and the TMC pin reference. Connect the known-good motor to the matching output; never change either connection with power on.
3. Set the selected socket to **VBB**, not HV. Leave DIAG unjumpered. Keep `BED POWER`, the bed and all heater outputs disconnected.
4. Confirm the motor is unloaded and fixed securely. Check the supply polarity and that no bare conductor can short.
5. In `printer.cfg`, remove the previous slot include and add **only** the configuration for the current slot, as shown below. Keep the Manta MCU serial path and other active MCU sections intact.
6. Power up and wait for host reconnect. If the host loses power with the 24 V supply, wait for its full boot and Klipper reconnection; do not issue commands using a stale console/configuration.
7. When Klipper reports `Ready`, run `DUMP_TMC STEPPER=mX`, replacing `mX` with the selected motor name. Confirm register values return without UART errors.
8. Run the motion sequence below. Starting from 0, the motor should move to +2 mm, −2 mm and back to 0. Confirm smooth motion in both directions and no abnormal current draw, noise, heating or MCU reset.
9. Record PASS/FAIL plus UART, motion, supply and symptom notes in [acceptance.csv](records/acceptance.csv) and [test-notes.md](records/test-notes.md). Power off and disconnect 24 V before moving to the next socket.

```gcode
MANUAL_STEPPER STEPPER=mX SET_POSITION=0
MANUAL_STEPPER STEPPER=mX ENABLE=1
MANUAL_STEPPER STEPPER=mX MOVE=2 SPEED=1 ACCEL=5
MANUAL_STEPPER STEPPER=mX MOVE=-2 SPEED=1 ACCEL=5
MANUAL_STEPPER STEPPER=mX MOVE=0 SPEED=1 ACCEL=5
MANUAL_STEPPER STEPPER=mX ENABLE=0
```

## Socket configuration and pin map

The include path is relative to `printer_data/config`; add one include at a time. `!` marks the inverted signal as written in Klipper syntax. Each slot file uses 16 microsteps, `rotation_distance: 40`, `run_current: 0.30 A RMS`, a 0.110 Ω sense resistor and low test speed/acceleration.

| Socket | Motor output | Step | Dir | Enable | UART | Klipper name | Include |
|---|---|---|---|---|---|---|---|
| M1 | Motor1 | PE6 | PE5 | !PC14 | PC13 | m1 | `manta-slots/M1.cfg` |
| M2 | Motor2 | PE2 | PE1 | !PE4 | PE3 | m2 | `manta-slots/M2.cfg` |
| M3 | Motor3A or Motor3B | PB8 | !PB7 | !PE0 | PB9 | m3 | `manta-slots/M3.cfg` |
| M4 | Motor4 | PB4 | PB3 | !PB6 | PB5 | m4 | `manta-slots/M4.cfg` |
| M5 | Motor5 | PG13 | PG12 | !PG15 | PG14 | m5 | `manta-slots/M5.cfg` |
| M6 | Motor6 | PG9 | PD7 | !PG11 | PG10 | m6 | `manta-slots/M6.cfg` |
| M7 | Motor7 | PD4 | PD3 | !PD6 | PD5 | m7 | `manta-slots/M7.cfg` |
| M8 | Motor8 | PC7 | PC8 | !PD2 | PC6 | m8 | `manta-slots/M8.cfg` |

Motor3A and Motor3B share the M3 driver. Testing both connectors is optional and does not count as two independent driver sockets; power off before moving the motor between them.

## Acceptance and failure isolation

A socket passes only when Klipper reads the TMC over UART, the known-good motor moves smoothly in both directions, Klipper stays `Ready`, and there is no abnormal heating, current draw or reset. Possession, visual inspection or a successful test on a different socket is not a pass.

If the reference driver/motor passes some sockets but not another, power down and recheck that socket's VBB/UART selection, orientation, connector seating and the matching include file. Repeat only after correcting a concrete setup issue, and retain both observations. If UART and motion fail on every socket, stop and inspect the common supply, Manta host/MCU and configuration. Do not keep swapping parts while powered.

## Closeout

When all eight entries are complete, summarize failed/open items and evidence paths in [test-notes.md](records/test-notes.md). Leave any failed socket unaccepted and resolve it under [closeout and evidence](09-closeout-and-evidence.md). These tests do not authorize heater, bed, CAN, full-board or print commissioning.
