# Stage 02 — Reassembly photo archive

This directory contains privacy-sanitized photographic evidence for **Stage 02 — Original mechanical reassembly** of Prusa i3 Revival 2026.

## Batches

- Imported batches: **4**
- Imported photographs: **116**
- Naming prefix: `RA` = Reassembly
- Available ID ranges:
  - `RA-20260914-001` through `RA-20260914-035`
  - `RA-20260915-001` through `RA-20260915-009`
  - `RA-20260916-001` through `RA-20260916-058`
  - `RA-20260921-001` through `RA-20260921-014`

## Repository path

Sanitized evidence images are stored in:

`photos/03-reassembly/derived/reassembly-evidence/`

## Naming convention

`RA-YYYYMMDD-NNN-stage-x-subsystem-description.jpg`

## Documentation

- `manifest.csv` — cumulative photo inventory, provenance, dimensions and SHA-256. Empty `source_pixel_sha256` cells in the 21 September batch mean the pre-encoding source hash is unavailable; all repository JPEG hashes are present.
- `INDEX.md` — archive summary grouped by reconstruction stage.
- `BATCH-20260914.md` — initial Stage A archive.
- `BATCH-20260915.md` — final Stage A additions.
- `BATCH-20260916.md` — Stage B–G reconstruction batch.
- `BATCH-20260916-classification.csv` — per-image stage classification for the B–G batch.
- [21 September batch](BATCH-20260921.md) — Stage H geared-extruder assembly, photo links and remaining checks.
- [Stage H classification](BATCH-20260921-classification.csv) — per-image descriptions for the latest batch.
- `derived/reassembly-evidence/SHA256SUMS.txt` — cumulative integrity hashes.

All repository JPEGs are privacy-sanitized evidence copies. Generated illustrations and manual renders are excluded.
