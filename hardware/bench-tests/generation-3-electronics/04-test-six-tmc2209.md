# 04 — Test all six TMC2209 V1.3 modules

Use the same Manta M8P V2.0 socket (M1), motor, cable and configuration to isolate each of the six plug-in drivers. After this test, test all eight Manta sockets with one known-good module using [procedure 05](05-test-eight-manta-sockets.md).

The printable bench copy is [Guia_Banco_Pruebas_TMC2209_M8P.pdf](Guia_Banco_Pruebas_TMC2209_M8P.pdf). This Markdown procedure and the slot configuration files are the editable canonical source.

## Preconditions and equipment

- Complete [materials and safety](00-materials-and-safety.md), [receiving inspection](01-receiving-inspection.md) and [Manta USB smoke test](03-manta-usb-smoke-test.md).
- Use the active CB1 mounted on the Manta, or another verified Klipper host. Keep its MCU serial path and any active EBB36/Eddy MCU sections intact.
- Use a current-limited/protected 24 V DC supply, multimeter and a known-good unloaded NEMA17 fixed to the bench. No belt, leadscrew or other mechanism may be attached.
- Keep the bed, heaters and unrelated actuators disconnected. This is a driver test only; it does not validate the printer or final motor-current settings.
- Label the six modules TMC-A through TMC-F. Photograph their markings and inspect pins before testing.

## 1. Prepare the board and motor

1. Shut down Klipper, switch off and disconnect the 24 V supply, then wait for the Manta LEDs to go out. Never insert/remove a driver or connect/disconnect a motor while powered.
2. With the multimeter in continuity/resistance mode, identify the two separate coil pairs on the motor cable. Record the pairings; do not rely on wire colours. Connect one coil to A+/A− and the other to B+/B− on the M1 motor output, following the Manta silkscreen.
3. Set M1's driver-supply selector to **VBB** for the board's 24 V driver rail. Do not use **HV**. Leave DIAG unjumpered. Confirm jumper positions against the Manta V2.0 reference diagram and the physical board labels.
4. Connect the supply's 24 V positive and negative to the Manta `POWER` input with polarity checked by meter. Set the supply's current limit conservatively, above idle/start-up draw but low enough to limit a wiring fault. Do not connect `BED POWER` or any heater output.
5. Verify the driver's orientation from the module pin-1 marking and the Manta socket silkscreen. Use [TMC2209 V1.3 pin reference](../../reference/bigtreetech/tmc2209-v1.3/TMC2209-V1.3-Pin.jpg); do not infer orientation from heatsink position alone.

## 2. Configure Klipper for M1

Use the supplied [M1.cfg](configs/manta-slots/M1.cfg). It defines `manual_stepper m1`, UART on `PC13`, 16 microsteps, `rotation_distance: 40`, `run_current: 0.30 A RMS`, `sense_resistor: 0.110`, and low test speed/acceleration. These are conservative test values, not printer settings.

1. Copy the file to the host, for example:

   ```sh
   mkdir -p ~/printer_data/config/manta-slots
   cp M1.cfg ~/printer_data/config/manta-slots/M1.cfg
   ```

2. Add exactly one include for the slot under test to the active `printer.cfg`:

   ```ini
   [include manta-slots/M1.cfg]
   ```

   Do not include the full set of M1–M8 configurations at the same time: the pin assignments overlap with the live machine configuration.
3. Retain the existing `[mcu]` serial path for the Manta and all MCU sections needed by the active host setup. Keep the heaters and bed disabled/disconnected.
4. In the Mainsail/Fluidd console, issue `FIRMWARE_RESTART`. Continue only when Klipper reports `Ready`. Resolve any pin, duplicate-section or UART error before powering a motor.

## 3. Test TMC-A through TMC-F in M1

Repeat this full cycle for each labelled module:

1. Switch off and disconnect 24 V; wait until all board LEDs are off.
2. Fit the next driver in M1 with its orientation verified. Check that it is fully seated and that no pin is bent or offset.
3. Confirm the unloaded motor is connected to M1 and clear to turn. Keep hands, tools and loose wires away from the shaft.
4. Apply 24 V and wait for the host and Klipper to reconnect. Do not send motion commands until Klipper shows `Ready`.
5. Read the driver over UART:

   ```text
   DUMP_TMC STEPPER=m1
   ```

   Confirm Klipper returns register values without a UART communication error.
6. Run the following commands one at a time. Starting at position 0, the motor should move to +2 mm, then −2 mm, then return to 0:

   ```gcode
   MANUAL_STEPPER STEPPER=m1 SET_POSITION=0
   MANUAL_STEPPER STEPPER=m1 ENABLE=1
   MANUAL_STEPPER STEPPER=m1 MOVE=2 SPEED=1 ACCEL=5
   MANUAL_STEPPER STEPPER=m1 MOVE=-2 SPEED=1 ACCEL=5
   MANUAL_STEPPER STEPPER=m1 MOVE=0 SPEED=1 ACCEL=5
   MANUAL_STEPPER STEPPER=m1 ENABLE=0
   ```

7. Confirm smooth movement in both directions, stable Klipper connection and no abnormal smell, noise, current draw or rapid heating. Do not hold or brake the shaft by hand.
8. Record UART and movement results, supply voltage/current limit, driver marking, date and any symptoms in [acceptance.csv](records/acceptance.csv) and [test-notes.md](records/test-notes.md). A module passes only when both UART access and motion pass.
9. Power down and disconnect 24 V before removing the driver. Inspect the module and socket before moving to the next one.

## 4. Isolate a failure

- If a module fails in M1 while another passes in the unchanged setup, recheck orientation, seating and motor wiring with power off, then repeat once. Record both attempts; do not label a module faulty based on a single misconfiguration.
- If all six modules fail the same way, stop swapping drivers and inspect the M1 UART/VBB jumpers, 24 V wiring, config include, motor coil pairs and host MCU connection.
- If UART works but the motor does not move, stop and check motor/output wiring and stepper enable/configuration with power removed. Never hot-plug the motor.
- Stop immediately for smoke, sparking, unexpected current, rapid heating, repeated resets or abnormal motor noise. Keep the failure status open until explained.

Passing this procedure validates each module in M1 at the stated low-current test settings only. It does not validate the remaining Manta sockets; use [procedure 05](05-test-eight-manta-sockets.md).
