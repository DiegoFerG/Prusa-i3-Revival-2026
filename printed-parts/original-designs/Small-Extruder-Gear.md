---
type: part
area: extrusion
status: under-study
phase: stage-02
priority: high
generation: original
updated: 2026-09-19
---

# Small Extruder Gear

[Open the original small-gear STL](upstream/jonaskuehling-18379/files/smallgearmod_fixed.stl)

This is the metric small herringbone gear from **Jonas Kühling's Greg's Wade Reloaded**, [Thingiverse 18379](https://www.thingiverse.com/thing:18379), paired with [biggearmod_fixed.stl](upstream/jonaskuehling-18379/files/biggearmod_fixed.stl). The author describes a 9/47 gear pair. The large member is a strong visual match to the recovered five-hole gear. This makes the small member a good candidate; physical compatibility has not yet been established.

## Open it in Bambu Studio

1. In Obsidian, use `Ctrl+O`, search `Small-Extruder-Gear`, and open this note. It is also linked from [Phase H](../../docs/knowledge-base/build/Phase-H.md) and [Parts](../../docs/knowledge-base/indexes/Parts.md).
2. Follow the STL link. If your system opens a different application, open Bambu Studio and import the file from `printed-parts/original-designs/upstream/jonaskuehling-18379/files/smallgearmod_fixed.stl` inside this repository.
3. Keep 100% scale. The original mesh bounding box is approximately **20.00 × 19.89 × 21.25 mm** in its stored orientation. STL has no explicit units; these historical models use millimetres. A large scale discrepancy should be resolved before slicing.
4. Compare the physical gear's tooth count, shaft bore, hub height, grub-screw/nut trap and the large gear's tooth geometry. Confirm the 9/47 pair and motor-to-hobbed-bolt spacing. The separately archived `small-gear-mod_holedia-4-2.stl` is a different bore variant.
5. Select the P1S and the real material/nozzle in use. Inspect the layer preview, bore and teeth before printing. The [project policy](../../docs/02-reassembly/README.md#temporary-replacement-parts-during-reassembly) allows ABS for a temporary Stage 02 replacement when ASA is unavailable.
6. Record the chosen source/hash, material, orientation, print settings, measured dimensions and mechanical fit after the test. Store a saved 3MF/profile as a new project artifact; preserve the source STL unchanged.

The archive has been checked for file integrity and readable STL geometry. It has not been sliced, printed or fit-tested on this printer. A successful print alone does not establish correct meshing.

[Catalogue](Original-Printed-Parts.md#gregwade-extrusion) · [Provenance](Provenance.md) · [Extrusion system](../../docs/knowledge-base/systems/Extrusion.md)
