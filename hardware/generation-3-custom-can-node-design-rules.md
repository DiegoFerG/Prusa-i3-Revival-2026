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

## Mandatory expansion reserve

The final MCU and pin allocation for **each** custom board must leave the following resources unused by frozen baseline functions and physically accessible for future expansion.

### EXP-SPI

Provide at least one spare SPI-capable expansion position with:

- SCK;
- MOSI;
- MISO;
- at least one dedicated chip-select GPIO;
- at least one additional GPIO suitable for IRQ/READY/BUSY use;
- 3.3 V;
- GND.

A dedicated unused hardware SPI controller is preferred. If MCU resource pressure makes a shared SPI bus preferable, the expansion device must still receive its own CS and IRQ-capable GPIO and the signal-integrity/loading implications must be reviewed.

The RASS RFID reader does **not** consume the mandatory spare expansion position: an additional SPI expansion position must remain available after the production RFID interface is allocated.

The Bed Node accelerometers do **not** consume the mandatory spare expansion position: an additional SPI expansion position must remain available after the production IMU interfaces are allocated.

### EXP-I2C

Provide one spare I2C expansion interface with:

- SDA;
- SCL;
- 3.3 V;
- GND;
- optional regulated 5 V power only when the connector and board documentation make clear that the I/O logic itself remains at the correct MCU voltage.

Pull-up strategy must be documented so future modules do not create excessive parallel pull-up loading.

### EXP-UART

Reserve and expose at least one unused hardware UART-capable TX/RX pair, plus GND and an appropriate logic-power reference.

If the selected MCU provides useful hardware flow-control pins without compromising the rest of the design, CTS/RTS should also be reserved or made available on test pads.

The presence of a hardware UART reserve does not imply that upstream Klipper exposes every arbitrary UART use case as a generic host API; future use must remain compatible with the frozen upstream-firmware policy.

### EXP-ANALOG

Reserve at least **two unused ADC-capable MCU inputs** after all production measurements are allocated.

The external connector or test-point implementation must include appropriate protection/filtering when signals can leave the PCB or come from electrically noisy areas.

### EXP-GPIO / PWM

Reserve at least **four general-purpose GPIOs** after all production functions are allocated.

Where the selected MCU permits practical pin assignment, at least **two of those spare GPIOs should be timer/PWM-capable**.

At least one spare GPIO should be suitable for an external interrupt/event input.

### Power rails

Expansion headers should expose:

- GND;
- regulated 3.3 V;
- regulated 5 V where the board power budget supports it.

Available current must be specified in the released board documentation. Expansion connectors must not be treated as an undocumented source of heater, motor or other high-current power.

## Debug and recovery reserve

Both custom boards must provide practical access to:

- BOOT/recovery mechanism appropriate to the selected MCU;
- RESET;
- the MCU-native debug/programming interface where practical, for example SWD on STM32;
- labelled test points for CAN-H, CAN-L, main logic rails and ground.

USB-C service/recovery remains strongly preferred when compatible with the selected MCU and board topology.

## MCU selection rule

The MCU is **not acceptable** merely because it can run Klipper and satisfy the current I/O list.

After allocating all frozen production functions, it must still satisfy the mandatory expansion reserve above.

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
- ability to preserve the mandatory expansion reserve without unsafe pin multiplexing.

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
- spare SPI/I2C/UART/ADC/GPIO/PWM resources still available;
- boot/debug pins;
- pins that must never be used because of boot, crystal, USB, CAN or other hardware constraints.

A board is not considered design-complete until this ledger proves that the mandatory expansion reserve survived the final schematic and PCB pin assignment.

## Safety boundary

Expansion capacity is for diagnostics, sensing and validated auxiliary functions.

No future plug-in expansion may silently become the sole protection for:

- mains isolation;
- protective earth;
- over-current protection;
- heated-bed thermal protection;
- emergency energy removal;
- other safety-critical functions that the Generation 3 architecture requires to remain independent of Linux/Klipper/CAN.
