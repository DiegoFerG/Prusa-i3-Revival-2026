# Prusa i3 Revival 2026

> Bringing a classic Prusa i3 back to life — one printed part at a time.

**Prusa i3 Revival 2026** documents the complete restoration and modernization of a self-built classic Prusa i3, recovered after more than a decade in storage.

The goal is not to turn it into a modern Prusa clone. We want to preserve the character of the original machine while rebuilding its mechanics, electronics and safety systems with current components and reproducible open documentation.

## Project roadmap

The project deliberately progresses through three generations of the same printer rather than replacing everything at once:

1. **Original Hardware Revival** — recover a reliable printing baseline with the installed Mega/RAMPS-era hardware and legacy 3 mm / 2.85 mm extrusion system.
2. **Re-ARM Upgrade** — move to the recovered Panucatt Re-ARM while preserving the RAMPS/RepRap-era machine for a documented 32-bit transitional stage.
3. **Revival 2026 Final Build** — convert to 1.75 mm, proper Z leadscrews and current autonomous networked electronics while preserving the classic Prusa i3 appearance and kinematics.

The complete stage-by-stage plan, validation gates and deliverables are maintained in **[docs/ROADMAP.md](docs/ROADMAP.md)**.

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
  - [`docs/ROADMAP.md`](docs/ROADMAP.md) — complete staged restoration and modernization roadmap
  - `docs/00-arqueologia/` — printer and loose-parts archaeology
  - `docs/01-filaments/` — recovered legacy filament inventory and qualification
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
