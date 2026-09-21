---
type: reference
area: documentation
status: documented
phase: stage-02
generation: original
updated: 2026-09-19
---

# Original designs — provenance and licenses

[Archive](README.md) · [Catalogue](Original-Printed-Parts.md) · [Manifest](manifest.json)

## Retrieval and scope

Retrieved on **19 September 2026** in response to the missing original-printable-parts archive. The owner does not remember the kit supplier. No invoice, designer attribution or exact variant identifier was recovered. The reference machine remains the one documented in the [hardware baseline](../../hardware/README.md), rather than a newly assigned commercial model.

Every imported file has an entry in `manifest.json` with its original source/path, revision when available, byte count and SHA-256. Git blobs were copied directly at the pinned revisions; Thingiverse files were extracted from the author's downloaded package. No meshes were repaired, rescaled, regenerated or renamed. The enclosing collection directories are local archive names. `.gitattributes` disables line-ending conversion within `upstream/` so checksums remain stable.

Upstream Git metadata and ignore rules are excluded from the selection; they are not part designs and must not change this repository's tracking behavior.

| Source | Pinned identity | Archived selection |
| --- | --- | --- |
| [Josef Prusa / Prusa3](https://github.com/josefprusa/Prusa3/tree/7ab0186d94b4a9af7c4d832b6a4f0245dd165bc1) | Commit `7ab0186d94b4a9af7c4d832b6a4f0245dd165bc1`, 27 January 2015 | Original README/license, `old_single_plate` printable sources and dependencies, plus the two `box_frame` endstop sources and their configuration/library dependencies. Metal-frame drawings and other printer families are excluded. |
| [Obijuan / Clone-wars](https://github.com/Obijuan/Clone-wars/tree/b0bf2cafcef9b367e14d01f21bb3a408e5ffa054/Printers/Prusa3/Single_frame) | Commit `b0bf2cafcef9b367e14d01f21bb3a408e5ffa054`, 7 October 2014 | Every STL in `Printers/Prusa3/Single_frame`, including its `Extras` directory: 12 files. This is a historical distribution mirror, not a claim that Obijuan designed every part. |
| [Jonas Kühling / Greg's Wade Reloaded](https://www.thingiverse.com/thing:18379) | Thingiverse 18379, published 1 March 2012; downloaded 19 September 2026 | All 17 design files plus package README and LICENSE: 11 STL and 6 SCAD. Package images are not imported. Per-file hashes pin this downloaded version. |

The two metric gear files from the author's package are byte-identical to `Printers/Extruders/Jonaskuehling/stl/stl/{smallgearmod_fixed,biggearmod_fixed}.stl` at the pinned Clone Wars revision. Only one copy of each is stored here.

## Attribution and notices

- **Josef Průša and contributors:** original i3 structural sources. The repository and source headers state GNU GPL v3; the full [upstream license](upstream/josefprusa-prusa3/LICENSE.md) and notices are preserved. The additional endstop rotator credits **Ethan Sherman** in its source header. Retain those notices with derived exports and provide their corresponding source.
- **Clone Wars / Obijuan and contributors:** historical STL collection. The selected directory supplies no standalone license file or per-STL designer declaration. Its original Prusa structural lineage is supported by the [Clone Wars single-frame documentation](https://www.reprap.org/wiki/Clone_wars:_Prusa_iteraci%C3%B3n_3_single_frame) and the preserved GPL source. Exact source-to-STL equivalence and the individual author/license notices for the V2 carriage and `Extras` modifications have not been established; do not invent a blanket new license for these files. The manifest retains their precise public distribution origin.
- **Jonas Kühling (`jonaskuehling`):** Greg's Wade Reloaded and its supplied gear variants. Preserve the author's [package LICENSE](upstream/jonaskuehling-18379/LICENSE.txt) and [README](upstream/jonaskuehling-18379/README.txt). The live publication identifies **Creative Commons Attribution–ShareAlike**, linking to [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); the downloaded notice does not itself specify a version. Its SCAD files retain older **Creative Commons–GNU GPL** notices credited to **Greg Frost**. Both sets of notices are retained; this archive does not rewrite their licensing history or relicense the models.
- Jonas's publication credits **Greg Frost** for the Guidler and **Stoffel15** for the 9/47 and herringbone work: [Guidler](https://www.thingiverse.com/thing:17030), [Accessible Wade 9/47](https://www.thingiverse.com/thing:11152), [Wade Goes Fishing](https://www.thingiverse.com/thing:5268). These credits do not identify the unknown supplier of the physical kit.

## Evidence and rejected substitutions

The [catalogue](Original-Printed-Parts.md) links the actual teardown photographs used for comparison. Mesh previews were inspected locally as research aids; they are not new photographs or manufacturing validation.

- The recovered large gear has five round lightening holes and herringbone teeth. Jonas's published large gear has that layout; its paired small gear is the leading replacement candidate. Physical tooth count, bore and gear spacing remain to be checked.
- The recovered idler's guided bearing window and open screw slots agree visually with Jonas's idler. The Z upper mount and X idler-end shapes also support the classic single-sheet family. This is evidence of design lineage, not an exact kit identification.
- [eMotion-Tech Rework](https://github.com/eMotion-Tech/Prusai3_EINSTEIN_Reworked/tree/a22f00b1ea36b0c81ba73b62a3dfb91863582fdc) was examined. Its archived big gear has six teardrop-shaped openings and different dimensions, while its body/duct target a Magma hotend. These models were not imported as replacements for the recovered five-hole gear and E3D-family hotend.
- [ch1t0's i3 variants](https://www.thingiverse.com/thing:76660) were examined as the cited parent of Rework. Their body, carriage and Z stabilizers differ; they are research references, not a selected replacement set.
- The current EiNSTeiN development branch contains later modifications. It was not treated as an unchanged 2013-era kit. Modern Original Prusa MK-series files were excluded for the same identification reason.

## Editable sources and dependencies

The `old_single_plate` source tree is preserved with its `src/inc/` dependencies. In a separate working copy, copy `configuration.scad-dist` to `configuration.scad` in the `old_single_plate` directory, then review dimensions and T2.5 settings. The old README spells the template differently; use the actual archived filename. Do not assume these sources reproduce every Clone Wars revision exactly.

For the two `box_frame/extras/` endstop files, copy `configuration.scad.dist` to `configuration.scad` in a separate `box_frame` working directory, retain `inc/`, and select the actual rod/bushing configuration. The defaults are not a verified configuration for this machine.

Jonas's six SCAD files are kept together to preserve local includes. They are editable extruder-body sources. The package contains **no corresponding editable source for the exact gear STL revisions**; do not label a different 15/49 gear generator from the wider Prusa repository as their source. No STEP or P1S 3MF was supplied in these selected publications.

## Verification and open completion criteria

Run `python verify_archive.py` from this directory to check all 62 manifest entries and parse all 23 STL files for complete triangles and finite coordinates. The tool also reports bounding boxes. It does not certify manifoldness, slicing, strength, material suitability or physical fit.

The published file sets above have been archived completely within the declared selection. To complete the **exact as-built printer archive**, identify the remaining endstop mounts, hotend clamp/duct and loose accessory revisions, then link each to a measured inventory record. Keep this work open in [KB-013](../../docs/knowledge-base/project/Open-Issues.md). A downloaded candidate is not a closed identification issue.
