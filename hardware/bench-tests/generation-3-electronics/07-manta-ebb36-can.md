# 07 — Manta ↔ EBB36 CAN acceptance test

Perform this only after both boards pass their USB tests.

## Manta USB-to-CAN bridge target

- STM32H723
- 128 KiB bootloader
- 25 MHz crystal
- USB PA11/PA12
- CAN PD0/PD1
- CAN bitrate 1,000,000

## EBB36 CAN target

- STM32G0B1
- 8 MHz crystal
- bootloader choice matching the board's actual firmware state
- CAN PB12/PB13
- CAN bitrate 1,000,000

After flashing and with power removed, configure EBB36 for CAN mode, disconnect its USB data connection, connect CAN-H/CAN-L/common ground and retain the intended 24 V supply through the adapter/protection board.

## Termination

```text
Raspberry Pi 2
      |
     USB
      |
Manta M8P V2  ===== CAN =====  EBB36 Gen2
  120 ohm                          120 ohm
```

With power removed, CAN-H to CAN-L should measure about 60 Ω.

## Linux can0

Install [can0.interfaces](configs/can0.interfaces) at `/etc/network/interfaces.d/can0`, then verify:

```bash
ip -details link show can0
~/klippy-env/bin/python ~/klipper/scripts/canbus_query.py can0
```

Record the Manta bridge and EBB36 UUIDs and insert them in [printer-manta-ebb-can.cfg.template](configs/printer-manta-ebb-can.cfg.template).

## Functional and stability checks

Run `DUMP_TMC STEPPER=ebb_motor`, `ACCELEROMETER_QUERY`, and the unloaded ±2 mm motor movement. Keep the two-node bus running for at least 15 minutes and inspect:

```bash
ip -details -statistics link show can0
```

PASS requires stable can0, both MCU UUIDs recorded, Klipper connected to both nodes, working EBB TMC/LIS2DW and no CAN disconnects or BUS-OFF state.
