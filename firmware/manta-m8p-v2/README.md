# Manta M8P V2 Firmware

Firmware and host configuration for the Generation 3 electronics of
Prusa i3 Revival 2026 (PHOENIX).

## Architecture

PHOENIX uses a BIGTREETECH Manta M8P V2 as the main controller.

Host computer:
- Temporary bring-up: BIGTREETECH CB1
- Final target: BIGTREETECH CB2 or Raspberry Pi CM4
- Current CB1 hostname: PHOENIX-CB1

Toolhead:
- BIGTREETECH EBB36
- CAN/USB architecture to be finalized during commissioning.

## Directories

- host/    Host/SBC configuration and installation documentation.
- mcu/     Manta STM32H723 firmware build and flashing documentation.
- klipper/ Version-controlled Klipper configuration for PHOENIX.

## Security

Real system.cfg files and other files containing credentials must never
be committed. Use the sanitized templates stored in this repository.
