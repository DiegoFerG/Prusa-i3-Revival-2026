# Generation 3 linear-motion architecture

> Frozen mechanical architecture for the **Revival 2026 final build**. Exact rail lengths, lead-screw lead, mounting-hole coordinates and adjuster dimensions remain deferred until the original machine has been rebuilt and measured.

See [`../docs/final-build-architecture.md`](../docs/final-build-architecture.md) for the complete Generation 3 system architecture.

## Design intent

Generation 3 replaces the original smooth-rod/LM8UU guidance with **MGN12-class linear guides on all three axes** while preserving the original Prusa i3 frame, silhouette, bed footprint and machine envelope.

The purpose is not to make the original frame behave like a precision-machined CNC chassis by force. Instead, the new guide system is deliberately designed around **mechanical adjustability** so modern alignment can be achieved on the restored historical structure.

All critical linear-guide mounts must therefore be:

- mechanically adjustable;
- independently lockable after adjustment;
- capable of correcting alignment without bending or forcing the rail;
- measurable with conventional workshop metrology;
- serviceable without destroying the original frame.

## Frozen axis architecture

| Axis | Guidance | Drive | Frozen concept |
|---|---|---|---|
| X | 1× MGN12-class rail, long carriage preferred | GT2 belt | one rigid adjustable rail carrier |
| Y | 2× MGN12-class rails, one carriage per rail initially | GT2 belt | master/slave rail pair with parallelism and coplanarity adjustment |
| Z | 2× MGN12-class rails, one per side | 2× independent Tr8 lead screws | rails define geometry; lead screws provide vertical drive only |

**MGN12H-class long carriages** are the current preferred starting point. Exact manufacturer, preload class and rail lengths remain open until the restored printer is dimensionally surveyed.

## Mandatory alignment principle

No critical Generation 3 linear rail is to be treated as a simple fixed-hole bolt-on part.

Each rail system must use an **adjustable mounting structure** consisting of a rigid rail carrier/reference plate plus fine adjustment and separate clamping hardware.

The adjustment screws are setup tools, not primary structural fasteners.

Typical arrangement:

```text
                 linear rail
============================================
     o        o        o        o
        rail fixing screws
--------------------------------------------
          rigid aluminium carrier
       <--- fine adjustment screws --->
--------------------------------------------
             original structure
```

After alignment:

1. the rail/carrier is brought into position with fine adjusters;
2. alignment is verified;
3. independent fixing screws are tightened to the documented torque;
4. adjusters remain lightly seated or are lock-nutted as appropriate;
5. the structural load is carried by the fixing system, not by the adjuster tips.

## Adjustment-screw concept

Fine positioning should use ordinary fine-pitch screws rather than expensive micrometer heads unless testing proves otherwise.

A useful reference is an M3×0.5 or M4×0.5 adjuster:

| Rotation | Linear movement at 0.5 mm pitch |
|---:|---:|
| 1 turn | 0.500 mm |
| 1/2 turn | 0.250 mm |
| 1/4 turn | 0.125 mm |
| 1/8 turn | 0.0625 mm |
| 1/16 turn | 0.03125 mm |

Where useful, printed or engraved index marks may be added so setup changes can be recorded reproducibly.

## X axis

### Architecture

- one MGN12-class rail;
- one long carriage, currently MGN12H-class preferred;
- GT2 belt drive;
- direct-drive toolhead attached to the carriage;
- rigid X beam/carrier designed specifically to provide a suitable rail mounting reference.

The X rail replaces the original pair of smooth rods and their LM8UU bearings.

### X-rail adjustment

The X rail must be mounted to a rigid carrier with:

- lateral fine-adjustment screws distributed along the rail/reference edge;
- slotted or clearance mounting where required for controlled movement;
- independent rail fixing screws;
- no intentional rail bending to compensate for a poor support surface.

The complete X beam must also allow mechanical squaring to the Z system before software compensation is used.

Klipper `Z_TILT_ADJUST` is for small repeatable corrections, not for hiding a poorly aligned X beam.

## Y axis

### Architecture

Generation 3 uses two MGN12-class rails under the original-footprint moving bed.

```text
                 original-footprint bed
          +-----------------------------+
          |                             |
          +-----------------------------+
                  |             |
              carriage      carriage
                  |             |
             ==== rail ==== ==== rail ====
                 Y-L            Y-R
```

The initial design target is **one long carriage per rail**. Additional carriages are not frozen and should only be added if load/moment testing demonstrates a real need.

### Master/slave philosophy

One Y rail is designated the **master datum rail**. The second rail is the **slave rail** and is aligned to the master.

The master establishes the Y travel direction. The slave must not be used to force the bed/carriage assembly into a second conflicting datum.

### Required Y adjustment

The Y mounting system must provide controlled adjustment for:

- lateral parallelism between the two rails;
- vertical coplanarity between the two rails;
- longitudinal pitch where necessary;
- local support-height correction without bending either rail.

A preferred concept is a rigid aluminium rail carrier supported by a small number of defined adjustment points. Three height-setting points are preferred where practical because they define a plane without creating unnecessary over-constraint.

The final design should allow the slave rail to be adjusted while the bed is moved through the complete Y travel so drag/preload can be checked continuously.

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

### Z-rail adjustment

Each Z rail is mounted on a rigid backing/carrier plate attached to the original frame.

The system must allow correction of:

- left/right rail parallelism;
- rail verticality;
- front/back coplanarity;
- squareness relative to X and Y;
- small dimensional errors in the original steel frame.

One Z side acts as the primary geometric reference and the second is adjusted relative to it.

Fine-adjustment/jacking screws should act on the carrier plates, not deform the rail itself.

## Z lead-screw alignment

Lead-screw alignment is performed **after the Z linear guides are aligned and locked**.

The motor mount, nut mount and any upper support must provide enough controlled lateral compliance/adjustment to align each Tr8 screw to the already-established rail geometry.

Design targets:

- motor position adjustable in X/Y before final locking;
- lead-screw nut mount tolerant of tiny radial mismatch rather than transmitting side load into the carriage;
- upper bearing/support, if used, must not over-constrain the screw;
- no lead-screw component may be used as a structural guide.

The final Tr8 lead remains open. Tr8×2 and Tr8×4 are candidates; selection will be based on restored geometry, desired Z speed, mechanical advantage and motor behaviour.

## Rail-carrier construction

The rail-supporting reference surfaces should be metallic and dimensionally stable in the final machine.

Preferred approach:

- aluminium carrier/backing plates for the actual rail reference and clamping structure;
- ASA printed parts for prototypes, covers, adjuster retainers, scales, cable features and non-reference geometry;
- printed polymer is not to be the sole precision reference surface sandwiched between a final MGN rail and the historical frame unless testing specifically validates that design.

## Alignment and commissioning workflow

The final procedure will be refined after CAD is complete, but the intended order is frozen:

1. rebuild and measure the original frame;
2. establish the Y master rail;
3. align the Y slave rail for parallelism and coplanarity;
4. lock Y and verify full-travel drag;
5. establish the primary Z rail;
6. align the secondary Z rail;
7. lock Z and verify free full-travel movement;
8. install/square the X beam;
9. align the X rail to its carrier;
10. align each Tr8 lead screw to the already-established Z guide geometry;
11. verify full manual travel before powered motion;
12. record adjuster positions and final fastener torque;
13. commission motors at low speed;
14. use probe-assisted Klipper Z tilt only after mechanical squareness is acceptable;
15. run the permanent X and Y accelerometers and record the resonance baseline.

Recommended setup tools include a dial indicator, precision square, straightedge/reference surface, feeler gauges and documented measurement fixtures.

## Frozen decisions

- MGN12-class guidance on X, Y and Z;
- one X rail;
- two Y rails;
- two Z rails;
- long MGN12H-class carriage format preferred as the starting point;
- GT2 belt drive retained on X and Y;
- dual independent Tr8 Z drive;
- Z linear rails define motion; Z lead screws provide drive only;
- all critical rail systems use fine mechanical adjustment plus independent locking;
- Y uses a master/slave datum strategy;
- Z uses a primary/secondary datum strategy;
- rail-support geometry is not intentionally forced or bent to compensate for the old frame;
- final rail reference structures should be metallic;
- software correction is secondary to mechanical alignment.

## Intentionally deferred

- exact rail manufacturer;
- exact preload class;
- exact rail lengths;
- exact carriage count if testing shows one-per-Y-rail is insufficient;
- exact carrier-plate dimensions/material grade;
- exact adjuster screw size and count per axis;
- exact Tr8 lead;
- exact motor/nut/upper-support adjustment geometry;
- final tolerances and acceptance criteria after restored-frame metrology.