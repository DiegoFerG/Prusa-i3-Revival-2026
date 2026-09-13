# Photo index — Stage 01 Teardown and Inventory

**Capture / inventory date:** 2026-09-13  
**Stage:** 01 · Teardown, cleaning and inventory  
**Status:** COMPLETE  
**Current TD sequence:** `TD-20260913-001` through `TD-20260913-228`

## Archive layers

| Range | Count | Location | Evidence role |
|---|---:|---|---|
| 001–040 | 40 | `originals/` | Pre-teardown baseline and installed subsystem details |
| 041–159 | 119 | `originals/` | Controlled teardown, removed components and final disassembled state |
| 160–228 | 69 | `derived/component-inventory/` | Cleaned, measured and privacy-sanitized component catalogue |
| **Total** | **228** | | Stage 01 documented image sequence |

## Authoritative file-level catalogues

The photo index is intentionally split by acquisition layer rather than duplicating 228 rows in this Markdown file:

- `manifest.csv` — `TD-20260913-001` through `040`;
- `inventory-20260913.csv` — `TD-20260913-041` through `159`, including source filename, SHA-256 and byte count;
- `derived/component-inventory/manifest.csv` — `TD-20260913-160` through `228`, including source-session filename, component ID where assigned, SHA-256, size and privacy processing.

## Major subjects documented

The archive includes:

- original frame and threaded-rod geometry;
- Y, X and Z motion systems;
- bed, heated-bed PCB, levelling hardware and build surfaces;
- Wade/Greg's-Wade-family geared extruder;
- E3D-family hotend, heater block, captive heater cartridge and thermistor;
- five Wantai 42BYGHW811 NEMA17 motors;
- Arduino Mega 2560, StaticBoards RAMPS 1.4SB and A4988-family drivers;
- graphic LCD, RAMPS smart adapter and Panasonic 16 GB SDHC card;
- JCPOWER JC-360-12 PSU;
- mechanical endstop modules;
- T2.5 belt and drive pulley evidence;
- LM8UU-family and FAG 608Z bearings;
- smooth/threaded rod measurements;
- mixed fasteners and the original bed springs;
- removed original wiring harnesses.

## Interpretation rule

A photograph proves only what is visible or measured. Exact model/revision claims remain conservative where markings are unreadable. In particular, the hotend remains E3D-family / probable V5-era, the thermistor type remains electrically unconfirmed, and the plug-in stepper modules are treated as A4988-family unless exact clone/revision evidence is available.

## Transition to Stage 02

This archive is now the primary visual reference for **original mechanical reassembly**. New reassembly photographs should start a new stage/batch rather than extending the teardown sequence indefinitely.
