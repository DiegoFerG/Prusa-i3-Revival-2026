# 00 — Materials and safety

## Required equipment

- Raspberry Pi 2 and microSD card
- separate power supply for the Raspberry Pi 2
- Ethernet for the Pi, preferred for the bench
- 24 V DC bench supply with current limiting, or a correctly protected 24 V supply
- multimeter
- one known-good unloaded NEMA17 stepper motor
- one known-good 100K NTC thermistor, optional
- one small 24 V fan, optional
- USB-A ↔ USB-C **data** cable for Manta
- short twisted pair for CAN-H/CAN-L plus common ground
- small microSD card for Manta MCU firmware update if that method is used

For the first board-only/motor tests, a current-limited 24 V supply in the low-amp range is sufficient. Do not size this bench supply from the final printer load.

## Bench rules

- Generation 3 bench work uses 24 V.
- Power the Raspberry Pi separately.
- Do not insert or remove TMC drivers, motors, thermistors, CAN wiring or 24 V wiring while powered.
- Verify each TMC2209 orientation against both the Manta silkscreen and the module before insertion.
- Do not install DIAG jumpers for these acceptance tests.
- Use UART mode for TMC2209 modules.
- Keep heaters and the bed disconnected during firmware flashing and initial tests.
- EBB36 Gen2 USB is for communication; the board still requires its intended 24 V supply path through the supplied adapter/protection hardware.
- Do not bypass the EBB36 adapter/protection board.
- Do not connect EBB36 USB and CAN simultaneously during these tests.
- CAN must have exactly two 120 Ω terminations, one at each physical end.
- With power removed, a correctly terminated two-node CAN bus should measure about 60 Ω between CAN-H and CAN-L.

## Conservative motor current

The supplied bench configuration uses **0.30 A RMS** for stepper-driver tests. This is deliberately low for an unloaded known-good NEMA17.

Do not reuse this as the final printer motor current.
