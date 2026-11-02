# How a driver is built

The shape every HardFOC driver shares, so that a driver written once runs on any MCU the platform supports.

| Layer | Lives in | Knows about |
| --- | --- | --- |
| Driver core | `external/<driver>/inc`, `src` | The chip: registers, commands, timing, units, faults |
| Communication interface | `external/<driver>/inc` | The handful of operations the driver needs: transfer, GPIO, delay |
| Platform port | hf-core handlers, or your project | The MCU, through `internal/hf-internal-interface-wrap` or the vendor SDK |

## The standard each driver is brought to

- **No platform code in the driver.** No ESP-IDF, STM32 HAL or RTOS includes in the driver core.
- **No exceptions, no heap in the hot path.** Results come back as status codes or `std::expected`-style types.
- **Host tests** against a mock of the communication interface, run in CI.
- **ESP32 examples**, built in CI from `examples/esp32/app_config.yml`.
- **A documentation site** with the standard page set: Quickstart, Installation, Hardware, Architecture, API
  guide, Porting, Examples, Testing and CI.

Drivers are moved to this standard one by one; each driver's Testing and CI page says what it has today.

The details (naming, error types, include order, Doxygen comments) are in the
[coding standards](coding-standards.md). The pilot for the current documentation and structure is the
[TMC9660 driver](https://hardfoc.github.io/hf-tmc9660-driver/).

Next: [Driver catalogue](catalogue.md).
