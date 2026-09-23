# Generation 3 electronics bench-test pack

Version: **1.0**  
Prepared: **22 September 2026**

## Purpose

Validate the purchased Generation 3 electronics while return/warranty windows are still open:

- 1 × BIGTREETECH Manta M8P V2.0
- 6 × BIGTREETECH TMC2209 V1.3
- 1 × BIGTREETECH EBB36 Gen2 kit including the Gen2 adapter/protection board

A Raspberry Pi 2 is used only as a **temporary Klipper bench host**. This does not change CB2 as the frozen final Generation 3 host.

## Acceptance rule

A component may be marked **TESTED / PASS** only after:

1. packaging and exact PCB revision are photographed;
2. visual inspection finds no disqualifying damage;
3. power-up shows no abnormal smell, heat or current draw;
4. communication with Klipper is stable;
5. the applicable functional tests pass;
6. evidence is retained in the test record.

`Purchased != Tested != Commissioned`.

## Test order

1. [Materials and safety](00-materials-and-safety.md)
2. [Receiving inspection](01-receiving-inspection.md)
3. [Raspberry Pi 2 Klipper host](02-rpi2-klipper-host.md)
4. [Manta USB smoke test](03-manta-usb-smoke-test.md)
5. [Test all six TMC2209 modules](04-test-six-tmc2209.md)
6. [Test all eight Manta driver sockets](05-test-eight-manta-sockets.md)
7. [EBB36 Gen2 USB test](06-ebb36-usb.md)
8. [Manta ↔ EBB36 CAN test](07-manta-ebb36-can.md)
9. [Optional low-risk I/O tests](08-optional-io-tests.md)
10. [Closeout and evidence](09-closeout-and-evidence.md)

Bench configurations are intentionally conservative and are **not final printer settings**.

## Bench fixture

Before CAD, use the [bench-fixture dimensional survey](bench-fixture-dimensional-survey.md) to record the exact mounting, connector and service-clearance geometry of the Manta, temporary Raspberry Pi 2, 24 V bench power supply and EBB USB Adapter.

## Records

- [Acceptance register](records/acceptance.csv)
- [Test notes](records/test-notes.md)
- [Sources](SOURCES.md)

Future evidence should be added with clear dates and component IDs. Photographs remain evidence, not proof of a passed test unless linked to a recorded result.
