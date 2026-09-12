# Legacy filament inventory — Batch 01

**Date:** 12 September 2026  
**Source:** recovered stored filament from the original Prusa i3 era  
**Status:** visual/label inspection only; no spool has yet been dried or test-printed in the Revival.

> The exact remaining mass of each spool is still unknown. Labels below document the product specification, not the amount currently left.

| ID | Brand / product | Material | Labelled diameter | Colour | Labelled print temperature | Revival assessment | First action |
|---|---|---|---:|---|---|---|---|
| FIL-001 | FFF World FlexiSMART | Flexible TPU | 3.00 mm | Black | handwritten 220–240 °C; box text also gives a broader generic range | **Usable candidate.** Direct-drive Wade-style extrusion is favourable, but the feed path must be tightly constrained and speeds kept low. TPU is hygroscopic. | Inspect for tackiness/cracking, dry, measure diameter, then slow extrusion test |
| FIL-002 | FFF World FlexiSMART | Flexible TPU | 3.00 mm | Red | label visible in archive; exact temperature to be confirmed from box | **Usable candidate** under the same conditions as FIL-001 | Dry, measure diameter and bench-test |
| FIL-003 | Generic legacy box marked PLA 3.0 mm | PLA | 3.00 mm | White | not yet transcribed | **Conditional candidate.** Old PLA can become very brittle after long storage even when sealed. | Bend/brittleness test, dry gently, measure diameter |
| FIL-004 | T-PLA | PLA-family | 3.00 mm | Violet | not yet transcribed | **Conditional candidate.** Treat as old PLA until exact formulation is confirmed. | Inspect, dry gently, measure diameter |
| FIL-005 | ABS-H | Filled/special ABS | 3.00 mm | Glow in the dark green | not yet transcribed | **Usable candidate with caution.** Glow pigments are typically abrasive; avoid using a soft brass nozzle for a large quantity. | Confirm formulation, use hardened nozzle, dry and test |
| FIL-006 | Smartfil ABS | ABS | 2.85 mm ±0.05 mm | Sunset | 230–250 °C | **Good candidate.** 2.85 mm is the normal practical size for many legacy “3 mm” systems. | Dry, measure several points, test extrusion |
| FIL-007 | FFF World ABS++ | ABS-family | 3.00 mm | Silver | 235–255 °C | **Good candidate.** ABS generally stores better than PLA, but moisture and dimensional drift still need checking. | Dry, dimensional check, test cube |
| FIL-008 | FFF World ABS++ | ABS-family | 3.00 mm | Golden | 235–255 °C | **Good candidate** subject to normal ageing checks | Dry, dimensional check, test cube |
| FIL-009 | FFF World ABS++ | ABS-family | 3.00 mm | Black | 235–255 °C | **Good candidate** subject to normal ageing checks | Dry, dimensional check, test cube |
| FIL-010 | Smartfil ABS | ABS | 2.85 mm ±0.05 mm | Hüller Lake | 230–250 °C | **Good candidate.** Label explicitly identifies 2.85 mm stock. | Dry, dimensional check, test extrusion |

## Can these filaments be used in the Revival?

**Yes, very likely many of them can.** This is one of the main reasons Phase 1 of the Revival will retain a legacy 3 mm / 2.85 mm toolhead.

The important point is that “3 mm” was historically a family name rather than a guarantee that every product measures exactly 3.00 mm. Some recovered spools are explicitly **2.85 mm**, while others are labelled **3.00 mm**. The Revival toolhead must therefore be checked for:

- filament-path internal diameter;
- drive gear/hob geometry;
- heatbreak and PTFE bore, if present;
- nozzle/hotend compatibility;
- extruder calibration for each real measured diameter.

### Material-specific notes

**ABS / ABS++ / Smartfil ABS**
- Highest-priority material for recovery.
- Old ABS often remains printable if it has been kept dry and has not chemically degraded.
- Dry before testing.
- The rebuilt printer should ideally have an enclosure or at least a controlled environment for large ABS parts.

**PLA / T-PLA**
- More uncertain because very old PLA can embrittle through hydrolysis.
- A spool that snaps repeatedly while being uncoiled is not a good candidate for reliable long prints.
- Drying can remove moisture but cannot reverse polymer-chain degradation.

**FlexiSMART TPU**
- Potentially very useful and historically interesting.
- Requires a short, constrained filament path from drive gear to hotend.
- Start very slowly; old Wade-style direct drive is preferable to a long Bowden path.
- Dry thoroughly before testing.

**ABS-H glow-in-the-dark**
- Treat as abrasive until proven otherwise.
- Use a hardened-steel or other wear-resistant nozzle for sustained printing.
- Keep this spool out of initial hotend-validation tests.

## Proposed qualification procedure

1. Photograph sealed/open state and spool label.
2. Inspect for contamination, deformation and obvious brittleness.
3. Measure diameter at multiple locations and orientations with a micrometer/caliper.
4. Dry according to material class using conservative temperatures.
5. Perform a cold bend/unwind test.
6. Extrude 100–200 mm manually at low speed.
7. Print a small temperature tower or simple calibration specimen.
8. Record actual temperature, flow multiplier, measured diameter and any popping/stringing/brittleness.
9. Mark each spool as **PASS**, **LIMITED USE**, **DISPLAY/ARCHIVE** or **REJECT**.

No old filament should be treated as trustworthy solely because its original bag remained sealed.
