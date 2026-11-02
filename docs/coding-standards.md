# Coding standards

The naming, error-handling, memory and documentation rules shared by the HardFOC drivers, in brief.

The full text, with rationale and examples, is [`CODING_STANDARDS.md`](../CODING_STANDARDS.md). When a driver's
existing code uses a different but consistent style, match the file you are editing.

## Naming

| Element | Convention | Example |
| --- | --- | --- |
| Public functions | PascalCase | `Init()`, `EnableChannel()` |
| Private functions | camelCase | `checkInitialized()`, `transferFrame()` |
| Member variables | snake_case with trailing `_` | `comm_`, `initialized_` |
| Static member variables | snake_case with trailing `_` | `instance_count_` |
| Global variables | `g_` prefix, snake_case | `g_transfer_count` |
| Constants (`constexpr`, `const`) | UPPER_CASE | `MAX_CHANNELS`, `CH_CTRL` |
| Enum classes | PascalCase | `DriverError`, `ChannelMode` |
| Enum values (errors, states) | PascalCase | `None`, `NotInitialized` |
| Enum values (flags, bits) | UPPER_CASE | `CRC_ERROR` |
| Local variables, parameters | snake_case | `current_value`, `current_ma` |
| Type aliases, classes, structs | PascalCase | `CommResult`, `ChannelConfig`, `MAX22200` |
| Namespaces | lowercase (preferred) | `max22200`, `tmc9660` |
| Macros | UPPER_CASE | `DEVICE_HPP` |
| Files | lowercase with underscores | `max22200_spi_interface.hpp` |
| Repositories | lowercase with dashes | `hf-max22200-driver` |

Prefer full words (`channel`, not `ch`) and put units in names (`current_setpoint_ma_`).

## Code organisation

- Include guards (`#ifndef DEVICE_HPP`), then includes in the order: system headers, third-party headers, the
  driver's own headers.
- Classes list public, then protected, then private members; within a section constructors first and data members
  last.
- Fixed-width integer types (`uint8_t`, `int32_t`) for anything that maps to hardware.

## Errors

- C++ drivers return results: `std::expected` on C++23, or the driver's own `expected`-style polyfill on C++20.
- C code returns status codes.
- Every call that can fail is checked and its error propagated; no silent fallbacks.

## Memory and threads

- Stack and static storage first; RAII for every resource; smart pointers when dynamic allocation is unavoidable.
- Drivers are not thread-safe by default: the caller synchronises shared access unless a function is documented
  as thread-safe.
- Document which functions are thread-safe; protect shared state with `std::atomic` or a mutex, and prefer class
  members to globals.

## Documentation

- Doxygen comments (`@brief`, `@param`, `@return`) on every public declaration.
- Inline comments say why, not what.
- Documentation sites follow the HardFOC
  [documentation style guide](https://github.com/hardfoc/hf-general-ci-tools/blob/main/docs/DOCS-STYLE-GUIDE.md).
