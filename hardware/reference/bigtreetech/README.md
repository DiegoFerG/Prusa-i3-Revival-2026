# BIGTREETECH vendor reference archive

This directory preserves pinned, local copies of official BIGTREETECH reference material used to identify, wire, configure and bench-test the purchased **Generation 3** electronics.

Imported on **23 September 2026**.

These files are **vendor references**, not project-authored documentation and not evidence that any component passed inspection, testing or commissioning.

## Manta M8P V2.0

- [User manual](manta-m8p-v2.0/BIGTREETECH-MANTA-M8P-V2.0-User-Manual.pdf)
- [Official pinout](manta-m8p-v2.0/BIGTREETECH-MANTA-M8P-V2.0-PinOut.png)
- [Connection diagram](manta-m8p-v2.0/M8P-V2.0-connect.png)
- [Schematic](manta-m8p-v2.0/BIGTREETECH-MANTA-M8P-V2.0-SCH.pdf)
- [Board dimensions](manta-m8p-v2.0/BIGTREETECH-MANTA-M8P-V2.0-SIZE.pdf)
- [Reference Klipper configuration](manta-m8p-v2.0/generic-bigtreetech-manta-m8p-V2_0.cfg)
- [Official wiki source snapshot](wiki/M8P-V2_0.md)

## EBB36 Gen2 V1.0 and EBB USB Adapter V1.0

- [EBB36 Gen2 schematic](ebb36-gen2-v1.0/BIGTREETECH-EBB36-GEN2-SCH.pdf)
- [EBB36 Gen2 pinout](ebb36-gen2-v1.0/EBB36-GEN2-pin-en.jpg)
- [Reference Klipper configuration](ebb36-gen2-v1.0/sample-bigtreetech-ebb36-gen2-v1.0.cfg)
- [Official wiki source snapshot](wiki/EBB36_GEN2.md)
- The wiki snapshot is self-contained with its referenced images, including the USB adapter, communication-mode/termination, power, motor, fan, probe and passthrough diagrams.

## TMC2209 V1.3

- [User manual](tmc2209-v1.3/BIGTREETECH-TMC2209-V1.3-User-Manual.pdf)
- [Pinout](tmc2209-v1.3/TMC2209-V1.3-Pin.jpg)
- [Schematic](tmc2209-v1.3/TMC2209-V1.3-SCH.pdf)
- [Board dimensions](tmc2209-v1.3/TMC2209-V1.3-SIZE.pdf)
- [Official wiki source snapshot](wiki/TMC2209.md)

## Archive rules

- Keep imported vendor files unmodified.
- Put Revival-specific annotations, wiring decisions and derived diagrams outside the imported files and link back to the source.
- Verify the physical PCB revision in hand before applying any pinout, jumper or flashing instruction.
- See [SOURCE-MANIFEST.md](SOURCE-MANIFEST.md) for pinned upstream revisions and [SHA256SUMS.txt](SHA256SUMS.txt) for local file hashes.
- See [THIRD-PARTY-NOTICE.md](THIRD-PARTY-NOTICE.md) for attribution/licensing notes.
