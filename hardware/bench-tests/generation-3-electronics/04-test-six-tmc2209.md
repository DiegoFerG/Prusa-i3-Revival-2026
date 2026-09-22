# 04 — Test all six TMC2209 V1.3 modules

The objective is to isolate each plug-in driver by using the **same known Manta socket** for every module.

## Prepare M1

With Manta fully powered off:

- configure M1 for UART operation according to the M8P V2.0 documentation
- do not install the DIAG jumper
- use the normal 24 V driver supply domain
- use [M1.cfg](configs/manta-slots/M1.cfg)

## Repeat for TMC-A through TMC-F

1. remove 24 V power and wait until board LEDs are off;
2. insert the TMC2209 with orientation verified;
3. connect the unloaded known-good NEMA17 to M1;
4. apply 24 V and start/restart Klipper;
5. run `DUMP_TMC STEPPER=m1`;
6. exercise the motor:

```gcode
MANUAL_STEPPER STEPPER=m1 SET_POSITION=0
MANUAL_STEPPER STEPPER=m1 ENABLE=1
MANUAL_STEPPER STEPPER=m1 MOVE=2 SPEED=1
MANUAL_STEPPER STEPPER=m1 MOVE=0 SPEED=1
MANUAL_STEPPER STEPPER=m1 ENABLE=0
```

7. confirm smooth movement in both directions and no abnormal heating;
8. remove power before changing the module;
9. record the result in [acceptance.csv](records/acceptance.csv).

If one module fails in M1 while another passes in the same socket, the module becomes the primary suspect.
