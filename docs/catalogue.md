# Driver catalogue

Every driver in the umbrella, grouped by what it controls, with its bus and a link to its documentation site.

The cards are generated from [`.gitmodules`](../.gitmodules) and the facts in
[`tools/docs/drivers.yml`](../tools/docs/drivers.yml); CI fails when a submodule is added without a card.

<!-- generated: catalogue -->
## Motor and actuator control

<div class="grid" markdown>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Smart servo (wrapper around the DYNAMIXEL SDK)</span>
<span class="hf-chip__name">DYNAMIXEL X-series</span>
<span class="hf-chip__vendor">ROBOTIS</span>
</div>

Bus
:   Half-duplex UART (Protocol 2.0)

Language
:   C++17

[Documentation](https://hardfoc.github.io/hf-dynamixel-driver/) · [GitHub](https://github.com/hardfoc/hf-dynamixel-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">CANopen client for Vortex motor controllers (CiA 301 / 402)</span>
<span class="hf-chip__name">HardFOC Vortex</span>
<span class="hf-chip__vendor">HardFOC</span>
</div>

Bus
:   CAN

Language
:   C++20

No site yet · [GitHub](https://github.com/hardfoc/hf-vortex-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Octal solenoid and motor driver</span>
<span class="hf-chip__name">MAX22200</span>
<span class="hf-chip__vendor">Analog Devices</span>
</div>

Bus
:   SPI

Language
:   C++20

[Documentation](https://hardfoc.github.io/hf-max22200-driver/) · [GitHub](https://github.com/hardfoc/hf-max22200-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Six-channel low-side solenoid driver</span>
<span class="hf-chip__name">TLE92466ED</span>
<span class="hf-chip__vendor">Infineon</span>
</div>

Bus
:   SPI

Language
:   C++20

[Documentation](https://hardfoc.github.io/hf-tle92466ed-driver/) · [GitHub](https://github.com/hardfoc/hf-tle92466ed-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Stepper motor controller and driver</span>
<span class="hf-chip__name">TMC5130 / TMC5160</span>
<span class="hf-chip__vendor">Analog Devices (Trinamic)</span>
</div>

Bus
:   SPI or UART

Language
:   C++17

[Documentation](https://hardfoc.github.io/hf-tmc5160-driver/) · [GitHub](https://github.com/hardfoc/hf-tmc5160-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">BLDC / stepper / DC motor controller with on-chip FOC</span>
<span class="hf-chip__name">TMC9660</span>
<span class="hf-chip__vendor">Analog Devices (Trinamic)</span>
</div>

Bus
:   SPI or UART (TMCL)

Language
:   C++20

[Documentation](https://hardfoc.github.io/hf-tmc9660-driver/) · [GitHub](https://github.com/hardfoc/hf-tmc9660-driver)
</div>

</div>

## Position and motion sensing

<div class="grid" markdown>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Magnetic rotary position encoder</span>
<span class="hf-chip__name">AS5047U</span>
<span class="hf-chip__vendor">ams OSRAM</span>
</div>

Bus
:   SPI

Language
:   C++20

[Documentation](https://hardfoc.github.io/hf-as5047u-driver/) · [GitHub](https://github.com/hardfoc/hf-as5047u-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">9-axis IMU and sensor-fusion hub</span>
<span class="hf-chip__name">BNO080 / BNO085 / BNO086</span>
<span class="hf-chip__vendor">CEVA (Hillcrest)</span>
</div>

Bus
:   I²C

Language
:   C++

[Documentation](https://hardfoc.github.io/hf-bno08x-driver/) · [GitHub](https://github.com/hardfoc/hf-bno08x-driver)
</div>

</div>

## Data conversion

<div class="grid" markdown>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">12-channel 12-bit SAR ADC</span>
<span class="hf-chip__name">ADS7952</span>
<span class="hf-chip__vendor">Texas Instruments</span>
</div>

Bus
:   SPI

Language
:   C++20

[Documentation](https://hardfoc.github.io/hf-ads7952-driver/) · [GitHub](https://github.com/hardfoc/hf-ads7952-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">16-channel 16-bit simultaneous-sampling SAR ADC</span>
<span class="hf-chip__name">ADS9324</span>
<span class="hf-chip__vendor">Texas Instruments</span>
</div>

Bus
:   SPI

Language
:   C++20

[Documentation](https://hardfoc.github.io/hf-ads9324-driver/) · [GitHub](https://github.com/hardfoc/hf-ads9324-driver)
</div>

</div>

## Environmental and process sensors

<div class="grid" markdown>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Mass flow meter and controller</span>
<span class="hf-chip__name">BASIS-2</span>
<span class="hf-chip__vendor">Alicat Scientific</span>
</div>

Bus
:   Modbus RTU over UART

Language
:   C++17

[Documentation](https://hardfoc.github.io/hf-alicat-basis2-driver/) · [GitHub](https://github.com/hardfoc/hf-alicat-basis2-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Barometric pressure sensor</span>
<span class="hf-chip__name">BMP581</span>
<span class="hf-chip__vendor">Bosch Sensortec</span>
</div>

Bus
:   I²C or SPI

Language
:   C++17 (header-only)

[Documentation](https://hardfoc.github.io/hf-bmp581-driver/) · [GitHub](https://github.com/hardfoc/hf-bmp581-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Optical oxygen sensor</span>
<span class="hf-chip__name">FDO2-G2</span>
<span class="hf-chip__vendor">PyroScience</span>
</div>

Bus
:   UART

Language
:   C++17

[Documentation](https://hardfoc.github.io/hf-fdo2-driver/) · [GitHub](https://github.com/hardfoc/hf-fdo2-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Analog temperature sensor</span>
<span class="hf-chip__name">MCP9700 / MCP9700A</span>
<span class="hf-chip__vendor">Microchip</span>
</div>

Bus
:   ADC

Language
:   C++17

[Documentation](https://hardfoc.github.io/hf-mcp9700-driver/) · [GitHub](https://github.com/hardfoc/hf-mcp9700-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Thermistor temperature (table</span>
<span class="hf-chip__name">NTC thermistor</span>
<span class="hf-chip__vendor">Generic</span>
</div>

Bus
:   ADC

Language
:   C++

[Documentation](https://hardfoc.github.io/hf-ntc-thermistor-driver/) · [GitHub](https://github.com/hardfoc/hf-ntc-thermistor-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">SF06-family gas mass flow meter</span>
<span class="hf-chip__name">SFM4300</span>
<span class="hf-chip__vendor">Sensirion</span>
</div>

Bus
:   I²C

Language
:   C++17 (header-only)

[Documentation](https://hardfoc.github.io/hf-sfm-flow-meter-driver/) · [GitHub](https://github.com/hardfoc/hf-sfm-flow-meter-driver)
</div>

</div>

## I/O, PWM and display

<div class="grid" markdown>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">96 × 64 RGB OLED SmartDisplay pushbutton</span>
<span class="hf-chip__name">ISF15ACP4</span>
<span class="hf-chip__vendor">NKK Switches</span>
</div>

Bus
:   SPI

Language
:   C++20

[Documentation](https://hardfoc.github.io/hf-isf15acp4-driver/) · [GitHub](https://github.com/hardfoc/hf-isf15acp4-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">16-bit I/O expander</span>
<span class="hf-chip__name">PCA9555 / PCAL9555A</span>
<span class="hf-chip__vendor">NXP</span>
</div>

Bus
:   I²C

Language
:   C++

[Documentation](https://hardfoc.github.io/hf-pcal95555-driver/) · [GitHub](https://github.com/hardfoc/hf-pcal95555-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">16-channel 12-bit PWM controller</span>
<span class="hf-chip__name">PCA9685</span>
<span class="hf-chip__vendor">NXP</span>
</div>

Bus
:   I²C

Language
:   C++

[Documentation](https://hardfoc.github.io/hf-pca9685-driver/) · [GitHub](https://github.com/hardfoc/hf-pca9685-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Addressable RGB(W) LEDs</span>
<span class="hf-chip__name">WS2812 / NeoPixel</span>
<span class="hf-chip__vendor">Worldsemi</span>
</div>

Bus
:   ESP32 RMT

Language
:   C++ (ESP32 only)

[Documentation](https://hardfoc.github.io/hf-ws2812-rmt-driver/) · [GitHub](https://github.com/hardfoc/hf-ws2812-rmt-driver)
</div>

</div>

## Power, memory and security

<div class="grid" markdown>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Serial EEPROM</span>
<span class="hf-chip__name">AT25010B / AT25020B / AT25040B</span>
<span class="hf-chip__vendor">Microchip</span>
</div>

Bus
:   SPI

Language
:   C++17 (header-only)

[Documentation](https://hardfoc.github.io/hf-at25040-driver/) · [GitHub](https://github.com/hardfoc/hf-at25040-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">PMIC with 3 buck</span>
<span class="hf-chip__name">PF1550</span>
<span class="hf-chip__vendor">NXP</span>
</div>

Bus
:   I²C

Language
:   C++20 (header-only)

[Documentation](https://hardfoc.github.io/hf-pf1550-driver/) · [GitHub](https://github.com/hardfoc/hf-pf1550-driver)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">EdgeLock secure element</span>
<span class="hf-chip__name">SE050</span>
<span class="hf-chip__vendor">NXP</span>
</div>

Bus
:   I²C (T=1)

Language
:   C++17

[Documentation](https://hardfoc.github.io/hf-se050-driver/) · [GitHub](https://github.com/hardfoc/hf-se050-driver)
</div>

</div>

## Platform layer (internal/)

<div class="grid" markdown>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">MCU peripheral interfaces (GPIO</span>
<span class="hf-chip__name">Base interfaces</span>
<span class="hf-chip__vendor">HardFOC</span>
</div>

Bus
:   All

Language
:   C++

[Documentation](https://hardfoc.github.io/hf-internal-interface-wrap/) · [GitHub](https://github.com/hardfoc/hf-internal-interface-wrap)
</div>

<div class="hf-chip" markdown>
<div class="hf-chip__head">
<span class="hf-chip__kicker">Compile-time functional pin maps per board (Vortex V1</span>
<span class="hf-chip__name">Pin maps</span>
<span class="hf-chip__vendor">HardFOC</span>
</div>

Bus
:   none

Language
:   C++20 (header-only)

[Documentation](https://hardfoc.github.io/hf-pincfg/) · [GitHub](https://github.com/hardfoc/hf-pincfg)
</div>

</div>
<!-- /generated -->

The same list as one table: [All drivers](drivers.md).
