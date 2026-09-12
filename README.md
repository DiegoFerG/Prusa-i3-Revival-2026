# Prusa i3 Revival 2026

> Bringing a classic Prusa i3 back to life — one printed part at a time.

**Prusa i3 Revival 2026** documents the complete restoration and modernization of a self-built classic Prusa i3, recovered after more than a decade in storage.

The goal is not to turn it into a modern Prusa clone. We want to preserve the character of the original machine while rebuilding its mechanics, electronics and safety systems with current components and reproducible open documentation.

## Project goals

### Phase 1 — Legacy 3 mm
- Identify and document the original printer and all recovered parts.
- Rebuild the mechanical system.
- Replace the old threaded Z rods with proper leadscrews.
- Reprint structural and functional parts, primarily in ASA.
- Enclose and reorganize the electronics.
- Modernize the controller, drivers, wiring and thermal safety.
- Restore reliable printing with the original 3 mm / 2.85 mm filament system.
- Test and consume the surviving stock of legacy filament.

### Phase 2 — 1.75 mm conversion
Once the legacy filament stock has been consumed, convert the extrusion system to 1.75 mm. The Phase 1 design should make this conversion as modular as possible.

## Starting point

The printer was originally assembled from a classic Prusa i3/Rework-era design with a single-sheet metal frame, threaded-rod Y structure, smooth rods, NEMA 17 motors and a geared Wade-style extruder.

The exact variant and every component will be identified during the archaeology stage rather than assumed.

## Design principles

1. **Document before dismantling.**
2. **Reuse when it makes engineering sense.**
3. **Modernize safety-critical systems.**
4. **Prefer reproducible, readily available components.**
5. **Publish editable source files**, not only STL exports.
6. **Keep the 3 mm stage functional**, but design with the later 1.75 mm conversion in mind.
7. Record decisions, measurements, failures and test results so other classic i3 owners can reuse the work.

## Repository

- `docs/` — archaeology, teardown, design decisions and build documentation
- `hardware/` — mechanical and electrical documentation and BOM
- `printed-parts/` — CAD sources, STEP, STL and slicer projects
- `firmware/` — printer configurations
- `profiles/` — printing/slicer profiles
- `photos/` — photographic record of the restoration

## Status

**Stage 00 — Archaeology / initial inspection**

The printer is still in storage. The first photographs were taken before moving, cleaning or dismantling it. This deliberately preserves the true starting condition of the project.

---

Started in September 2026.
