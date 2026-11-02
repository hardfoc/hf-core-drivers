# Using the drivers

Add the umbrella to a project and build the drivers a board needs, through hf-core or on their own.

## Through hf-core

[hf-core](https://github.com/hardfoc/hf-core) carries this repository as its `hf-core-drivers` submodule and
compiles a driver only when its switch is on. A board HAL sets the switches and includes the build settings:

```cmake
set(HF_CORE_MCU  "ESP32")
set(HF_CORE_RTOS "FREERTOS")
set(HF_CORE_ENABLE_TMC9660 ON)
set(HF_CORE_ENABLE_PCAL95555 ON)
set(HF_CORE_ENABLE_NTC_THERMISTOR ON)
include(path/to/hf-core/cmake/hf_core_build_settings.cmake)
# Outputs: HF_CORE_SOURCES, HF_CORE_INCLUDE_DIRS, HF_CORE_COMPILE_DEFINITIONS, HF_CORE_IDF_REQUIRES
```

For each enabled driver, `hf_core_build_settings.cmake` includes that driver's own
`external/<driver>/cmake/hf_<name>_build_settings.cmake`, and adds the platform layer from `internal/`. Clone
recursively, or initialise the submodules a board uses:

```bash
git clone --recurse-submodules https://github.com/hardfoc/hf-core.git
```

The switches and their defaults are documented on the [hf-core site](https://hardfoc.github.io/hf-core/).

## On their own

Every driver is a standalone repository with a CMake target and an ESP-IDF component; use it directly when you do
not need hf-core:

```bash
git submodule add https://github.com/hardfoc/hf-tmc9660-driver.git external/hf-tmc9660-driver
```

Each driver's Installation page lists its target, options and ESP-IDF component. Start from the
[driver catalogue](catalogue.md).

## The umbrella on its own

```bash
git submodule add https://github.com/hardfoc/hf-core-drivers.git hf-core-drivers
git -C hf-core-drivers submodule update --init --depth 1 external/hf-tmc9660-driver internal/hf-pincfg
```

The umbrella has no build files of its own: it pins versions. Initialise only the submodules you build.

Next: [Platform layer](internal.md).
