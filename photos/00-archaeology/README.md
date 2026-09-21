# Archaeology photo archive

This directory contains the photographic evidence collected during **Stage 00 — Archaeology** of Prusa i3 Revival 2026.

## Originals

`originals/` currently contains **89 JPEG files**, with two distinct provenance groups:

- **80 historical baseline photographs**, ARQ 001–080, captured during the archaeology work on 12–13 September 2026 and committed without intentional image editing or recompression. This remains the frozen baseline.
- **Nine later spare-box photographs**, `ARQ-20260915-081`–`ARQ-20260915-089`, published after metadata sanitization. Their legacy `originals/` location does not make them untouched camera originals. The [spare-box record](../../docs/00-archaeology/06-motion-electronics-spares.md) records their recovery and processing.

This summary was reconciled with the [current photo catalogue](../../docs/00-archaeology/02-photo-catalogue.md) and repository files on 21 September 2026. No evidence files or permanent IDs were changed.

Their filenames use the legacy permanent identifier format:

`ARQ-YYYYMMDD-NNN-<capture-or-source-id>.jpg`

`ARQ` is retained as an opaque historical ID prefix because these identifiers were already established as the canonical evidence references. All descriptive repository paths, document names and new filenames are standardised in English.

## Evidence classes

The archive intentionally mixes several kinds of discoveries made during the archaeology sessions. A photograph does **not** prove that the pictured object was installed on the printer.

- **PRINTER-AS-FOUND** — component visibly installed on the printer before dismantling.
- **LOOSE-FOUND** — loose component found in boxes from the same period.
- **DONATED-PURCHASED** — component known to have been donated or purchased at the time.
- **PERIOD-UNRELATED** — period hardware not known to belong to the printer, but retained as technological context.
- **UNKNOWN** — provenance or function still unresolved.

## Preservation policy

Do not edit, overwrite, rotate destructively or recompress files in `originals/`. Crops, annotations, web versions and comparison images belong in `derived/`.

## Documentation

See:
- [Archaeology documentation](../../docs/00-archaeology/README.md)
- [Photo catalogue](../../docs/00-archaeology/02-photo-catalogue.md)
- [Evidence rules](../../docs/00-archaeology/03-method-and-provenance.md)
- [Blog source notes](../../docs/00-archaeology/04-blog-source-notes-chapter-0.md)
