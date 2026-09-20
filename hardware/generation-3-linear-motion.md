# Generation 3 linear-motion architecture

> Frozen mechanical architecture for the **Revival 2026 final build**. Exact rail lengths, aluminium-extrusion sections, lead-screw lead, mounting-hole coordinates and detailed adjuster geometry remain deferred until the original machine has been rebuilt and measured.

See [`../docs/final-build-architecture.md`](../docs/final-build-architecture.md) for the complete Generation 3 system architecture.

## Design intent

Generation 3 replaces the original smooth-rod/LM8UU guidance with **MGN12-class linear guides on all three axes** while preserving the original Prusa i3 frame, silhouette, bed footprint and machine envelope.

The historical lower structure remains a functional part of the final machine rather than becoming decorative:

- 2× M10×350 mm longitudinal threaded rods;
- 4× M8×200 mm transverse threaded rods;
- the original flat steel vertical frame clamped into that threaded-rod base.

These members are not to be replaced by a modern aluminium-extrusion chassis. Commercial aluminium T-slot profiles may be added as local precision/structural carriers for the X and Y rail systems, but the original M8/M10 base and steel frame remain the printer skeleton.

The purpose is not to make the original frame behave like a precision-machined CNC chassis by force. Instead, the new guide system is deliberately designed around **mechanical adjustability** so modern alignment can be achieved on the restored historical structure.

All critical linear-guide mounting systems must therefore be:

- mechanically alignable;
- independently lockable after adjustment;
- capable of correcting alignment without bending or forcing the rail;
- measurable with conventional workshop metrology;
- serviceable without destroying the original frame.

## Frozen axis architecture

| Axis | Guidance | Drive | Frozen support concept |
|---|---|---|---|
| X | 1× MGN12-class rail, long carriage preferred | GT2 belt | MGN12 mounted to a rigid commercial aluminium T-slot extrusion used as the X beam; exact 2020/2040-class section deferred |
| Y | 2× MGN12-class rails, one carriage per rail initially | GT2 belt | one longitudinal T-slot extrusion carrier per rail, mounted to the historical M8/M10 base through adjustable supports; exact 2020/2040-class section deferred |
| Z | 2× MGN12-class rails, one per side | 2× independent Tr8 lead screws | direct mounting to the steel frame is preferred if metrology permits; thin aluminium backing plates are the second choice; T-slot profiles are used only if required |

**MGN12H-class long carriages** are the current preferred starting point. Exact manufacturer, preload class, rail lengths and aluminium-profile sections remain open until the restored printer is dimensionally surveyed.

## Mandatory alignment principle

No Generation 3 linear rail may be forced to conform to a poor reference surface.

The metallic reference structure depends on the axis:

- X and Y use commercial aluminium T-slot extrusion as the rail-support structure;
- Z may use the original steel frame directly when its measured geometry is suitable;
- Z may add a thin aluminium backing/reference plate when the steel frame needs a better local reference or adjustment surface;
- a Z T-slot extrusion is a fallback only when metrology or packaging demonstrates that direct/plate mounting is insufficient.

Controlled adjustment may use fine-pitch jacking screws, slotted/clearance holes, metallic shims or a combination appropriate to the axis. Adjustment features establish geometry; **independent clamping fasteners carry the structural load after alignment**.

The exact adjustment mechanism is not frozen until the restored frame has been measured.

## Aluminium-profile principle

Commercial T-slot extrusion is a practical structural/reference carrier, not an assumption of metrological perfection.

Before rail installation, each selected profile must be checked for:

- straightness over the working length;
- twist;
- usable mounting-face flatness;
- adequate stiffness at the selected span;
- mass, especially for the moving Z/X gantry;
- slot geometry and fastener access.

The MGN12 rail must not be intentionally bent to follow profile error. If a selected extrusion does not provide a sufficiently good reference by itself, controlled shimming or an intermediate metallic reference strip/plate may be used.

Exact profile family and supplier remain deferred. **2020 and 2040-class sections are the current design candidates; 3030 is not a requirement.**

## X axis

### Architecture

- one MGN12-class rail;
- one long carriage, currently MGN12H-class preferred;
- GT2 belt drive;
- direct-drive toolhead attached to the carriage;
- one rigid commercial aluminium T-slot extrusion forming the X beam and MGN12 support.

The X rail replaces the original pair of Ø8 mm smooth rods and their LM8UU bearings. The aluminium extrusion takes over the structural beam function previously provided by the rod pair; the MGN12 provides guidance and must not be treated as the primary beam.

A **2040-class profile with the 40 mm dimension oriented for useful vertical bending stiffness is a leading candidate**, while 2020 remains a candidate if stiffness, mass and packaging measurements support it. The exact section is intentionally not frozen yet.

### X-rail adjustment

The X rail/profile assembly must provide:

- a straight metallic reference for the MGN12;
- controlled lateral/vertical correction where required;
- independent rail fixing;
- no intentional rail bending to compensate for a poor profile or support;
- mechanical squaring of the complete X beam to the Z system before software compensation is used.

Klipper `Z_TILT_ADJUST` is for small repeatable corrections, not for hiding a poorly aligned X beam.

## Y axis

### Architecture

Generation 3 uses two MGN12-class rails under the original-footprint moving bed. Each rail is supported by its own longitudinal commercial aluminium T-slot extrusion.

```text
                 original-footprint bed
          +-----------------------------+
          |                             |
          +-----------------------------+
                  |             |
              carriage      carriage
                  |             |
             ==== rail ==== ==== rail ====
                  |             |
             T-slot profile T-slot profile
                 Y-L            Y-R
                  |             |
          adjustable mounts to historical
             M8/M10 threaded-rod base
```

The historical M8/M10 base remains the structural skeleton. The T-slot profiles are local rail carriers and do not replace the base with a new extrusion chassis.

The initial design target is **one long carriage per rail**. Additional carriages are not frozen and should only be added if load/moment testing demonstrates a real need.

A **2020-class profile is the leading Y candidate** because of its lower height and mass, but 2040 remains available if stiffness, mounting or adjustment tests justify it. Exact section and orientation are deferred to CAD/metrology.

### Master/slave philosophy

One Y rail/profile assembly is designated the **master datum**. The second is the **slave** and is aligned to the master.

The master establishes the Y travel direction. The slave must not be used to force the bed/carriage assembly into a second conflicting datum.

### Required Y adjustment

The Y mounting system must provide controlled adjustment for:

- lateral parallelism between the two rails;
- vertical coplanarity between the two rails;
- longitudinal pitch where necessary;
- local support-height correction without bending either rail.

The adjustable interfaces are between the historical M8/M10 base and the extrusion carriers and/or between the extrusion and rail, as determined by final CAD.

Three height-setting points are preferred where practical because they define a plane without creating unnecessary over-constraint.

The final design should allow the slave assembly to be adjusted while the bed is moved through the complete Y travel so drag/preload can be checked continuously.

## Z axis

### Architecture

Generation 3 uses:

- one MGN12-class rail on the left side;
- one MGN12-class rail on the right side;
- two independent Tr8 lead screws;
- one independently driven Z motor per lead screw;
- one TMC2209 channel per Z motor;
- probe-assisted Klipper Z-tilt correction after mechanical alignment.

```text
                 X gantry
       +---------------------------+
       |                           |
       +---------------------------+
          |                     |
       carriage              carriage
          |                     |
      === Z rail ===        === Z rail ===
          |                     |
         Tr8                   Tr8
          |                     |
       motor Z0              motor Z1
```

### Geometric responsibility

This is a strict design rule:

**The Z linear rails define the Z motion geometry. The Tr8 lead screws only provide vertical drive.**

The lead screws must never be used to force the Z carriages into alignment.

### Frozen Z mounting hierarchy

The final Z mounting method is selected after metrology of the restored steel frame, in this order:

1. **Direct MGN12-to-steel-frame mounting** when the frame is sufficiently straight/flat locally and the mounting can provide the required alignment and independent locking.
2. **Thin aluminium backing/reference plate** between frame and rail when the frame needs a better local reference surface, controlled shimming or more convenient adjustment/fixing geometry.
3. **Commercial T-slot extrusion between frame and rail** only when measurements or packaging show that the first two solutions cannot provide the required geometry, stiffness or adjustment.

This hierarchy is frozen. The final outcome remains measurement-dependent.

The design must minimise unnecessary forward offset of the Z carriages/X gantry because any intermediate structure changes X-beam position, Tr8 alignment, nozzle-to-bed geometry and moving mass.

### Z alignment

The Z system must allow correction of:

- left/right rail parallelism;
- rail verticality;
- front/back coplanarity;
- squareness relative to X and Y;
- small dimensional errors in the original steel frame.

One Z side acts as the primary geometric reference and the second is adjusted relative to it.

Direct mounting may use suitable clearance/slotted holes and metallic shims. Backing plates or profiles may add fine-adjustment screws where useful. In every case, alignment must be locked by structural fasteners without deforming the rail.

## Z lead-screw alignment

Lead-screw alignment is performed **after the Z linear guides are aligned and locked**.

The motor mount, nut mount and any upper support must provide enough controlled lateral compliance/adjustment to align each Tr8 screw to the already-established rail geometry.

Design targets:

- motor position adjustable in X/Y before final locking;
- lead-screw nut mount tolerant of tiny radial mismatch rather than transmitting side load into the carriage;
- upper bearing/support, if used, must not over-constrain the screw;
- no lead-screw component may be used as a structural guide.

The final Tr8 lead remains open. Tr8×2 and Tr8×4 are candidates; selection will be based on restored geometry, desired Z speed, mechanical advantage and motor behaviour.

## Rail-support construction

The rail-supporting reference surfaces must be metallic and dimensionally stable in the final machine.

Frozen material/role rules:

- X/Y commercial aluminium extrusion provides the main rail-support structure;
- the original steel frame may itself be the Z rail reference where metrology validates it;
- aluminium backing plates are permitted for Z reference/alignment;
- ASA printed parts are appropriate for adjustable brackets where loads and creep are acceptable, prototypes, covers, adjuster retainers, scales, cable features and non-reference geometry;
- printed polymer is not to be the sole precision reference surface sandwiched between a final MGN rail and its structural metallic reference unless testing specifically validates that design.

The final choice of metal fasteners, inserts, brackets and any printed support geometry must preserve serviceability and independent locking.

## Alignment and commissioning workflow

The final procedure will be refined after CAD is complete, but the intended order is frozen:

1. rebuild and measure the original frame and M8/M10 base;
2. inspect candidate X/Y extrusion straightness and mounting faces;
3. establish the Y master profile/rail assembly;
4. align the Y slave profile/rail assembly for parallelism and coplanarity;
5. lock Y and verify full-travel drag;
6. measure the Z frame mounting zones and choose direct, backing-plate or profile mounting according to the frozen hierarchy;
7. establish the primary Z rail;
8. align the secondary Z rail;
9. lock Z and verify free full-travel movement;
10. install/square the X extrusion beam;
11. align the X rail to its extrusion/reference surface;
12. align each Tr8 lead screw to the already-established Z guide geometry;
13. verify full manual travel before powered motion;
14. record shims/adjuster positions and final fastener torque;
15. commission motors at low speed;
16. use probe-assisted Klipper Z tilt only after mechanical squareness is acceptable;
17. run the permanent X and Y accelerometers and record the resonance baseline.

Recommended setup tools include a dial indicator, precision square, straightedge/reference surface, feeler gauges and documented measurement fixtures.

## Frozen decisions

- preserve the original flat steel frame as a functional structural member;
- preserve the original lower threaded-rod structure: 2× M10×350 mm longitudinal rods and 4× M8×200 mm transverse rods;
- do not replace the historical base with a modern aluminium-extrusion chassis;
- MGN12-class guidance on X, Y and Z;
- one X rail;
- two Y rails;
- two Z rails;
- long MGN12H-class carriage format preferred as the starting point;
- GT2 belt drive retained on X and Y;
- dual independent Tr8 Z drive;
- Z linear rails define motion; Z lead screws provide drive only;
- X uses a commercial aluminium T-slot extrusion as its structural rail carrier;
- Y uses two longitudinal commercial aluminium T-slot extrusion rail carriers mounted to the historical base;
- exact X/Y profile section remains deferred, with 2020/2040-class profiles as the design family to evaluate;
- Y uses a master/slave datum strategy;
- Z uses a primary/secondary datum strategy;
- Z mounting follows the frozen hierarchy: direct to steel frame if metrology permits, otherwise thin aluminium backing plate, with T-slot extrusion only if necessary;
- rail-support geometry is not intentionally forced or bent to compensate for the old frame or extrusion error;
- final rail reference structures are metallic;
- software correction is secondary to mechanical alignment.

## Intentionally deferred

- exact rail manufacturer;
- exact preload class;
- exact rail lengths;
- exact X and Y aluminium extrusion section, orientation, supplier and length;
- exact profile-to-historical-frame bracket geometry;
- exact carriage count if testing shows one-per-Y-rail is insufficient;
- whether the final Z implementation uses direct frame mounting, aluminium backing plates or T-slot profiles, as determined by restored-frame metrology;
- exact Z backing-plate/profile dimensions if required;
- exact shim/adjuster screw size and count per axis;
- exact Tr8 lead;
- exact motor/nut/upper-support adjustment geometry;
- final tolerances and acceptance criteria after restored-frame metrology.
