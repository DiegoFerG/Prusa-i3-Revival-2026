# Stage 02 — Reassembly photo archive

This directory contains privacy-sanitized photographic evidence for **Stage 02 — Original mechanical reassembly** of Prusa i3 Revival 2026.

## Batch

- Capture/context date: **14 September 2026**
- Imported photographs: **35**
- Naming prefix: `RA` = Reassembly
- Current batch range: `RA-20260914-001` through `RA-20260914-035`

## Repository path

Sanitized evidence images are stored in:

`photos/03-reassembly/derived/reassembly-evidence/`

The user's untouched source files are intentionally **not** included in the repository package because some phone/camera files may contain private metadata.

## Privacy and integrity processing

Every repository JPEG in this batch was:

1. decoded from the uploaded source image;
2. orientation-normalized using EXIF orientation when present;
3. converted to RGB pixel data;
4. re-encoded as high-quality JPEG;
5. written without EXIF, GPS, XMP, ICC profile, device or camera metadata.

No generative edit, object removal, crop, resize or content-changing operation was applied.

## Naming convention

`RA-YYYYMMDD-NNN-subsystem-description.jpg`

Where:

- `RA` = Reassembly;
- `YYYYMMDD` = reassembly capture/context date;
- `NNN` = stable identifier within the Stage 02 batch;
- `subsystem-description` = concise English description.

## Documentation

- `manifest.csv` records original filename, sanitized filename, dimensions and SHA-256.
- `derived/reassembly-evidence/SHA256SUMS.txt` provides integrity hashes for every repository JPEG.
- `BATCH-20260914.md` describes the batch and evidence scope.

## Evidence scope

This batch covers:

- Stage A component references;
- M10 side rods and frame-clamping hardware;
- paired M8 Y-axis crossmembers;
- front Y idler support and pulley references;
- rear Y motor support references;
- rectangular Y-frame reconstruction;
- installation of the original black steel single-plate frame.

Generated illustrations, manuals and assistant-created diagrams are **not** part of this evidence archive.
