---
type: archive
area: mechanics
status: under-study
phase: stage-02
generation: original
updated: 2026-09-19
---

# Original design archive

Local copies of historical Prusa i3 single-sheet and Greg/Wade designs, recovered on 19 September 2026. Start with the [original printed-parts catalogue](Original-Printed-Parts.md), or go directly to the [small extruder gear](Small-Extruder-Gear.md).

The archive contains **62 unchanged upstream files: 23 STL files, 31 SCAD files, two configuration templates and six documentation/build files**, approximately 7.64 MB. STL count includes alternative versions and plates containing multiple objects; it is not a count of installed parts.

These are authentic published designs, not yet a fully verified set of exact replacements for this individual printer. The supplier and exact kit revision are unknown. The catalogue records the strongest matches, alternatives and remaining gaps. No reprint, fit test or new assembly completion is implied.

| Collection | Contents | Use |
| --- | --- | --- |
| [Original printed parts](Original-Printed-Parts.md) | Links by assembly role and phase | Find a part without searching filenames |
| [Small extruder gear](Small-Extruder-Gear.md) | Direct STL link, matching gear and inspection checklist | Prepare the Stage H replacement in Bambu Studio |
| [Provenance and licenses](Provenance.md) | Authors, pinned revisions, retrieval, exclusions and license notices | Distinguish original files from later project work |
| [Manifest](manifest.json) | Source path, byte count and SHA-256 for every imported file | Check archive integrity |
| [Verification tool](verify_archive.py) | Standard-library Python archive and STL checks | Recheck after copying or updating the archive |

## Preservation and future changes

Keep `upstream/` byte-for-byte unchanged, including original filenames and notices. Do not repair, rescale or overwrite an upstream STL. Store a modified replacement in a separate project design directory with its parent file/hash, changes, dimensions and print/fit results. Update this catalogue and the affected knowledge-base pages in the same change.

The original SCAD configuration templates must be copied and deliberately configured in a **separate working copy** before compilation. They are not P1S printer profiles. The old single-plate template uses T2.5; the separate `box_frame` template has other defaults and must be checked before generating endstop holders. See [provenance](Provenance.md#editable-sources-and-dependencies).

[Printed parts](../README.md) · [Parts index](../../docs/knowledge-base/indexes/Parts.md) · [Stage 02](../../docs/knowledge-base/build/Stage-02-Original-Reassembly.md)
