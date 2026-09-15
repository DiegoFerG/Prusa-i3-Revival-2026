# Original Prusa i3 Reassembly Manual — Revival 2026

> Historical reconstruction guide for Stage 02. This manual intentionally approaches the printer as it would have been assembled in the 2012–2014 RepRap era, while using the recovered printer itself as the final authority.

## 1. Purpose and evidence hierarchy

This manual reconstructs the original mechanical Prusa i3 before modernization. It is not a generic modern i3 guide.

Evidence priority:

1. Stage 00/01 photographs and measured recovered components.
2. Teardown sequence and component-inventory records.
3. Contemporary 2012–2014 assembly sources.
4. Later derivative documentation only where it explains an unchanged mechanical principle.

Every instruction is tagged conceptually as one of:

- **Observed** — visible or measured on this printer.
- **Probable** — strongly supported by period documentation and the recovered parts, but still to be verified during assembly.
- **Future improvement** — recorded for later stages and not applied here.

## 2. Historical fit of this machine

The recovered hardware aligns unusually closely with the Spanish community Prusa i3 build documented by SpainLabs on 3 August 2013. That guide lists 2× M5×310 mm Z threaded rods, 4× M8×200 mm Y cross rods, 2× M10×350 mm Y longitudinal rods, 10× LM8UU and 3× 608ZZ bearings. The same discussion references 2.5 A / 1.8° motors and 5-to-5 mm Z couplers. Those values closely match this printer's recovered hardware.

This makes the SpainLabs guide a strong historical clue, but not an authority over the physical evidence. The recovered smooth-rod lengths, belt type, printed parts and exact frame geometry differ from several published variants.

## 3. Tools and preparation

Prepare a clear bench and keep the Stage 01 photographs accessible.

Recommended hand tools:

- metric hex keys;
- 5.5 mm, 8 mm, 13 mm and 17 mm spanners/nut drivers as required by the recovered fasteners;
- small adjustable spanner;
- screwdrivers;
- vernier caliper;
- steel ruler;
- engineer's square;
- marker and removable labels;
- side cutters for temporary cable ties;
- lint-free cloths and suitable cleaning supplies;
- appropriate lubricant for the linear guides, applied only after bearing condition is assessed.

Do not connect the PSU to mains power during Stage 02.

## 4. Stage A — Y-frame structural base and steel frame

### Parts to prepare

- 2× M10×350 mm threaded rods;
- 4× M8×200 mm threaded rods;
- four original Y-corner printed parts;
- original Y motor support and Y idler support;
- M8/M10 nuts and washers from the recovered fastener set;
- single-sheet steel vertical frame.

### Historical reconstruction logic

**Observed:** the recovered inventory contains the same M10×350 and M8×200 threaded-rod pattern as the 2013 SpainLabs guide. `TD-20260913-005` and `TD-20260913-021` record the assembled lower structure before teardown.

**Probable:** the base should first be assembled as two M8 cross-members — one carrying the Y idler and one carrying the Y motor support — and then joined by the two M10 longitudinal rods. This is the sequence used in the contemporary SpainLabs instructions and is mechanically consistent with the recovered parts.

### Assembly

1. Lay out the four M8×200 rods in two pairs. Do not tighten anything fully yet.
2. Identify the original front/idler support by comparison with `TD-005`, `TD-021` and `TD-038`.
3. Fit the idler support approximately at the centre of its M8 pair, using a washer and nut on each side of the printed part where the original geometry shows this arrangement.
4. Fit two Y-corner pieces to the ends of that M8 pair.
5. Repeat with the rear pair using the Y motor support and the remaining two Y corners.
6. Pass the two M10×350 rods through the four Y corners to connect the front and rear assemblies.
7. Before closing the M10 ends, install the inner washers/nuts that will later clamp the steel frame. Contemporary 2013 instructions explicitly placed these near the middle before final assembly because they cannot be added later without dismantling the base.
8. Place the steel frame between the inner washer/nut pairs, matching the orientation visible in the teardown photographs. Do not yet assume equal distances from the rod ends; reproduce the photographed geometry.
9. Square the Y rectangle. Measure both diagonals and adjust until they are equal within practical measurement error.
10. Confirm that the two M10 rods are parallel and that the M8 front/rear cross-members are perpendicular to them.
11. Only then progressively tighten the structural nuts, alternating sides so the plastic corners are not twisted.

### Stop-and-check gate

Before continuing, photograph the complete base from above and from both sides. The steel frame must stand perpendicular to the Y base without visible twist.

**Future improvement:** none applied. Later stages may replace fatigued printed corners or change structural hardware, but Stage 02 preserves the original architecture.

## 5. Stage B — Y linear guides and bed carriage

### Parts to prepare

- recovered Y smooth-rod pair — currently catalogued as the probable Ø8×350 mm pair;
- Y carriage plate (~220×220 mm, ~210 mm mounting-hole spacing, ~6 mm thick);
- 3× LM8UU for Y;
- original LM8UU retention method/hardware;
- Y belt holder.

### Assembly

1. Use the pre-teardown photographs to determine which side of the Y carriage faced upward.
2. Install three LM8UU bearings in the same 1+2 arrangement visible in the original build. Do not substitute a four-bearing layout.
3. If the original carriage used cable ties through slots to hold the LM8UU bearings, reproduce that only for the historical reconstruction; use new ties rather than brittle old ones.
4. Install the Y belt holder in its original position and orientation.
5. Clean the two probable Y rods and inspect for scoring, corrosion or bends before inserting them.
6. Slide the rods through the LM8UU bearings gently. Never hammer a rod through a bearing.
7. Seat the smooth rods into the Y-corner grooves/retainers as shown by the original geometry.
8. Move the carriage by hand through the entire travel. It must move freely without forcing either rod inward or outward.
9. If motion binds, loosen the Y-frame nuts and align the frame around the carriage rather than forcing the bearings to compensate for a skewed base.

### Bearing classification

Classify each LM8UU as **REUSE**, **RESTORE** or **REPLACE** according to noise, roughness, play and visible damage. Do not lubricate a visibly damaged bearing as a substitute for replacement.

## 6. Stage C — Y motor, idler and T2.5 transmission

### Parts to prepare

- 1× Wantai 42BYGHW811 motor;
- original Y motor bracket already installed in the base;
- T2.5 ~20-tooth drive pulley;
- original Y idler hardware;
- appropriate FAG 608Z bearing if confirmed by photographs for this location;
- T2.5 belt.

### Assembly

1. Compare motor orientation with `TD-021`, `TD-032` and `TD-038` before installing it.
2. Mount the motor loosely enough to permit pulley alignment.
3. Fit the T2.5 pulley with its teeth in the same belt plane as the carriage belt holder.
4. Reconstruct the front idler from the photographs. Do not substitute the 623ZZ arrangement shown in some contemporary manuals if the recovered machine used a 608Z.
5. Route the T2.5 belt around the motor pulley and idler, with the toothed face engaged on the drive pulley.
6. Attach both belt ends to the original Y belt holder.
7. Align the belt so its long runs are parallel to the Y rods and approximately horizontal.
8. Tension only enough to remove slack. Period instructions consistently warn against an over-tight belt; the carriage must remain smooth over full travel.

**Observed:** the recovered belt and pulley are T2.5, not GT2. Period sources that show GT2 are useful for routing logic only.

## 7. Stage D — Heated bed, levelling springs and mirror

### Parts to prepare

- original heated-bed PCB;
- four original long M3 bed screws;
- original levelling springs, including the repurposed clothes-peg springs;
- washers/nuts as documented;
- one IKEA SÖRLI 200×200×3 mm mirror;
- original mirror clips if recovered and serviceable.

### Assembly

1. Confirm which face of the Y carriage is uppermost from the teardown photos.
2. Insert the four levelling screws through the carriage/bed mounting points in the original direction.
3. Recreate the original spring stack at all four corners. Do not replace the springs yet; their unusual origin is part of the documented machine history.
4. Install the heated bed mechanically but do not connect its wiring.
5. Compress the springs only enough to make the bed stable while leaving useful adjustment travel in both directions.
6. Place the SÖRLI mirror on the bed and secure it using the original clip arrangement if that arrangement can be proven from photographs.
7. Check that no clip can collide with the nozzle path at the future print limits.

**Future improvement:** purpose-made bed springs/spacers and a modern build surface may be evaluated after the original baseline is reconstructed.

## 8. Stage E — Z lower mounts, motors and smooth guides

### Parts to prepare

- 2× Wantai 42BYGHW811 motors;
- original lower Z motor mounts;
- probable Z smooth rods — catalogued Ø8×330 mm;
- Z top supports;
- 4× LM8UU assigned to the X-end assemblies;
- 2× flexible aluminium Z couplers;
- 2× M5×310 mm threaded rods.

### Assembly

1. Identify left/right Z mounts using `TD-003` through `TD-012` and `TD-030` where relevant.
2. Mount both lower Z motor brackets to the steel frame in their original holes and orientation.
3. Install the two Z motors but leave final motor/bracket tightening until rod alignment is checked.
4. Install the two smooth Z rods in the lower mounts.
5. Fit the upper Z supports while ensuring each smooth rod remains straight and unstressed.
6. The smooth rods must be parallel to one another and approximately perpendicular to the Y plane.
7. Do not install the M5 threaded drive rods permanently until the X gantry ends have been prepared.

## 9. Stage F — X ends, X carriage and X guide rods

### Parts to prepare

- X-end motor printed part;
- X-end idler printed part;
- remaining LM8UU bearings for the X ends;
- X carriage with its 3× LM8UU bearings;
- recovered probable X smooth-rod pair — catalogued Ø8×317 mm;
- X motor;
- T2.5 pulley;
- X idler bearing/hardware;
- X belt.

### Assembly

1. Reconstruct the X-end idler using the bearing and fastener arrangement visible in the teardown photos.
2. Insert the LM8UU bearings into the two X ends in the same orientation used originally.
3. Install the M5 drive nuts in the X ends if the original parts use trapped M5 nuts. Period i3 instructions placed these nuts before the X/Z marriage because access becomes difficult later.
4. Install 3× LM8UU into the X carriage using the original retention method.
5. Pass the two X smooth rods through the carriage bearings.
6. Fit the X-end motor and X-end idler to the rod ends. Use `TD-027`, `TD-028` and `TD-030` to establish which side contains the motor.
7. Move the X carriage by hand through the complete span before tightening anything that could distort the rod spacing.
8. Mount the X motor and T2.5 pulley.
9. Route the X belt around the motor pulley and idler and secure it to the X carriage in the original fashion.
10. Tension only enough to remove backlash without increasing carriage drag.

## 10. Stage G — Join X gantry to Z

1. With both Z smooth rods installed, slide the X-end LM8UU bearings onto the Z rods simultaneously.
2. Lower both sides evenly; never force one side far ahead of the other.
3. Insert the two M5×310 threaded rods through the trapped M5 nuts in the X ends.
4. Connect each M5 rod to its Z motor using the recovered flexible aluminium coupling.
5. Before tightening coupler screws, align each threaded rod as closely as possible with its motor shaft and the associated Z smooth rod.
6. Turn both M5 rods by hand together and raise/lower the X gantry. It should move without periodic binding.
7. Level the X gantry relative to the Y carriage by turning the two Z screws independently by hand.

**Observed:** this printer uses aluminium flexible couplers. Some 2013 guides used short rubber hose; that is historical context only and is not reproduced here.

**Future improvement:** Stage 03 will replace the M5 threaded rods with proper leadscrews only after the original geometry is validated.

## 11. Stage H — Wade-style geared extruder and legacy 3 mm hotend

### Parts to prepare

- Wade/Greg's-Wade-family extruder body;
- large printed gear;
- small motor gear;
- hobbed bolt and associated washers/nut/bearings;
- idler assembly, tension screws and springs;
- extruder NEMA17 motor;
- legacy E3D-family groove-mount hotend;
- hotend fan/supports as originally fitted;
- thermistor and captive heater cartridge retained for documentation.

### Historical assembly logic

Period Prusa Mendel instructions recommended assembling the hotend to the Wade body and mounting the body to the carriage before finally fitting the motor, large gear/hobbed bolt and idler. This avoids losing access to mounting screws.

### Assembly

1. Compare the complete extruder against `TD-002`, `TD-023` through `TD-025`, `TD-039` and `TD-040` before separating subcomponents further.
2. Build the hobbed-bolt/large-gear stack using the same washer and bearing order visible in the teardown evidence.
3. Install the idler bearing and hinge/tension hardware.
4. Do not fully compress the idler springs yet.
5. Mount the E3D-family hotend in the original groove-mount position beneath the extruder body.
6. The heater cartridge remains captive in the heater block because its retaining screw head is damaged. Do not attempt destructive removal during Stage 02.
7. Mount the extruder body to the X carriage in the original orientation.
8. Mount the extruder motor and small gear.
9. Mesh the small and large gears with a small amount of backlash; they must not bind.
10. Align the hobbed section of the drive bolt with the 3 mm filament path.
11. Tighten the idler springs evenly until the idler can grip filament, but leave final extrusion pressure to commissioning.
12. Refit the heatsink fan/support arrangement as documented.

No heater or thermistor wiring is energized in Stage 02.

## 12. Stage I — Endstops

### Parts to prepare

- original mechanical X, Y and Z endstop modules;
- their original printed mounts/fasteners.

### Assembly

1. Use `TD-009`, `TD-035` and the teardown endstop series around `TD-147…154` to identify each switch and mount.
2. Install X, Y and Z switches mechanically in their photographed positions.
3. Move each axis slowly by hand and confirm that the switch is physically actuated before any hard collision occurs.
4. Do not infer electrical NO/NC wiring from physical orientation; electrical validation belongs to a later stage.

## 13. Stage J — Electronics placement, historical only

### Parts to prepare

- Arduino Mega 2560;
- StaticBoards RAMPS 1.4SB;
- four A4988-family drivers;
- LCD and RAMPS adapter;
- original controller cooling fans/supports;
- JCPOWER JC-360-12 PSU only for mechanical positioning.

### Assembly

1. Use `TD-013` through `TD-020`, `TD-026`, `TD-029`, `TD-031` and the cleaned inventory photographs to reproduce component locations.
2. Use insulating spacers where the original electronics were mounted to the metal frame.
3. Position the PSU mechanically only if useful for reconstructing the original machine layout.
4. Keep all mains terminals disconnected and protected from accidental contact.
5. The original mixed wiring harness is reference evidence only and is **not reused**.

## 14. Final Stage 02 mechanical checks

Do not proceed to electrical work until all checks pass:

- Y-frame diagonals agree and the steel frame is square to the base;
- Y carriage travels end-to-end with no tight spot;
- X carriage travels end-to-end with no tight spot;
- X gantry rises and falls by turning both Z screws manually;
- X and Y belts stay in their pulley/idler planes;
- pulleys are secure on motor shafts;
- no LM8UU is forced sideways by misaligned rods;
- heated bed is stable and has useful levelling travel;
- each endstop is reached before a mechanical crash;
- extruder gears turn freely by hand;
- hotend is mechanically secure;
- loose wiring cannot enter belts, gears or fans.

At this point the printer should look and move like the historical machine, but it is still an unpowered mechanical reconstruction.

## 15. Component condition log

For every component touched during Stage 02 record one primary state:

- **REUSE** — acceptable after inspection;
- **RESTORE** — requires cleaning, lubrication or repair before reuse;
- **REPLACE** — equivalent replacement required for the original baseline;
- **REDESIGN** — intentionally deferred to a modernization stage;
- **ARCHIVE** — retained mainly as historical evidence.

Use notes to distinguish cleaning, lubrication and repair work without expanding the repository's primary status vocabulary.

## 16. Historical references

See `historical-references.md` for the complete source index and licensing notes. The most influential sources for this reconstruction are:

- SpainLabs, **Manual de montaje Prusa i3**, 3 August 2013;
- RepRap Magazine Issue 2, **Prusa i3 visual instructions**, June 2013;
- RepRap / Clone Wars, **Prusa iteration 3** documentation;
- Josef Prusa, **Prusa3** GPLv3 repository;
- RepRap Wiki, **Prusa Mendel Assembly (iteration 2)** for Wade-extruder practice;
- RepRap / Clone Wars, **MONTAJE PRUSA i3 MARCO DE MADERA** as a secondary period mechanical reference.

The sources explain contemporary assembly practice; the recovered printer determines the final answer whenever variants conflict.
