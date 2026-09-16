# Generation 3 smart spool system

This document defines the target **Revival Smart Spool System** for the Generation 3 build.

The objective is to reproduce the useful part of the automatic-spool experience of modern systems while keeping the Revival independent, open and vendor-neutral:

- identify a loaded spool automatically;
- recognise Revival-native tags;
- recognise supported Bambu Lab RFID-tagged spools;
- map detected material data to a **Revival-calibrated** filament profile;
- measure the installed spool mass and estimate remaining filament automatically;
- keep per-spool inventory/history;
- expose the result in the local HDMI5/KlipperScreen UI and to the host software.

The system is intentionally independent from the printer motion-control MCU. Failure of the spool-identification subsystem must not prevent safe manual operation of the printer.

## Architectural principles

1. **Revival format is native.** Our own tag/data format is the source of truth for non-Bambu spools.
2. **Bambu compatibility is read/import compatibility, not emulation.** The Revival should read supported original Bambu spool tags and translate their information into the Revival data model. It must not attempt to counterfeit Bambu tags.
3. **Material identity is separate from machine tuning.** A detected Bambu material may provide brand, family, colour, diameter and material limits/recommendations, but machine-specific parameters come from a profile calibrated for the Revival.
4. **A physical spool is tracked as an individual object.** Two nominally identical rolls remain two separate inventory records.
5. **Remaining filament is determined primarily from mass.** The system uses a load cell under the spool holder and subtracts the known empty-spool mass.
6. **Measurements during printing are treated as dynamic.** Final inventory correction is based on stable readings, not on a single instantaneous value affected by filament tension or spool acceleration.

## Functional architecture

```text
                         LOADED SPOOL
                              |
             +----------------+----------------+
             |                                 |
      Revival NFC/RFID tag              Bambu RFID tag
             |                                 |
             +----------------+----------------+
                              |
                     NFC/RFID reader
                              |
                      local controller
                    (ESP32-S3 class)
                              |
                              +-------------------+
                              |                   |
                        spool identity        load-cell ADC
                              |                 (HX711 class)
                              |                   |
                              +---------+---------+
                                        |
                               Revival spool service
                                        |
                  +---------------------+----------------------+
                  |                     |                      |
             filament DB           Klipper/Moonraker      HDMI5 UI
                  |                                            |
          Revival profile map                        material / colour /
                  |                                  remaining mass / alerts
                  v
          calibrated print profile
```

The exact reader IC, antenna geometry and local-controller board are intentionally left open until the spool-holder geometry is designed. **PN5180-class reader + ESP32-S3 + HX711-class load-cell ADC** is the current preferred implementation direction.

## Revival-native spool tags

The project will define a versioned format, provisionally named **Revival Spool Tag v1**.

The physical tag should be writable, inexpensive and replaceable. The tag should carry only stable identification and basic material data; frequently changing inventory data belongs in the host database.

Recommended tag fields:

- format/version identifier;
- unique spool UUID;
- manufacturer;
- product/family name;
- material family (PLA, PETG, ASA, TPU, etc.);
- material modifier/variant (Tough, Matte, CF, Silk, HF, 95A, etc.);
- colour name;
- colour RGB/RGBA value;
- nominal diameter;
- nominal net filament mass;
- empty-spool/tare mass where known;
- optional lot/batch identifier;
- optional production/purchase date;
- profile key used to locate the corresponding Revival material profile.

The tag should **not** be the only storage location for:

- current remaining mass;
- print history;
- calibration history;
- pressure advance;
- flow ratio;
- volumetric-flow limit;
- retraction;
- cooling tuning;
- other machine-specific tuning.

Those values belong in the Revival filament database/profile store so they can be updated without rewriting every physical tag.

## Bambu Lab compatibility layer

When a supported original Bambu RFID spool is detected, the reader service should attempt to extract the data available from that tag and translate it into the Revival data model.

Target information includes, where available:

- Bambu material/product identity;
- material family/variant;
- colour;
- nominal diameter;
- nominal mass/length;
- material temperature limits or recommendations;
- drying information;
- production/lot/spool identifiers.

The result is then mapped to a **Revival material profile**.

Example:

```text
Bambu RFID detected
        |
        +-- material: PLA Matte
        +-- colour: Charcoal
        +-- diameter: 1.75 mm
        +-- supplier limits/recommendations
        |
        v
Revival profile mapping
        |
        +-- REVIVAL_BAMBU_PLA_MATTE_V2
        +-- Revival flow calibration
        +-- Revival pressure advance
        +-- Revival retraction
        +-- Revival max volumetric flow
        +-- Revival cooling strategy
```

A previously unseen Bambu material must not silently inherit aggressive machine parameters. The UI should identify it as a new material and offer a compatible generic/base Revival profile until calibration is completed.

Supplier-provided temperature information may seed or constrain a profile, but the final print settings remain Revival-specific.

## Spool weighing and remaining-filament estimation

### Mechanical principle

The complete spool-support load must pass through a load cell or load-cell arrangement. The design must avoid bypass paths that allow part of the spool weight to be carried directly by the printer frame.

Concept:

```text
              SPOOL
                |
          bearing/roller holder
                |
         spool-holder structure
                |
             LOAD CELL
                |
           printer/frame mount
```

The load-cell mechanism must still allow the spool to rotate with low and repeatable resistance.

### Electronics

Preferred architecture:

```text
load cell
   |
HX711-class ADC
   |
ESP32-S3-class spool controller
   |
USB preferred to CB2
```

Wi-Fi may be used for setup, diagnostics or OTA updates, but the installed printer should not require Wi-Fi for normal spool recognition or weighing.

### Remaining filament

For a known spool:

```text
remaining filament mass = measured gross mass - empty-spool tare mass
```

The database stores the tare mass for each spool geometry or individual spool where known.

Where material density is available, the host may also estimate remaining length from filament mass, diameter and density.

### Measurement policy

A rotating spool and filament tension can distort instantaneous weight readings. The implementation therefore distinguishes between:

- **stable measurement** — printer idle or spool stationary long enough to obtain a filtered value; authoritative for inventory correction;
- **dynamic measurement** — printing in progress; shown as an estimate/diagnostic but not trusted as a single final inventory value.

Preferred inventory workflow:

1. spool is installed;
2. tag is identified;
3. load-cell reading settles;
4. gross mass is recorded;
5. tare is subtracted;
6. remaining filament is displayed;
7. extrusion usage is tracked during the job as a secondary estimate;
8. when the spool becomes mechanically stable again, a new mass reading reconciles the inventory.

This hybrid approach detects mistakes such as a manually removed length of filament or a partially used spool transferred from another machine.

## Calibration and tare handling

The spool system must support:

- load-cell zero/tare calibration;
- calibration with one or more known reference masses;
- empty-holder tare;
- empty-spool tare by spool type;
- individual spool tare override;
- filtering and stable-reading detection;
- temperature/drift checks if required by testing.

The UI should make recalibration possible without editing configuration files manually.

## User experience

When a spool is loaded, the desired interaction is:

```text
+--------------------------------+
|       SPOOL DETECTED           |
|                                |
|  Bambu PLA Matte               |
|  Charcoal                      |
|  1.75 mm                       |
|                                |
|  Revival profile:              |
|  BAMBU_PLA_MATTE_V2            |
|                                |
|  Remaining: 642 g              |
|  Estimated length: ... m       |
|                                |
|  Ready                         |
+--------------------------------+
```

For a Revival-native tag, the same UI is used without exposing implementation details unless requested.

Unknown or partially decoded tags must fail gracefully and allow manual material/profile selection.

## Inventory model

Each physical spool record should be able to retain:

- spool UUID / source-tag UID;
- tag type/source (`REVIVAL`, `BAMBU`, manual);
- manufacturer and product;
- material and colour;
- purchase/creation date;
- nominal net mass;
- empty-spool tare;
- current measured remaining mass;
- estimated remaining length;
- material profile mapping;
- print history / consumption history;
- last stable weighing timestamp;
- drying history/status if implemented later.

The implementation may use an existing spool database component or a small project-specific service, but the on-disk data model and configuration must be exportable/versioned/documented so the project is not locked to a cloud service.

## Interface to Klipper and slicer workflow

RFID/NFC data must not directly and silently overwrite safety-critical settings.

The smart-spool service provides identity and material context to the host. Klipper/macros and the slicer integration may use that information to:

- show the active spool;
- check that loaded material is compatible with the queued job;
- select/suggest the corresponding Revival material profile;
- warn if estimated remaining mass is below the predicted job consumption plus safety margin;
- record consumption after the print.

Machine-specific tuning remains under version-controlled Revival profiles.

## Mechanical integration rules

The final spool holder must be designed as an integrated Generation 3 subsystem rather than adding a scale under a generic holder.

Requirements:

- preserve the classic i3 visual language;
- keep the RFID antenna close enough to the expected tag path;
- allow practical reading of both Revival and supported Bambu tags;
- isolate the load path through the sensor;
- provide low-friction spool rotation;
- provide mechanical overload protection for the load cell;
- provide cable strain relief;
- allow removal/replacement of reader and load cell without dismantling the printer frame;
- avoid allowing the filament feed direction to create excessive lateral force on the weight sensor.

## Frozen architectural decisions

- a Generation 3 smart-spool subsystem is part of the target final build;
- Revival-native writable RFID/NFC tags are the primary format;
- supported original Bambu RFID spools should be recognised and translated into the Revival data model;
- Bambu tags are read/imported, not emulated/counterfeited;
- detected material is mapped to a Revival-calibrated profile rather than blindly applying another printer's complete tuning;
- individual physical spools are tracked separately;
- automatic spool weighing is part of the target system;
- remaining mass is calculated from measured gross mass minus tare;
- stable load-cell measurements are authoritative; dynamic readings during printing are filtered/secondary;
- local reader/weighing electronics are separated from motion-control electronics;
- wired USB to the CB2 is the preferred host link for the installed subsystem;
- exact reader IC, antenna, load-cell rating/geometry and controller PCB remain open until spool-holder mechanical design.

## Open component-level decisions

- exact NFC/RFID reader IC and antenna geometry;
- exact ESP32-S3/module/PCB implementation;
- exact tag technology for Revival Spool Tag v1;
- exact load-cell type, rating and mounting arrangement;
- whether one sensor or multiple sensors are mechanically preferable;
- exact spool-holder geometry and bearings/rollers;
- database/service implementation;
- exact KlipperScreen/Mainsail UI integration;
- exact method for mapping supported Bambu material identifiers to Revival profiles;
- optional future drying-history and environmental sensing.