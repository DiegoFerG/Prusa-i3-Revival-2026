# 00 — Materials and safety

## Required equipment

- CB1 mounted on the Manta M8P V2.0 with Klipper/Mainsail available over USB, or another already verified Klipper host
- separate host supply if using a temporary Raspberry Pi host
- 24 V DC bench supply with current limiting, or a correctly protected 24 V supply
- multimeter
- one known-good unloaded NEMA17 stepper motor
- multimeter with continuity/resistance mode for identifying the motor's coil pairs
- labels/marker for TMC-A through TMC-F and a way to record each result
- one known-good 100K NTC thermistor, optional
- one small 24 V fan, optional
- USB-A ↔ USB-C **data** cable for Manta
- short twisted pair for CAN-H/CAN-L plus common ground
- small microSD card for Manta MCU firmware update if that method is used

For the first board-only/motor tests, a current-limited 24 V supply with sufficient headroom for the board and unloaded motor is sufficient. Do not size this bench supply from the final printer load. Check its output polarity and voltage before connecting it to the Manta `POWER` input.

## Bench rules

- Generation 3 bench work uses 24 V.
- Power the Raspberry Pi separately.
- Do not insert or remove TMC drivers, motors, thermistors, CAN wiring or 24 V wiring while powered.
- Verify each TMC2209 orientation against both the Manta silkscreen and the module before insertion.
- Do not install DIAG jumpers for these acceptance tests.
- Use UART mode for TMC2209 modules.
- Keep heaters and the bed disconnected during firmware flashing and initial tests.
- For TMC2209 tests, select **VBB** at the driver socket; leave **HV** and `BED POWER` unused. Confirm the jumper and connector labels against the exact Manta M8P V2.0 board revision before applying power.
- Identify the motor's two coil pairs with a meter. Connect one pair to A+/A− and the other to B+/B−; do not rely only on wire colours.
- Secure the motor with its shaft unloaded and free to turn. Keep hands and tools away while energized; never hold the shaft to brake it.
- Use the supplied 0.30 A RMS TMC configuration only for these unloaded tests. It is not the final printer motor current.
- EBB36 Gen2 USB is for communication; the board still requires its intended 24 V supply path through the supplied adapter/protection hardware.
- Do not bypass the EBB36 adapter/protection board.
- Do not connect EBB36 USB and CAN simultaneously during these tests.
- CAN must have exactly two 120 Ω terminations, one at each physical end.
- With power removed, a correctly terminated two-node CAN bus should measure about 60 Ω between CAN-H and CAN-L.

## Conservative motor current

The supplied bench configuration uses **0.30 A RMS** for stepper-driver tests. This is deliberately low for an unloaded known-good NEMA17.

Do not reuse this as the final printer motor current.
