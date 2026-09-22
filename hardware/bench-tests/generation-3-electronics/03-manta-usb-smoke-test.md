# 03 — Manta M8P V2.0 USB smoke test

## Initial state

Do not fit any TMC2209 yet.

With power removed, disconnect heaters, bed, fans, motors and endstops; do not use the HV driver-power domain; and verify USB/power jumpers against the actual Manta V2.0 board before applying power.

## First 24 V power-up

Use a current-limited 24 V source. Immediately stop if there is smoke, sparking, abnormal smell, unexpectedly high current or rapid local heating.

## Build Klipper firmware for Manta

```bash
cd ~/klipper
make clean
make menuconfig
```

Target the documented Manta M8P V2.0:

- STMicroelectronics STM32
- STM32H723
- 128 KiB bootloader offset
- 25 MHz crystal
- USB communication on PA11/PA12

Then:

```bash
make -j2
```

## Flash and identify

For an initial microSD flash, copy `~/klipper/out/klipper.bin` as `firmware.bin` to the Manta MCU microSD card and reboot the controller. Verify the board performed the expected bootloader update/rename behaviour before continuing.

```bash
ls -l /dev/serial/by-id/
```

Record the exact Klipper STM32H723 path and insert it into [printer-manta-usb.cfg.template](configs/printer-manta-usb.cfg.template).

## PASS

- Klipper connects to the MCU
- USB remains stable for at least 10 minutes
- no repeated resets/disconnects
- no abnormal heating

Run [snapshot.sh](scripts/snapshot.sh).
