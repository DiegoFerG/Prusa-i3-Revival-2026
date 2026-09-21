# Generation 3 target hardware BOM

This is the target hardware set for the **Revival 2026 final build**. It records architectural selections early so later purchases and CAD decisions remain consistent. It is **not** an instruction to skip the original Arduino/RAMPS or Re-ARM generations.

See [`../docs/final-build-architecture.md`](../docs/final-build-architecture.md) for the full architecture and safety boundaries.

See [`generation-3-linear-motion.md`](generation-3-linear-motion.md) for the frozen Generation 3 linear-motion and alignment architecture.

See [`generation-3-smart-spool-system.md`](generation-3-smart-spool-system.md) for the Generation 3 spool-identification, vendor compatibility, adaptive tag learning and automatic-weighing architecture.

See [`generation-3-rass.md`](generation-3-rass.md) for the RASS active single-spool feeding, driven-spool assistance and buffer/dancer architecture.

See [`generation-3-extrusion-toolhead.md`](generation-3-extrusion-toolhead.md) for the preferred Roto + Revo Generation 3 extrusion/toolhead direction and material-use priorities.

See [`generation-3-enhancement-candidates.md`](generation-3-enhancement-candidates.md) for remaining fault-detection, cleaning, safety-control, maintenance and electrical-monitoring candidates, plus the recorded promotion of Eddy Duo probing into the frozen architecture.

See [`generation-3-procurement-status.md`](generation-3-procurement-status.md) for actual purchases, pending acquisitions and bench-test status.

## Frozen selections

| Subsystem | Target component / architecture | Status |
|---|---|---|
| Main controller | BIGTREETECH Manta M8P V2.0 | Frozen; purchased |
| Linux host | BIGTREETECH CB2 | Frozen; not yet purchased |
| Main stepper drivers | TMC2209 plug-in modules for Manta; base allocation X/Y/Z0/Z1 | Frozen architecture; 6× BTT TMC2209 V1.3 purchased (4 base + 2 spare) |
| Local display | BIGTREETECH HDMI5, 5-inch capacitive touchscreen | Frozen |
| Display integration | Custom retro/industrial ASA enclosure + KlipperScreen theme | Frozen concept |
| Toolhead MCU | BIGTREETECH EBB36 Gen2 | Frozen; purchased |
| Generation 3 extruder/hotend | E3D Roto + Revo, 1.75 mm, direct drive | Frozen architecture; current purchase preference Roto Sensored + Revo 24 V / 40 W |
| Primary material target | PLA, quality-first tuning | Frozen design intent |
| ABS/ASA target | occasional open-frame use only; no heated-chamber requirement | Frozen design intent |
| Z / bed probe | BIGTREETECH Eddy Duo eddy-current probe for fast/dense bed scanning | Frozen architecture; 5 V CAN node after EBB36 passthrough; exact mount/harness to finalise |
| Toolhead network | CAN bus | Frozen |
| CAN distribution | BIGTREETECH CEB V1.0 in electronics bay | Frozen |
| Historical mechanical skeleton | original flat steel frame + 2× M10×350 mm longitudinal threaded rods + 4× M8×200 mm transverse threaded rods | Frozen; retained as functional final structure |
| X guidance | 1× MGN12-class rail, long MGN12H-class carriage preferred | Frozen architecture |
| X rail support | commercial aluminium T-slot extrusion used as the structural X beam; 2020/2040-class family to be evaluated | Frozen concept; exact section deferred |
| Y guidance | 2× MGN12-class rails, master/slave datum strategy | Frozen architecture |
| Y rail support | 2× longitudinal commercial aluminium T-slot extrusion carriers mounted to the historical M8/M10 base through adjustable interfaces | Frozen concept; exact 2020/2040-class section deferred |
| Z guidance | 2× MGN12-class rails, primary/secondary datum strategy | Frozen architecture |
| Z rail support hierarchy | direct to steel frame if metrology permits; thin aluminium backing plate second; T-slot extrusion only if necessary | Frozen hierarchy; final implementation measurement-dependent |
| Linear-rail alignment | metallic reference surfaces, controlled adjustment/shimming as required, and independent structural locking; rails are never forced to compensate for support error | Frozen architecture |
| X/Y drive | GT2 belt drive | Frozen architecture |
| Z drive | 2× independent Tr8 lead screws and independent Z motors | Frozen architecture |
| Z geometry rule | rails define Z motion; lead screws provide vertical drive only | Frozen |
| Toolhead accelerometer | permanent LIS2DW associated with EBB36 Gen2 | Frozen |
| Bed accelerometer | BIGTREETECH S2DW V1.0 (RP2040 + LIS2DW), permanent | Frozen |
| Bed accelerometer link | USB to CB2 | Frozen |
| Smart spool system | Revival-native RFID/NFC identification with local inventory/profile mapping | Frozen architecture |
| Open smart-spool interoperability | OpenPrintTag read compatibility in the target decoder layer | Frozen architecture |
| Bambu spool compatibility | read/import supported original Bambu RFID spool data and translate to Revival model/profile | Frozen architecture |
| Additional vendor compatibility | decoder/plugin framework; Creality smart-spool RFID is a planned validation target | Frozen architecture |
| Unknown-tag learning | fingerprint readable unknown tags, allow assisted manual identification, save samples/signatures and promote validated mappings into new decoders | Frozen architecture |
| Brand database growth | create/update local brands, products, materials, spool families and tag signatures from user-confirmed observations | Frozen architecture |
| Spool weighing | integrated load cell under spool-holder load path; remaining mass = gross mass − tare | Frozen architecture |
| Spool measurement policy | stable weight readings are authoritative; dynamic printing readings are filtered/secondary | Frozen |
| Smart spool host link | local reader/weighing controller, wired USB to CB2 preferred | Frozen architecture |
| RASS active feed | single-spool active feeder near spool + driven-spool assistance | Frozen architecture |
| RASS control hierarchy | toolhead direct drive remains extrusion master; RASS follows via buffer/dancer feedback | Frozen |
| RASS tension decoupling | intermediate buffer/dancer between upstream feeder and toolhead | Frozen architecture |
| RASS fallback | passive/manual feed path remains possible if active feed subsystem is unavailable | Frozen design requirement |
| Main camera concept | fixed frame-mounted camera, CSI preferred and USB UVC permitted | Frozen architecture, model/interface open |
| Camera styling | custom retro late-1980s/1990s CCTV/video-surveillance enclosure | Frozen concept |
| Main DC voltage | 24 V | Frozen |
| Heated-bed construction | original footprint; aluminium + silicone heater + magnetic base + flexible PEI sheet | Frozen architecture |
| Bed switching | external DC MOSFET controlled by Manta | Frozen architecture |
| Bed protection | dedicated fuse + independent thermal fuse | Frozen architecture |
| Frame lighting | dimmable 24 V diffused white work light | Frozen architecture |
| Toolhead lighting | EBB36-controlled nozzle work/status light | Frozen architecture |
| Hotend cooling | 24 V fan with tachometer feedback preferred | Frozen architecture |
| Electronics cooling | large low-RPM temperature-controlled enclosure fan(s) | Frozen architecture |
| Wiring | completely new harnesses | Frozen |

## Possible future upgrades / candidates

These items are intentionally **not frozen**. They are documented so they are evaluated at the correct design stage rather than forgotten.

| Candidate | Concept | Status |
|---|---|---|
| Nozzle camera | tiny camera fixed to toolhead/nozzle for nozzle-centred timelapse; likely USB/UVC and therefore requiring a separate moving USB service to the toolhead | Possible future upgrade only |
| Nozzle-camera styling | miniature retro CCTV/video-surveillance enclosure, not an exposed PCB | Frozen aesthetic if upgrade is adopted |
| Filament motion/jam sensor | encoder/pulse sensor verifies that filament actually moves when extrusion is commanded | Strong candidate; exact sensor/mount open |
| Nozzle cleaning station | compact purge/wipe/brush station integrated near the bed without materially increasing the envelope | Strong candidate; tied to final probe/toolhead |
| Retro physical control panel | physical pause/resume/function controls matching the industrial Revival aesthetic | Candidate |
| Hardware emergency stop | latching hardware safety control independent of Linux/Klipper/CAN/macros | High-priority safety candidate |
| Maintenance telemetry | runtime, heater/fan cycles, filament throughput, maintenance dates, error history and resonance trends | Candidate; mainly software |
| Electrical monitoring | 24 V voltage/current/power/energy and thermal warm-up trend logging for diagnostics | Candidate; non-safety telemetry |
| Automated pre-print self-check | orchestration of spool ID/weight, filament motion, homing, Z alignment, nozzle clean, bed scan and fan/temperature checks | Candidate after underlying hardware is validated |

The nozzle camera is deliberately excluded from the base moving-harness design until cable flexibility, bend life, strain relief, toolhead mass, EMI and USB topology can be evaluated on the final head.

See [`generation-3-enhancement-candidates.md`](generation-3-enhancement-candidates.md) for evaluation criteria, safety boundaries and the intended relationship between these candidates.

## Selections intentionally deferred

These items must fit the frozen architecture but their exact model or rating depends on later measurement/CAD/testing:

- exact E3D Roto/Revo SKU/revision and final toolhead CAD after fit/thermal review;
- exact Eddy Duo mounting geometry, offset, thermal compensation/calibration strategy and final CAN harness/connector implementation;
- filament-presence / filament-motion sensing implementation;
- exact MGN rail manufacturer, preload class and lengths;
- exact X/Y T-slot extrusion section, orientation, supplier and length; 2020/2040-class profiles remain the design candidates;
- exact profile-to-historical-base bracket geometry and adjustment method;
- whether final Z rails mount directly to the steel frame, use thin aluminium backing plates or require T-slot profiles, as determined by restored-frame metrology;
- exact Z backing-plate/profile dimensions if required;
- exact shim/adjuster screw size/count and final adjustment range;
- exact Y carriage count if testing shows one long carriage per rail is insufficient;
- exact Tr8 lead (Tr8×2 and Tr8×4 remain candidates);
- exact Z motor, nut and upper-support adjustment geometry;
- exact RFID/NFC reader IC and antenna geometry;
- exact Revival tag technology/schema and degree of OpenPrintTag interoperability;
- exact ESP32-S3-class spool-controller implementation;
- exact load-cell type, rating, ADC and mechanical mounting arrangement;
- exact smart-spool database/service implementation, on-disk decoder format and UI integration;
- exact list of additional vendor decoders after real-tag validation;
- exact bed aluminium thickness;
- exact silicone-heater dimensions and power, after measuring the original heated-bed PCB;
- exact Mean Well 24 V PSU wattage after heater loads are frozen;
- fan makes/models and final duct geometry;
- frame-light strip/diffuser;
- connector families and wire gauges;
- final electronics enclosure and airflow geometry;
- main frame-camera sensor, lens/FOV and final CSI-versus-USB choice;
- optional nozzle-camera hardware/interface if that future upgrade is adopted;
- exact emergency-stop power-cut topology and physical controls;
- exact electrical-monitoring sensor topology;
- exact nozzle-cleaning mechanism and placement.

## Bed size rule

Do not order a 220/235/250 mm standard modern bed merely because it is convenient. The Generation 3 bed is to match the **original heated-bed footprint and travel envelope**. The catalogued approximately 220 × 220 mm Y carriage and 200 × 200 mm original mirror surfaces are reference evidence only; the original heated-bed PCB must be measured before releasing the final aluminium/heater CAD.
