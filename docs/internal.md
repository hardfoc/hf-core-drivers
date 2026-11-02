# Platform layer

The two repositories under `internal/` that every driver and board HAL builds on.

| Path | What it is | Documentation |
| --- | --- | --- |
| `internal/hf-internal-interface-wrap` | Hardware-agnostic base classes for MCU peripherals (GPIO, ADC, I²C, SPI, UART, CAN, PWM, NVS, timers and more) with ESP32 implementations | [Site](https://hardfoc.github.io/hf-internal-interface-wrap/) · [GitHub](https://github.com/hardfoc/hf-internal-interface-wrap) |
| `internal/hf-pincfg` | Compile-time functional pin maps per board (Vortex V1, Flux V1) as X-macro rows | [Site](https://hardfoc.github.io/hf-pincfg/) · [GitHub](https://github.com/hardfoc/hf-pincfg) |

## How they fit together

- A **driver** in `external/` depends on neither: it defines its own small communication interface (a CRTP class or
  a few virtual methods) and never includes an MCU header.
- **hf-core handlers** implement each driver's interface on top of the `Base*` classes of the interface layer, so
  one adapter serves every MCU the interface layer supports.
- A **board HAL** selects its pin map with one `HARDFOC_BOARD_*` define and registers GPIO and ADC channels from it.

Porting to a new MCU means implementing the interface layer's `Base*` classes for it; the drivers do not change.

Next: [Updating submodules](submodules.md).
