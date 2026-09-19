# Generation 3 smart spool system

This document defines the target **Revival Smart Spool System** for the Generation 3 build.

The objective is to reproduce the useful part of the automatic-spool experience of modern systems while keeping the Revival independent, open, vendor-neutral and extensible:

- identify a loaded spool automatically;
- recognise Revival-native tags;
- recognise supported third-party smart-spool formats;
- learn from previously unseen tags and expand the local brand/format database;
- map detected material data to a **Revival-calibrated** filament profile;
- measure the installed spool mass and estimate remaining filament automatically;
- keep per-spool inventory/history;
- expose the result in the local HDMI5/KlipperScreen UI and to the host software.

The system is intentionally independent from the printer motion-control MCU. Failure of the spool-identification subsystem must not prevent safe manual operation of the printer.

The Generation 3 spool system is extended by **RASS — Revival Active Spool System**, which adds active spool rotation assistance, an upstream feeder and buffer/dancer-based tension control. See [`generation-3-rass.md`](generation-3-rass.md).

## Architectural principles

1. **Revival data model is native.** Every source tag is normalised into the same internal material/spool representation.
2. **Revival tags remain first-class.** Our own writable tag format is supported directly and can carry project-specific identifiers.
3. **Interoperability is preferred over vendor lock-in.** Open standards such as OpenPrintTag should be read directly where practical.
4. **Vendor compatibility is read/import compatibility, not emulation.** Supported Bambu, Creality and future vendor tags are translated into the Revival data model. The Revival must not depend on pretending to be another vendor's hardware.
5. **Material identity is separate from machine tuning.** Vendor tags may provide brand, family, colour, diameter and supplier limits/recommendations, but machine-specific parameters come from a profile calibrated for the Revival.
6. **A physical spool is tracked as an individual object.** Two nominally identical rolls remain two separate inventory records.
7. **Remaining filament is determined primarily from mass.** The system uses a load cell under the spool holder and subtracts the known empty-spool mass.
8. **Measurements during printing are treated as dynamic.** Final inventory correction is based on stable readings, not on a single instantaneous value affected by filament tension or spool acceleration.
9. **Unknown tags are data, not failures.** If a tag is readable but its format is unknown, the system records its fingerprint/raw accessible data and guides the user through registration rather than simply rejecting it.
10. **Learning is assisted and auditable.** The system may infer patterns from repeated tags, but it must not silently invent material identity or unsafe print parameters.

## Functional architecture

```text
                           LOADED SPOOL
                                |
          +---------------------+----------------------+
          |                     |                      |
   Revival native tag     Open standard tag      Vendor RFID/NFC
          |                     |                 (Bambu, Creality,
          |                     |                  future formats)
          +---------------------+----------------------+
                                |
                       multi-protocol reader
                                |
                        local controller
                      (ESP32-S3 class)
                                |
          +---------------------+----------------------+
          |                     |                      |
       tag probe           decoder registry        load-cell ADC
          |                     |                  (HX711 class)
          +----------+----------+----------------------+
                     |
             Revival spool service
                     |
       +-------------+--------------+----------------+
       |                            |                |
  brand/format DB             filament DB      Klipper/Moonraker
       |                            |                |
 decoder/profile map                +--------+-------+
       |                                     |
       +-------------------------------+-----+
                                       |
                                    HDMI5 UI
                                       |
                          identity / colour / mass /
                           profile / warnings / learn
```

The exact reader IC, antenna geometry and local-controller board are intentionally left open until the spool-holder geometry is designed. **PN5180-class reader + ESP32-S3 + HX711-class load-cell ADC** is the current preferred implementation direction.

## Normalised Revival spool record

Regardless of tag source, the decoder produces a common internal record where available:

- source format (`REVIVAL`, `OPENPRINTTAG`, `BAMBU`, `CREALITY`, `UNKNOWN`, future plugins);
- source UID / physical tag identifier;
- manufacturer/brand;
- product/family name;
- material family (PLA, PETG, ASA, TPU, etc.);
- material modifier/variant (Tough, Matte, CF, Silk, HF, 95A, etc.);
- colour name;
- colour RGB/RGBA value;
- nominal diameter;
- nominal net filament mass;
- known empty-spool/tare mass or spool family;
- optional production/lot identifiers;
- supplier temperature/drying information where available;
- Revival material-profile key;
- decoder confidence/provenance.

No third-party field is automatically treated as a Revival machine-tuning value unless explicitly mapped by a calibrated profile.

## Revival-native spool tags

The project will define a versioned format, provisionally named **Revival Spool Tag v1**.

The physical tag should be writable, inexpensive and replaceable. The tag should carry stable identification and basic material data; frequently changing inventory data belongs in the host database.

Recommended fields:

- format/version identifier;
- unique spool UUID;
- manufacturer;
- product/family name;
- material family and modifier;
- colour name and RGB/RGBA value;
- nominal diameter;
- nominal net filament mass;
- empty-spool/tare mass where known;
- optional lot/batch identifier;
- optional production/purchase date;
- profile key used to locate the corresponding Revival material profile.

The tag should **not** be the only storage location for current remaining mass, print history, calibration history, pressure advance, flow ratio, volumetric-flow limit, retraction, cooling tuning or other machine-specific tuning.

### OpenPrintTag interoperability

The Revival format remains our native project format, but the reader and database should also support **OpenPrintTag** directly because it is an open, offline smart-spool standard intended for cross-vendor use.

Where useful, Revival-native tags may later be made interoperable with or derived from an OpenPrintTag-compatible representation while retaining project-specific data in the Revival database. This choice is intentionally left open until the tag schema is finalised.

## Decoder registry and vendor adapters

Tag support is implemented as independent decoder modules rather than hard-coded printer logic.

Conceptual registry:

```text
Tag detected
    |
    +-- Revival decoder
    +-- OpenPrintTag decoder
    +-- Bambu decoder
    +-- Creality decoder
    +-- future vendor/plugin decoders
    +-- unknown-tag learner
```

The decoder registry allows new formats to be added without changing the rest of the spool, weighing or Klipper integration code.

### Priority tiers

**Tier 1 — required baseline**

- Revival Spool Tag;
- OpenPrintTag;
- Bambu Lab RFID.

**Tier 2 — planned compatibility**

- Creality smart-spool/CFS RFID;
- other documented, technically readable vendor formats as they are validated with real samples.

**Tier 3 — opportunistic/future**

- additional vendors discovered after the Generation 3 build;
- community/open formats not known when the initial firmware is released.

A format is only promoted to supported status after real tags have been tested and the extracted fields have been validated.

## Bambu Lab compatibility layer

When a supported original Bambu RFID spool is detected, the reader service should extract the available tag data and translate it into the Revival data model.

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

A previously unseen Bambu material must not silently inherit aggressive machine parameters. The UI identifies it as a new material and offers a compatible generic/base Revival profile until calibration is completed.

Supplier-provided temperature information may seed or constrain a profile, but the final print settings remain Revival-specific.

## Adaptive unknown-tag learning

A key requirement is that the machine can encounter a spool/tag that was not known when the software was written and still make useful progress.

### Stage 1 — physical/protocol fingerprint

On every tag, the reader records what can be obtained safely from the underlying NFC/RFID protocol, for example:

- protocol/family;
- UID length/value;
- ATQA/SAK or equivalent identification fields where applicable;
- memory size/page/block layout where readable;
- writable/read-only/locked state where detectable;
- authentication requirement;
- raw accessible user-memory bytes;
- NDEF records where present.

This fingerprint is used to match known decoders before asking the user for anything.

### Stage 2 — known-format probe

All registered decoders run non-destructive recognition checks. A decoder returns:

- no match;
- possible match;
- confirmed match;
- decoded fields plus confidence/provenance.

No decoder may write to an unknown vendor tag during detection.

### Stage 3 — unknown format workflow

If no decoder matches, the UI displays an **Unknown smart spool** workflow instead of failing:

```text
UNKNOWN SMART SPOOL

Tag family: MIFARE / NTAG / other
UID: ...
Readable data: yes / partial / protected
Known format: no

[ Identify manufacturer ]
[ Register spool manually ]
[ Save tag sample for analysis ]
```

The user can provide manufacturer, product, material and colour. The spool becomes usable immediately through a manual/assisted Revival record while the unknown source format remains linked to it.

### Stage 4 — local brand and format learning

The database stores repeated observations under a **brand/format signature**. Examples of useful evidence include:

- several tags from the same manufacturer;
- bytes/records that stay constant between products;
- bytes that correlate with known material, colour or nominal weight;
- known text/ASCII fields;
- known NDEF keys;
- UID/protocol patterns;
- spool dimensions and tare families entered by the user.

When enough evidence exists, a new decoder definition can be created and versioned. New observations may suggest mappings, but user confirmation is required before a field becomes authoritative.

The intended result is a growing local knowledge base, for example:

```text
brands/
  bambu/
    decoder-version: 1
    materials: ...
  creality/
    decoder-version: 1
    materials: ...
  unknown-brand-003/
    samples: 4
    status: learning
    candidate-fields:
      material: probable
      colour: confirmed
```

### Stage 5 — decoder promotion

Once a learned mapping is validated against multiple real tags, it becomes a named decoder plugin and future rolls from that source are recognised automatically.

The project should preserve decoder test samples/fixtures in a privacy-safe form where possible so regressions can be tested after software updates.

### Limits of learning

"Learning" does **not** mean the printer can magically decrypt or reverse-engineer every protected tag.

If a tag requires unknown cryptographic keys, secure authentication, inaccessible memory or unsupported radio hardware, the system may only be able to identify the physical tag family/UID and ask for manual spool data until a legitimate decoder becomes available.

Manual registration must always remain available.

## Brand and material database

The database is not only an inventory of individual spools. It also becomes an expandable catalogue of manufacturers and products.

Suggested hierarchy:

```text
brand
  |
  +-- product/family
        |
        +-- material variant
              |
              +-- colours
              +-- supplier metadata
              +-- Revival calibrated profiles
              +-- known tag signatures/decoders
              +-- spool tare families
```

When the user registers an unknown roll, the system can:

1. search for an existing brand;
2. create the brand if it does not exist;
3. create or select the product/material family;
4. link the observed RFID/NFC fingerprint;
5. store measured tare/weight information;
6. map or create a Revival profile;
7. reuse that knowledge automatically on later rolls.

The database must be exportable, backed up locally and stored in a documented format. Cloud access may be added later but is never required for basic recognition.

## Spool weighing and remaining-filament estimation

### Mechanical principle

The complete spool-support load must pass through a load cell or load-cell arrangement. The design must avoid bypass paths that allow part of the spool weight to be carried directly by the printer frame.

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

The database stores the tare mass for each spool geometry or individual spool where known. Where material density is available, the host may also estimate remaining length from filament mass, diameter and density.

### Measurement policy

A rotating spool and filament tension can distort instantaneous weight readings. The implementation distinguishes between:

- **stable measurement** — printer idle or spool stationary long enough to obtain a filtered value; authoritative for inventory correction;
- **dynamic measurement** — printing in progress; shown as an estimate/diagnostic but not trusted as a single final inventory value.

Preferred inventory workflow:

1. spool is installed;
2. tag is identified or registered;
3. load-cell reading settles;
4. gross mass is recorded;
5. tare is subtracted;
6. remaining filament is displayed;
7. extrusion usage is tracked during the job as a secondary estimate;
8. when the spool becomes mechanically stable again, a new mass reading reconciles the inventory.

This hybrid approach detects a manually removed length of filament or a partially used spool transferred from another machine.

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

### Known spool

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

### Unknown spool

```text
+--------------------------------+
|      NEW SMART SPOOL           |
|                                |
| Tag detected but format is     |
| not yet known.                 |
|                                |
| Manufacturer: [ select/add ]   |
| Product:      [ enter       ]  |
| Material:     [ select      ]  |
| Colour:       [ select      ]  |
|                                |
| [ Save + learn this format ]   |
+--------------------------------+
```

Unknown or partially decoded tags must fail gracefully and allow manual material/profile selection immediately.

## Inventory model

Each physical spool record should retain:

- spool UUID / source-tag UID;
- tag type/source;
- decoder/version and confidence;
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
- drying history/status if implemented later;
- link to any unknown-format fingerprint/sample used for learning.

## Interface to Klipper and slicer workflow

RFID/NFC data must not directly and silently overwrite safety-critical settings.

The smart-spool service provides identity and material context to the host. Klipper/macros and slicer integration may use that information to:

- show the active spool;
- check that loaded material is compatible with the queued job;
- select/suggest the corresponding Revival material profile;
- warn if estimated remaining mass is below predicted job consumption plus safety margin;
- record consumption after the print;
- flag a new/unknown material that still needs calibration.

Machine-specific tuning remains under version-controlled Revival profiles.

## Mechanical integration rules

The final spool holder must be designed as an integrated Generation 3 subsystem rather than adding a scale under a generic holder.

Requirements:

- preserve the classic i3 visual language;
- keep the RFID/NFC antenna close enough to the expected tag path;
- accommodate multiple supported tag technologies within the selected reader's capability;
- isolate the load path through the sensor;
- provide low-friction spool rotation;
- provide mechanical overload protection for the load cell;
- provide cable strain relief;
- allow removal/replacement of reader and load cell without dismantling the printer frame;
- avoid allowing the filament feed direction to create excessive lateral force on the weight sensor.

## Frozen architectural decisions

- a Generation 3 smart-spool subsystem is part of the target final build;
- Revival-native writable RFID/NFC tags are supported as a primary format;
- OpenPrintTag compatibility is part of the target interoperability layer;
- supported original Bambu RFID spools are read and translated into the Revival data model;
- Creality smart-spool RFID is a planned compatibility target once validated with real samples;
- vendor tags are read/imported, not emulated/counterfeited;
- a plugin/decoder registry is used so new tag formats can be added independently;
- unknown readable tags enter an assisted learning/registration workflow instead of being rejected;
- the local database can create new brands, products, materials, spool families and format signatures from user-confirmed observations;
- learned field mappings require validation before becoming authoritative decoders;
- protected/encrypted formats that cannot yet be decoded fall back to UID/fingerprint + manual registration;
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
- exact tag technology/schema for Revival Spool Tag v1;
- exact degree of OpenPrintTag interoperability for Revival-native tags;
- exact load-cell type, rating and mounting arrangement;
- whether one sensor or multiple sensors are mechanically preferable;
- exact spool-holder geometry and bearings/rollers;
- database/service implementation;
- exact on-disk decoder/plugin schema;
- exact KlipperScreen/Mainsail UI integration;
- exact method for mapping supported vendor material identifiers to Revival profiles;
- future vendor decoders and their test fixtures;
- optional future drying-history and environmental sensing.
