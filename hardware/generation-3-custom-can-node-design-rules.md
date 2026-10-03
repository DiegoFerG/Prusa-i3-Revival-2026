# Generation 3 custom CAN node design rules

This document defines the common electrical, firmware and expansion rules for Revival-designed Klipper CAN boards. It currently applies to the **Revival Bed Node** and the **RASS CAN Node**.

The purpose is to keep both boards maintainable with normal upstream Klipper while deliberately preserving hardware capacity for future sensors and peripherals.

## Frozen firmware policy

Both custom boards shall run **unmodified upstream Klipper MCU firmware**.

This means:

- the MCU firmware must be buildable from the normal upstream Klipper source tree;
- board-specific `make menuconfig` selections, pin maps, Klipper configuration includes and build documentation are expected;
- an upstream-compatible CAN bootloader/update path may be used where appropriate;
- USB boot/recovery support may be provided by the selected MCU and board design;
- Revival-specific behaviour should be implemented in host-side Python modules/services, Klipper configuration/macros, Moonraker integrations or other Linux-host software;
- no production requirement may depend on a private Klipper MCU fork, patched `src/` tree, private MCU protocol command or custom C firmware command.

If a future peripheral cannot be supported without modifying Klipper MCU firmware, the first design responses are to change the peripheral/interface, use an upstream-supported bus primitive, move the logic to the Linux host, or introduce a separate bridge/coprocessor. Accepting a Klipper MCU fork would be an explicit architecture change that must supersede this frozen rule in the Decision Log.

The repository must record the upstream Klipper revision/hash used to validate each released board.

## Host versus MCU responsibility

The custom CAN MCU is responsible for deterministic local I/O that upstream Klipper already supports: pins, timers, ADCs, steppers, heaters/PWM where relevant, and supported bus transactions.

Revival-specific semantics belong on the Linux host whenever practical.

Examples:

- Bed Node: RID interpretation, history and high-level diagnostics are host responsibilities.
- RASS Node: RFID/NFC electrical acquisition may occur on the node, but vendor/tag/material decoding, inventory and profile mapping are host responsibilities.
- CB1 may provide the Linux-host role during bench development; CB2 is the final Generation 3 host.

This boundary deliberately keeps the custom PCBs useful across normal Klipper updates.

## Full unused-pin exposure policy

The Revival does **not** use a minimum-reserve model for its custom CAN boards.

After all frozen production functions are assigned, **every remaining electrically usable MCU pin must be physically exposed for future use** on the Bed Node and RASS CAN Node. The objective is to avoid stranding MCU capability inside the PCB.

This rule applies to all unused MCU pins that can safely be made available, including pins whose alternate functions can provide:

- SPI;
- I2C;
- UART/USART;
- ADC;
- timer/PWM;
- external interrupt/event input;
- ordinary digital GPIO;
- other upstream-Klipper-compatible peripheral functions supported by the selected MCU.

### What counts as exposed

An unused pin is considered exposed only when it is reachable without PCB modification through one of:

- a labelled expansion connector;
- a labelled through-hole header position;
- a deliberately provided, accessible solder pad/test pad intended for expansion.

Merely routing a trace to an inaccessible via does not satisfy this rule.

Where practical, related signals should be grouped into useful expansion headers — for example SPI + CS + IRQ + power, I2C + power, or UART + power — while still exposing any remaining individual pins that do not fit those groups.

### Exceptions

A pin may remain unavailable only when there is a documented hardware reason, for example:

- it is committed to CAN, USB, SWD/debug, BOOT/RESET or the selected bootloader/recovery scheme;
- it is required by the crystal/oscillator or other mandatory clock circuitry;
- it is tied to power, reference, regulator or other non-GPIO MCU functions;
- exposing it would violate MCU boot-strapping requirements or create a credible electrical/safety hazard;
- package-specific restrictions make it unusable in the selected board configuration.

Such pins must still appear in the resource ledger with the reason they are unavailable.

SWD/debug, BOOT and RESET are not treated as lost resources: they must be exposed separately as service/debug access. Where the selected MCU requires manual BOOT/BOOTSEL and RESET intervention for commissioning or recovery, **dedicated tactile pushbuttons shall be fitted on the PCB**, following the serviceability model used by the EBB36.

### Alternate-function documentation

For every exposed unused MCU pin, the released board documentation must record:

- MCU pin name;
- PCB connector/pad and pin number;
- logic voltage;
- ADC capability where applicable;
- timer/PWM capability where applicable;
- SPI/I2C/UART alternate functions that remain usable with the final pin mux;
- boot/debug/electrical caveats;
- any external protection, pull-up/down or filtering already attached to the pin.

This documentation is authoritative for future expansions.

### Bus-oriented expansion

Because future peripherals are likely to use buses, the PCB layout should still group exposed pins into convenient bus-oriented connectors whenever practical.

However, these grouped connectors are **in addition to**, not a substitute for, the full-unused-pin rule. If an MCU has more unused pins than are needed for the grouped SPI/I2C/UART headers, the remaining safe unused pins must still be exposed.

### Power rails

Expansion areas should make nearby access available to:

- GND;
- regulated 3.3 V;
- regulated 5 V where the board power budget supports it.

Available current must be specified in the released board documentation. Expansion connectors must not be treated as an undocumented source of heater, motor or other high-current power.

## Debug and recovery reserve

Both custom boards must provide practical access to:

- a **dedicated BOOT/BOOTSEL pushbutton** when the selected MCU/boot scheme benefits from or requires manual boot-mode entry;
- a **dedicated RESET pushbutton** when supported/required by the selected MCU;
- the MCU-native debug/programming interface, for example **SWDIO + SWCLK + GND + 3.3 V reference** on a keyed header or clearly labelled service pads for STM32-class designs;
- labelled test points for CAN-H, CAN-L, main logic rails and ground.

SWD is a debug/programming interface, not a pushbutton function; it must remain physically accessible without dismantling or desoldering the board. USB-C service/recovery remains strongly preferred when compatible with the selected MCU and board topology.

## MCU selection rule

The MCU is **not acceptable** merely because it can run Klipper and satisfy the current I/O list.

After allocating all frozen production functions, the selected MCU/package must still permit every remaining electrically usable MCU pin to be exposed in accordance with the full unused-pin policy above.

MCU selection therefore considers:

- upstream Klipper CAN support;
- USB/recovery options;
- timer/stepper resources;
- SPI/I2C/UART peripheral count and pin mapping;
- ADC channel count and quality;
- available GPIO/PWM resources;
- flash/RAM margin;
- package/routing practicality;
- availability and lifecycle;
- ability to expose all remaining electrically usable MCU pins without unsafe pin multiplexing or impractical routing.

A larger MCU/package is preferred over consuming every peripheral at initial release.

## Connector and labelling rules

Exact connector families remain open until PCB layout, enclosure and harness design.

Released boards must nevertheless:

- key external connectors where practical;
- label voltage and signal orientation clearly on silkscreen;
- distinguish 3.3 V logic from any 5 V power rail;
- avoid exposing raw high-current paths on generic expansion headers;
- document connector pinout, logic voltage, maximum current and MCU pin mapping;
- reserve service loops/strain relief where a cable leaves the enclosure.

## Resource ledger

Each released PCB must include a versioned resource ledger in the repository showing:

- MCU part and package;
- each hardware peripheral used by baseline functions;
- each assigned pin;
- each expansion connector;
- every remaining unused MCU pin, its alternate-function capabilities and its physical expansion connector/pad;
- boot/debug pins;
- pins that must never be used because of boot, crystal, USB, CAN or other hardware constraints.

A board is not considered design-complete until this ledger accounts for **every MCU pin** and proves that every electrically usable pin not consumed by the production design is physically exposed, with documented exceptions for pins that cannot safely be made available.

## Safety boundary

Expansion capacity is for diagnostics, sensing and validated auxiliary functions.

No future plug-in expansion may silently become the sole protection for:

- mains isolation;
- protective earth;
- over-current protection;
- heated-bed thermal protection;
- emergency energy removal;
- other safety-critical functions that the Generation 3 architecture requires to remain independent of Linux/Klipper/CAN.
