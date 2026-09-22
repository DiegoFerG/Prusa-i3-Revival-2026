# 05 — Test all eight Manta driver sockets

After validating the six TMC2209 modules, use **one known-good module** to test M1 through M8. This deliberately checks unused sockets while the return window is open.

Every socket change is made with 24 V removed and board LEDs off.

Use one include at a time from [configs/manta-slots](configs/manta-slots/).

For each socket:

1. configure that socket for UART operation;
2. leave DIAG disabled;
3. install the known-good TMC2209;
4. connect the known-good NEMA17 to the matching motor output;
5. power up and confirm Klipper connection;
6. run `DUMP_TMC STEPPER=mX`;
7. move ±2 mm with `MANUAL_STEPPER`;
8. power down and record PASS/FAIL.

A socket passes when UART register access and stepper movement both work with the same known-good driver/motor.
