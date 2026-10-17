# Generation 3 electronics bench-test notes

Status: **procedure prepared; TMC2209/Manta socket results not yet recorded**.

## 24 V bench supply

Model:
No-load measured voltage:
Current limit used:
Manta `POWER` polarity checked:
Driver rail selector (VBB/HV):

## Klipper host

Host type (CB1 / temporary Linux host):
Model/revision:
OS:
IP address:
Klipper commit:
Manta serial path:

## Manta M8P V2.0

PCB revision:
USB serial path:
CAN UUID:

## TMC2209 modules

| ID | Marking/revision | Result | Notes |
|---|---|---|---|
| TMC-A | | | |
| TMC-B | | | |
| TMC-C | | | |
| TMC-D | | | |
| TMC-E | | | |
| TMC-F | | | |

For each module, record UART (`DUMP_TMC`), movement in both directions, Klipper state, current/temperature symptoms and evidence path in the result/notes fields. The procedure uses M1 unchanged for all six modules.

## Manta M8P V2.0 driver sockets

Reference TMC (label/revision):
Reference motor/cable:

| Socket | Output connector | UART (`DUMP_TMC`) | Motion both directions | Klipper stayed Ready | Result | Notes / evidence |
|---|---|---|---|---|---|---|
| M1 | Motor1 | | | | | |
| M2 | Motor2 | | | | | |
| M3 | Motor3A or Motor3B | | | | | |
| M4 | Motor4 | | | | | |
| M5 | Motor5 | | | | | |
| M6 | Motor6 | | | | | |
| M7 | Motor7 | | | | | |
| M8 | Motor8 | | | | | |

For M3, Motor3A and Motor3B share the same driver and count as one socket. Note which output was used.

## EBB36 Gen2

PCB revision:
Adapter/protection PCB revision:
USB serial path:
CAN UUID:

## Observations

Add dated observations here and link retained logs or photographs.

## 8 October 2026 — active CB1 USB bench

[Detailed session record](2026-10-08-usb-eddy-camera.md): Manta/CB1/EBB/Eddy communication, corrected Eddy short cable, direct-USB 30-minute baseline, camera/Crowsnest/Mainsail, initial USB disruption and successful later restart/cold start. Joint prolonged test and CAN remain pending.
