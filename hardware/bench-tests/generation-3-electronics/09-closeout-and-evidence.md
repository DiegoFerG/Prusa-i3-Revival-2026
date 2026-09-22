# 09 — Closeout and evidence

## Minimum expected acceptance record

### Manta M8P V2.0

- [ ] PCB revision photographed
- [ ] 24 V smoke test passed
- [ ] Klipper firmware flashed
- [ ] USB stable
- [ ] M1–M8 tested with one known-good TMC
- [ ] CAN bridge tested with EBB36
- [ ] no abnormal thermal behaviour

### Six TMC2209 V1.3 modules

- [ ] TMC-A UART + motor
- [ ] TMC-B UART + motor
- [ ] TMC-C UART + motor
- [ ] TMC-D UART + motor
- [ ] TMC-E UART + motor
- [ ] TMC-F UART + motor

### EBB36 Gen2

- [ ] PCB revision photographed
- [ ] adapter/protection board photographed
- [ ] 24 V power-up passed
- [ ] USB stable
- [ ] integrated TMC2209 passed
- [ ] LIS2DW passed
- [ ] board-temperature input plausible
- [ ] CAN stable
- [ ] no abnormal thermal behaviour

## Evidence to retain

- original photographs
- `snapshot-*.txt`
- relevant `klippy.log`
- `DUMP_TMC` output
- CAN UUID query output
- `ip -details -statistics link show can0`
- [acceptance.csv](records/acceptance.csv)
- [test-notes.md](records/test-notes.md)

Only after reviewed evidence exists should the canonical procurement record change a part from **Purchased** to **Tested**. Do not mark these parts **Commissioned** until integrated and validated in the final machine.
