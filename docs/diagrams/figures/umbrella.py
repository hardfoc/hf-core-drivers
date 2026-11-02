"""Where hf-core-drivers sits: between hf-core above and the chips below, with the platform layer beside the drivers.

Reads: From top to bottom. Board HALs and products build on hf-core, whose handlers adapt each driver to the
platform. hf-core-drivers holds the device drivers under external/ (one per repository, names read from .gitmodules)
and the platform layer under internal/. The drivers talk to the chips through interfaces that the platform layer
implements for the MCU.
"""

import configparser
from pathlib import Path

from hardfoc_mkdocs_theme.figkit import Fig

ROOT = Path(__file__).resolve().parents[3]


def data():
    gm = configparser.ConfigParser()
    gm.read(ROOT / ".gitmodules")
    paths = [gm[s]["path"] for s in gm.sections()]
    short = lambda p: p.split("/", 1)[1].removeprefix("hf-").removesuffix("-driver")
    return {
        "external": sorted(short(p) for p in paths if p.startswith("external/")),
        "internal": sorted(p.split("/", 1)[1] for p in paths if p.startswith("internal/")),
        "sources": [".gitmodules:submodule paths"],
    }


def build(d):
    f = Fig(
        "umbrella",
        "One umbrella, one submodule per chip",
        alt="Layer diagram: board HALs and products build on hf-core, whose handlers use the device drivers in "
        "hf-core-drivers/external and the platform layer in hf-core-drivers/internal, which drive the chips.",
        width=1200,
        kicker="Architecture",
        subtitle=f"{len(d['external'])} device drivers and {len(d['internal'])} platform repositories, pinned "
        "together and built by hf-core.",
        profile="overview",
        legend=[("brand", "this repository"), ("teal", "built on it"), ("slate", "hardware")],
    )
    W = f.body_w
    hal = f.card(0, 0, W, "Board HALs and products", ["hf-hal-vortex-v1, hf-hal-flux-v1, firmware"], tone="teal")
    core = f.card(0, hal.b + 40, W, "hf-core", ["handlers adapt each driver to the platform; HF_CORE_ENABLE_* picks"
                                                " the drivers"], tone="teal", accent=True)
    top = core.b + 40
    chips_h = f.chips(16, f.region_inner_top(top), W - 32, d["external"], tone="brand")
    ext = f.region(0, top, W, f.region_inner_top(top) - top + chips_h + 18, "external/: device drivers",
                   tone="brand", sub="hardware-agnostic, one repository each")
    top2 = ext.b + 24
    chips2_h = f.chips(16, f.region_inner_top(top2), W - 32, d["internal"], tone="brand", )
    intl = f.region(0, top2, W, f.region_inner_top(top2) - top2 + chips2_h + 18, "internal/: platform layer",
                    tone="brand", sub="MCU interfaces and board pin maps")
    hw = f.card(0, intl.b + 40, W, "Chips and the MCU", ["SPI, I²C, UART, CAN, ADC, RMT"], tone="slate")
    for a, b in ((hal, core), (core, ext), (intl, hw)):
        f.connect(a, b, "bottom", "top", tone="rail")
    return f
