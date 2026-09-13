# Stage 01 — Teardown, cleaning and inventory photo archive

This directory contains the photographic evidence collected during **Stage 01 — Teardown, cleaning and inventory** of Prusa i3 Revival 2026.

**Stage status: COMPLETE — 13 September 2026.**

The current chronological `TD-` sequence runs from `TD-20260913-001` through `TD-20260913-228`.

## Originals

`originals/` contains **159 immutable evidence photographs**:

- `001–040`: workbench preparation, complete-printer baseline and installed subsystem close-ups;
- `041–159`: controlled teardown, removed components, wiring, electronics, printed parts and final disassembled state.

Original evidence files must not be intentionally edited, overwritten, destructively rotated or recompressed.

## Derived component inventory

`derived/component-inventory/` contains **69 cleaned catalogue photographs**, `160–228`.

These are intentionally **derivatives**, not forensic originals. Each JPEG was decoded, orientation-corrected and re-encoded from pixel data without retaining EXIF, GPS, XMP or camera/device metadata. No generative or content-changing edit was applied.

The derived inventory documents measured frame/carriage geometry, rods, motors, mirrors, electronics, PSU, motion hardware, bearings, hotend and thermistor.

## Naming convention

`TD-YYYYMMDD-NNN-subsystem-description.jpg`

Where:

- `TD` = Teardown;
- `YYYYMMDD` = capture/inventory date;
- `NNN` = stable chronological identifier within the Stage 01 archive;
- `subsystem-description` = concise English description.

## Indexes and manifests

- [INDEX.md](INDEX.md) — Stage 01 range/index overview;
- `manifest.csv` — originals `001–040`;
- `inventory-20260913.csv` — originals `041–159`;
- [BATCH-20260913.md](BATCH-20260913.md) — batch history and counts;
- `derived/component-inventory/manifest.csv` — derivatives `160–228`;
- `derived/component-inventory/SHA256SUMS.txt` — derivative integrity hashes.

## Language and path convention

Repository directory names, filenames, document filenames and repository documentation use **English**. Public blog content may be bilingual as defined by the roadmap.

## Next stage

Stage 02 will use this archive to reconstruct the printer's original mechanical geometry before modernization. Reassembly evidence should be stored as a new stage/batch rather than changing Stage 01 originals.
