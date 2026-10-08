# Generation 3 — PSU enclosure and 24 V power distribution

Status: **agreed topology / engineering specification; not manufactured, purchased or electrically validated**. Updated: 2026-10-08.

This document is the canonical design baseline for the separate Generation 3 power-supply enclosure, panel outlets and CAN power harness. It supplements [final architecture](../docs/final-build-architecture.md), [Bed Node](generation-3-bed-node.md) and [custom CAN node rules](generation-3-custom-can-node-design-rules.md).

## Architecture and enclosure boundaries

- A **separate PSU enclosure** receives 230 V AC through a suitably rated, protective-earth-capable IEC appliance inlet and a **two-pole master switch**; the chosen inlet/switch/fusing topology must be assessed as a complete approved mains assembly.
- Its internal 24 V PSU supplies a covered DC distribution block with **individually protected output branches**. The main control-electronics enclosure is not the source of heater power. No high-current bed supply shall travel through Manta PCB traces, USB wiring, CEB or CAN breakout.
- The preferred final PSU already listed in the repository is **Mean Well LRS-600-24, 24 V / 25 A / 600 W**, **subject to a measured simultaneous-load budget**, derating and thermal validation. Existing prototype PSU use is not final approval. The 150–200 W bed heater target in the frozen final architecture is unchanged; 250/300 W are only design scenarios, not an adopted heater.
- The printed enclosure must be assessed for mains electrical protection, access barriers, strain relief, ventilation, mounting, and a suitably rated flame-retardant material. Ordinary printed ABS/ASA does not automatically qualify as a mains enclosure. Prefer a certified mains compartment/enclosure solution, or a properly qualified insulated/metal sub-enclosure. Protective earth (PE) bonds the PSU chassis and accessible conductive parts as required; it is **not** a substitute for DC return.
- Provide serviceable branch fuses / DC-rated protection, suitably rated terminal blocks, covers, polarity labelling, connector shrouds and an accessible way to isolate all power. Size both positive and return conductors. Never expose live male contacts on the energized PSU panel.
- Any emergency stop / independent heater thermal cutoff remains outside Klipper, Linux and CAN authority. Provide independent bed thermal fuse mounted to the heater assembly and appropriate branch overcurrent protection. Functional heater control remains with a suitably rated **external DC MOSFET stage** under Bed Node control (or Manta control during initial commissioning).

## DC panel connectors and branch allocations

**Connector family selected:** genuine **AMASS XT60E panel-mount XT60-compatible** connectors, mechanically fastened to the PSU enclosure. Exact suffix, gender, orientation, mechanical cutout and mating cable-side item must be chosen from a manufacturer drawing before CAD release. **XT90 is not required in the present baseline**, but may be reconsidered for a future higher-current overall feed.

Select a **recessed/finger-safe female-socket power-supply panel interface** and a compatible male cable plug where appropriate, verified against AMASS drawings and real samples; no accessible energized pins. Each output must be clearly engraved/silkscreen-labelled and keyed/polarised. **Each branch has an independent fuse** and separately routed +24 V and 0 V. Proposed seven-way panel (outlet identities frozen; ratings provisional):

| Port | Destination / purpose | Connector | Design status |
| --- | --- | --- | --- |
| PWR-01 | Manta M8P V2 main logic/controller input / host (VIN or board-designated 24 V input after schematic verification) | XT60E panel | Dedicated protected branch |
| PWR-02 | Manta motor-driver supply domain (VBB/HV selection and board isolation **must be verified**; no assumption of electrically independent rails) | XT60E panel | Dedicated protected branch; actual Manta pins/jumpers TBD |
| PWR-03 | Rear bed-area **heater-power stage**, not CAN/Bed Node logic input | XT60E panel | Dedicated high-current heater branch |
| PWR-04 | Toolhead electronics/heater/extruder supply, delivered to EBB36 via the final **XT30(2+2)** CAN/power harness and an appropriately protected distribution point | XT60E panel | Only **one intentional power feed** to EBB; prohibit accidental parallel feeds |
| PWR-05 | CAN distribution PCB / CEB / low-power Bed Node/RASS logic supply | XT60E panel | Separate logic/CAN supply |
| PWR-06 | Auxiliary 24 V loads such as dedicated USB hub DC/DC, lighting or later spool accessories | XT60E panel | Auxiliary branch; its loads/budget TBD |
| PWR-07 | Labelled capped **SPARE**, normally unpopulated or electrically isolated until commissioned | XT60E panel provision | Reserve, no live exposed contact |

The branch plan must be consolidated during schematic design: a low-current CAN distribution PCB may receive 24 V from PWR-05 while the toolhead's higher-current 24 V originates from PWR-04. **Do not simply join two separately fused 24 V branches on the same unisolated CAN power conductor**. Select one feed per powered segment, or use designed separation of CAN-H/L from the high-current supply path, validated return and fault strategy. Passive CEB ports are **not** independent power outputs or CAN repeaters.

### Wiring topology (functional, not a pin-number drawing)

```text
IEC 230 Vac (L/N/PE) -> rated 2-pole switch + mains protection
                         -> 24 V PSU -> covered +24 V / 0 V DC distributor
                                       |-- F01 -> XT60 PWR-01 -> Manta logic
                                       |-- F02 -> XT60 PWR-02 -> Manta drivers*
                                       |-- F03 -> XT60 PWR-03 -> bed DC heater stage
                                       |-- F04 -> XT60 PWR-04 -> EBB feed design*
                                       |-- F05 -> XT60 PWR-05 -> CAN low-power domain*
                                       |-- F06 -> XT60 PWR-06 -> auxiliary loads
                                       '-- F07 -> XT60 PWR-07 -> isolated spare

Manta CAN -> CEB/passive linear CAN bus -> EBB36 and Bed Node/RASS
Bed Node logic: XT30(2+2) CAN + separately fused low-power 24 V segment*
Bed heater: independent PWR-03 high-current +24 V/0 V -> external
            MOSFET switching stage -> short flexible moving-bed heater cable;
            independent thermal fuse physically on bed
```

*Final separation of motor voltage domains, CAN power branches, physical power injection and grounding is **pending schematic verification**. Do not wire from this functional diagram alone.

## CAN connectors and cable manufacturing

- Connector type: **XT30(2+2), four contacts**: two large contacts for +24 V/0 V and two small contacts for differential CAN-H/CAN-L. **Ordinary 2-pole XT30 is not interchangeable.**
- Candidate **vertical male THT PCB**: **AMASS XT30(2+2)PB-M**, distributor listing **LCSC C19268029**. Candidate mating **female inline cable plug**: **AMASS XT30(2+2)-F**. Catalog designations, physical fit, electrical ratings, actual EBB36/CEB mating gender and precise manufacturer pin numbers are **to be verified from authoritative drawings and samples** before PCB footprint or harness release.
- At the PSU side, use panel XT60E; at CAN breakout / custom node PCB edges, use vertical XT30(2+2) where manufacturer-certified mating pairs fit the geometry.
- Keep **two independent cable assemblies** from main electronics area towards bed rear: (1) **four-core CAN+logic** (+24 V, 0 V, twisted CAN-H/L), with XT30(2+2) mating connectors; (2) **two-core 24 V heater power** from PWR-03 through a current-rated connector to external switching stage. Bed Node is fixed at rear chassis cross-member; only the short cable to the moving Y bed needs continuous-flex rating.
- EBB36 toolhead: four conductor combined CAN/power harness using XT30(2+2), continuously flex-rated in X-chain. The REVO heater, ROTO driver and all attached loads are included in the power budget.
- **Cable candidates only:** LAPP UNITRONIC BUS CAN FD P 2x2x0.5 mm² (manufacturer part 2170279), or chainflex-grade equivalent; 0.5 mm² for low-current Bed Node logic/CAN may be adequate after load/length checks. For moving EBB seek 2x0.75–1.0 mm² power + twisted 2x0.25–0.34 mm² CAN as an alternative if connector terminals and cable dynamic rating permit. Neither is automatically approved.
- Bed heater branch: consider **2x1.5–2.5 mm² flexible wire**, final selection based on actual 150–200 W heater, round-trip length, ambient temperature, routing, voltage drop, motion, fuse trip and connector rating. 0.5/0.75 mm² CAN cable **must not** be used to supply the bed heating element.
- Shielding/drain termination, reference ground strategy, conductor colours, crimp/solder specifications, heatshrink, strain relief, pin-to-pin continuity tests and service loops will be recorded in a separate **versioned harness drawing**. The simplified pairing CAN-H/L + PSU+/- is **not** a verified connector pin assignment.
- The CEB is a passive junction, not an active multiport hub. Maintain a CAN trunk with short stubs and **exactly two 120-ohm terminations at physical endpoints**. Custom Bed Node/RASS each provide two CAN passthrough connectors and switchable 120-ohm termination per [node rules](generation-3-custom-can-node-design-rules.md).

## Release gates / outstanding engineering

1. Confirm PSU nameplate, mechanical fit, fan/derating and complete worst-case load budget including bed, X/Y/Z, EBB, CB2, CAN nodes, fans and peripherals.
2. Confirm Manta V2.0 schematic input names, 24 V VBB/HV relationships, fusing, wiring, jumpers and whether separate PWR-01/PWR-02 circuits truly remain separate.
3. Confirm original AMASS manufacturer drawings, XT60E safe panel gender and XT30(2+2) board/cable mated geometry, pin numbering, thermal/current ratings and panel footprints.
4. Specify DC fuse sizes/type/power breaking ratings according to selected wiring, heater, PSU short circuit capability and connector ratings (no invented amperage).
5. Define documented single-source power injection for EBB, CEB and each custom CAN node; prevent backfeed between PWR-04/PWR-05.
6. Finalize wire gauge/length, harness routing, shield bonds, protective earth, movement, mechanical restraint and bed safety cutoff behavior.
7. Have the mains assembly designed/inspected by a competent person before energization; bench validate each DC branch disconnected from sensitive electronics, then test short circuit/fault protection and heat rise under controlled conditions.

## Procurement status

All XT60E/XT30(2+2) part references and cables above are **selection candidates, not recorded purchases**. The dedicated PSU enclosure, fused panel distributor, custom CAN breakout, Bed Node, heater stage and made-to-measure harnesses are **planned only**.
