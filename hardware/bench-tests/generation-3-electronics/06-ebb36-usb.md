# 06 — EBB36 Gen2 USB acceptance test

Test the EBB36 over USB before introducing CAN.

## Wiring

With all power removed:

- use the supplied Gen2 adapter/protection board
- supply the adapter/protection board from 24 V
- connect adapter ↔ EBB36 with the intended cable
- configure the EBB36 for USB mode according to the actual PCB documentation/revision
- connect the adapter USB-C data connection to the Raspberry Pi 2
- leave CAN disconnected
- leave heater output disconnected

The EBB36 still requires its intended 24 V power path when communicating by USB.

## Klipper USB firmware

```bash
cd ~/klipper
make clean
make menuconfig
```

Target the actual EBB36 Gen2 hardware:

- STM32G0B1
- 8 MHz crystal
- USB on PA11/PA12
- bootloader choice matching the firmware state actually present on the board

Compile with `make -j2`. If using STM32 DFU, confirm the board really enumerates in DFU mode before issuing a flash command.

Then identify the MCU with:

```bash
ls -l /dev/serial/by-id/
```

Use [printer-ebb36-usb-standalone.cfg.template](configs/printer-ebb36-usb-standalone.cfg.template) and replace `__EBB_SERIAL__`.

## Functional checks

With an unloaded NEMA17 attached to the EBB motor output:

```gcode
DUMP_TMC STEPPER=ebb_motor
MANUAL_STEPPER STEPPER=ebb_motor SET_POSITION=0
MANUAL_STEPPER STEPPER=ebb_motor ENABLE=1
MANUAL_STEPPER STEPPER=ebb_motor MOVE=2 SPEED=1
MANUAL_STEPPER STEPPER=ebb_motor MOVE=0 SPEED=1
MANUAL_STEPPER STEPPER=ebb_motor ENABLE=0
ACCELEROMETER_QUERY
```

PASS requires stable USB, working integrated TMC2209, motor movement in both directions, plausible LIS2DW response, plausible onboard temperature and no abnormal heating.
