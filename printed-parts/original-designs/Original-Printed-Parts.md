---
type: catalogue
area: mechanics
status: under-study
phase: stage-02
priority: high
generation: original
updated: 2026-09-19
---

# Original Printed Parts

[Archive](README.md) · [Small extruder gear](Small-Extruder-Gear.md) · [Provenance](Provenance.md) · [Build phases](../../docs/knowledge-base/build/Build.md)

This catalogue maps historical design files to assembly roles. Quantities describe the conventional assembly, not a new physical inventory. `Visual candidate` means the published shape agrees with visible evidence but dimensions and fit remain unchecked. `Family reference` means a relevant original design without an established match to the recovered part. No item is marked fit-tested.

## X, Y and Z structure

These STL files come from the historical [Clone Wars single-frame collection](https://github.com/Obijuan/Clone-wars/tree/b0bf2cafcef9b367e14d01f21bb3a408e5ffa054/Printers/Prusa3/Single_frame). They complement the archived Josef Prusa sources. The collection is not a modern MK2/MK3/MK4 or a P3Steel set.

| Part / phase | Published STL | Conventional quantity | Match and checks |
| --- | --- | --- | --- |
| Y corners / A–B | [y-corners.stl](upstream/clone-wars/Printers/Prusa3/Single_frame/y-corners.stl) | 4 | Family reference; check M10 longitudinal rods, M8 cross-rods and 8 mm smooth-rod seats against recovered corners. |
| Y motor bracket / C | [y-motor.stl](upstream/clone-wars/Printers/Prusa3/Single_frame/y-motor.stl) | 1 | Family reference; [three-hole alternative](upstream/clone-wars/Printers/Prusa3/Single_frame/Extras/y-motor.stl) is also archived. Compare mounting holes and belt line. |
| Y idler / C | [y-idler.stl](upstream/clone-wars/Printers/Prusa3/Single_frame/y-idler.stl) | 1 | Family reference; verify bearing, axle diameter and clearance. |
| Y belt holder / C | [y-belt-holder.stl](upstream/clone-wars/Printers/Prusa3/Single_frame/y-belt-holder.stl) | 1 | Family reference; compare tooth pitch with the original T2.5 belt and carriage mounting. |
| Z lower motor mounts / E | [z-axis-bottom.stl](upstream/clone-wars/Printers/Prusa3/Single_frame/z-axis-bottom.stl) | 1 plate containing both sides | Family reference; inspect the two objects, frame holes and motor/rod alignment before printing. |
| Z upper rod holders / G | [z-axis-top.stl](upstream/clone-wars/Printers/Prusa3/Single_frame/z-axis-top.stl) | 1 plate containing both sides | Visual candidate: open rod seat and two recessed frame fasteners resemble [TD-102](../../photos/02-teardown/originals/TD-20260913-102-red-printed-structural-part-01.jpg). Measure hole spacing and rod offset. |
| X end, motor side / F | [x-end-motor.stl](upstream/clone-wars/Printers/Prusa3/Single_frame/x-end-motor.stl) | 1 | Family reference; check LM8UU seats, 45 mm rod spacing, Z nut location and motor plate. |
| X end, idler side / F | [x-end-idler.stl](upstream/clone-wars/Printers/Prusa3/Single_frame/x-end-idler.stl) | 1 | Visual candidate: split vertical bearing sleeve and nut seat resemble [TD-073](../../photos/02-teardown/originals/TD-20260913-073-red-printed-part-05.jpg). Verify bearing/axle sizes and rod spacing. |
| X carriage / F–H | [x-carriage.stl](upstream/clone-wars/Printers/Prusa3/Single_frame/x-carriage.stl) | 1 | Family reference; compare with the [V2 alternative](upstream/clone-wars/Printers/Prusa3/Single_frame/x-carriageV2.stl). Do not choose by filename alone: compare extruder mounting and T2.5 belt attachment. |
| Jonas extruder adapter / H | [jonas_mount_i3.stl](upstream/clone-wars/Printers/Prusa3/Single_frame/Extras/jonas_mount_i3.stl) | As required by selected carriage | Family reference; the presence of this adapter in the archive does not prove it was fitted to this printer. |

## Greg/Wade extrusion

The following files were downloaded directly from [Jonas Kühling's Thingiverse publication 18379](https://www.thingiverse.com/thing:18379). Both metric gear files are also byte-identical to those in the historical Clone Wars mirror. The author specifies a **9-tooth small / 47-tooth large herringbone pair**.

| Part / phase | Published file | Match and checks |
| --- | --- | --- |
| Small motor gear / H | [smallgearmod_fixed.stl](upstream/jonaskuehling-18379/files/smallgearmod_fixed.stl) | Candidate companion to the matching large-gear design. Use the [small-gear page](Small-Extruder-Gear.md) before selecting the print. |
| Large hobbed-bolt gear / H | [biggearmod_fixed.stl](upstream/jonaskuehling-18379/files/biggearmod_fixed.stl) | Strong visual candidate: five circular lightening holes, central nut trap and herringbone teeth agree with [TD-078](../../photos/02-teardown/originals/TD-20260913-078-extruder-large-gear-front.jpg), [TD-079](../../photos/02-teardown/originals/TD-20260913-079-extruder-large-gear-rear.jpg) and [TD-080](../../photos/02-teardown/originals/TD-20260913-080-extruder-large-gear-edge.jpg). Tooth count and dimensions still need physical confirmation. |
| Hinged idler / H | [jonaskuehling_gregs-wade-v3_idler-only.stl](upstream/jonaskuehling-18379/files/jonaskuehling_gregs-wade-v3_idler-only.stl) | Strong visual candidate: the guided bearing window, hinge and open tension-screw slots resemble [TD-069](../../photos/02-teardown/originals/TD-20260913-069-red-printed-part-01.jpg). Check bearing and pivot dimensions. |
| Extruder body / H | [J-head body-only plate](upstream/jonaskuehling-18379/files/jonaskuehling_gregs-wade-v3_jhead-BODY-ONLY.stl) | Family reference with the curved motor mount seen in [TD-025](../../photos/02-teardown/originals/TD-20260913-025-extruder-gears-detail.jpg). This file also contains a loose washer. The recovered E3D-family groove mount is not identified by the J-head filename. Compare mounting holes and hotend seat before selection. |
| Alternative hotend interfaces / H | [Groovemount](upstream/jonaskuehling-18379/files/jonaskuehling_gregs-wade-v3_groovemount.stl), [J-head](upstream/jonaskuehling-18379/files/jonaskuehling_gregs-wade-v3_jhead.stl), [reprapfaborg](upstream/jonaskuehling-18379/files/jonaskuehling_gregs-wade-v3_reprapfaborg.stl) | Original author variants; these are alternatives, not three installed extruders. Inspect each plate's objects and sacrificial support geometry. |
| Historical layer-specific export / H | [J-head LAYER-0-35](upstream/jonaskuehling-18379/files/jonaskuehling_gregs-wade-v3_jhead-LAYER-0-35.stl) | Alternative export; author notes tie support membranes to layer thickness. This is not a P1S profile. |
| Non-default gear and imperial variants | [4.2 mm small gear](upstream/jonaskuehling-18379/files/small-gear-mod_holedia-4-2.stl), [SAE large gear](upstream/jonaskuehling-18379/files/big-gear-mod_SAE.stl), [SAE body](upstream/jonaskuehling-18379/files/jonaskuehling_gregs-wade-v3_SAE_groovemount.stl) | Preserved to keep the author's file set complete. These are not the default candidates for this metric machine. |

Editable body sources and their dependencies are in [the original SCAD entry point](upstream/jonaskuehling-18379/files/jonaskuehling_gregs-wade-v3.scad). This package does **not** contain editable source for the exact two gear meshes; the original STLs are preserved instead.

## Auxiliary parts and coverage gaps

| Role | Archived source or evidence | Remaining work |
| --- | --- | --- |
| Belt bearing guides / C–F | [Original belt-guide SCAD](upstream/josefprusa-prusa3/old_single_plate/src/belt-guide.scad) | Source archived; export the measured bearing/axle variant separately if needed. |
| Fan mount | [Original fan-mount SCAD](upstream/josefprusa-prusa3/old_single_plate/src/fan-mount.scad) | Family reference only. This does not identify the recovered hotend's fan duct. |
| Magnetic endstop holder | [Original magnetic-holder SCAD](upstream/josefprusa-prusa3/old_single_plate/src/magnetic-holder.scad) | Historical alternative; do not substitute it for the recovered mechanical-switch arrangement. |
| Mechanical endstop clamps / I | [Endstop-holder SCAD](upstream/josefprusa-prusa3/box_frame/extras/endstop-holder.scad), [90-degree adapter SCAD](upstream/josefprusa-prusa3/box_frame/extras/endstop-holder-extra.scad) | Original family sources archived; match clamp diameter, PCB hole pitch and actuation geometry to the actual holders before creating an export. |
| Hotend-specific clamp/duct | [Installed extruder evidence](../../photos/02-teardown/originals/TD-20260913-025-extruder-gears-detail.jpg) and [legacy hotend identification](../../docs/knowledge-base/systems/Extrusion.md) | Exact original variant remains unresolved. The Rework Magma body/duct must not be presented as an E3D replacement. |
| Loose black brackets and blocks / A–J | [Original teardown index](../../photos/02-teardown/INDEX.md), especially TD-081–101 and TD-113–114 | Attribution and installed-versus-spare status require individual matching. Similarity to a motor bracket is not enough to assign every loose piece to the original build. |

All 12 STL files in the selected Clone Wars single-frame directory and all 17 design files in Jonas's publication are present. That completes those **published file sets**, while the exact physical-part inventory remains open for the auxiliary pieces above. Record measurements and successful fit against the part's existing inventory entry; do not rename historical photo IDs.

For Bambu Studio, start from the linked STL at 100% scale, inspect the objects and dimensions, and use the P1S with the actual filament loaded in that printer. The Revival's legacy 3 mm filament path is a property of the part being reproduced, not the P1S filament setting. Follow the [Stage 02 replacement policy](../../docs/02-reassembly/README.md#temporary-replacement-parts-during-reassembly).
