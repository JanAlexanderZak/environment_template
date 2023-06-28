""" Contains constants such as date format, paths, reference dicts, colors, etc.
"""
import datetime as dt

from typing import Callable, Dict, List, Tuple, Union


# **************************************** Constants
ISO_DATE = dt.date.today()
ROUND_DECIMALS: int = 5

# **************************************** Colors
BLACK = "rgba(0,0,0,1)"
WHITE = "rgba(255,255,255,1)"

AXIS_COLOR = BLACK
AXIS_THK = 2
GRID_COLOR = "rgba(127,127,127,0.5)"
GRID_THK = 0.5
LEGEND_BACKGROUND_COLOR = "rgba(255,255,255, 0.8)"
PAPER_BACKGROUND_COLOR = "rgba(255,255,255,1)"
PLOT_HEIGHT = 500
PLOT_WIDTH = 800

PLOTLY_DEFAULT_COLORS_HEX: List[str] = [
    "#1f77b4",  # muted blue
    "#ff7f0e",  # safety orange
    "#2ca02c",  # cooked asparagus green
    "#d62728",  # brick red
    "#9467bd",  # muted purple
    "#8c564b",  # chestnut brown
    "#e377c2",  # raspberry yogurt pink
    "#7f7f7f",  # middle gray
    "#bcbd22",  # curry yellow-green
    "#17becf",  # blue-teal
]

PLOTLY_DEFAULT_COLORS: List[str] = [
    "rgba(31, 119, 180, 1)",
    "rgba(255, 127, 14, 1)",
    "rgba(44, 160, 44, 1)",
    "rgba(214, 39, 40, 1)",
    "rgba(148, 103, 189, 1)",
    "rgba(140, 86, 75, 1)",
    "rgba(227, 119, 194, 1)",
    "rgba(127, 127, 127, 1)",
    "rgba(188, 189, 34, 1)",
    "rgba(23, 190, 207, 1)",
]

PLOTLY_BLUE_SHADES: List[str] = [
    "#72BDF2",
    "#299DF0",
    "#1f77b4",
    "#207BBD",
    "#2E5570",
]

PLOTLY_ORANGE_SHADES: List[str] = [
    "#F29E55",
    "#FF7F0E",
    "#F0760C",
    "#BD5D09",
    "#704621",
]

PLOTLY_GREEN_SHADES: List[str] = [
    "#8AF28A",
    "#41F041",
    "#33BD33",
    "#2CA02C",
    "#397039",
]

PLOTLY_CURRY_SHADES: List[str] = [
    "#F2F274",
    "#F0F02B",
    "#BCBD22",
    "#BDBD22",
    "#70702F",
]

PLANES_3D: List[str] = [
    "rgba(240, 255, 255, 1)",
    "rgba(255, 240, 255, 1)",
    "rgba(255, 255, 240, 1)",
]

PLOTLY_SYMBOLS: List[str] = [
    "circle-open-dot",
    "square-open-dot",
    "star-open-dot",
    "x-open-dot",
    "cross-open-dot",
    "triangle-up-open-dot",
    "diamond-tall-open-dot",
    "triangle-down-open-dot",
]
PLOTLY_DASHES: List[str] = [
    "solid",
    "dash",
    "dot",
    "dashdot",
]
PLOTLY_SYMBOLS_ANNOTATION: List[str] = [""]


# **************************************** Symbols
ALPHA_c: str = "\u0391"
BETA_c: str = "\u0392"
GAMMA_c: str = "\u0393"
DELTA_c: str = "\u0394"
EPSILON_c: str = "\u0395"
ZETA_c: str = "\u0396"
ETA_c: str = "\u0397"
THETA_c: str = "\u0398"
IOTA_c: str = "\u0399"
KAPPA_c: str = "\u039A"
LAMBDA_c: str = "\u039B"
MU_c: str = "\u039C"
NU_c: str = "\u039D"
XI_c: str = "\u039E"
OMICRON_c: str = "\u039F"
PI_c: str = "\u03A0"
RHO_c: str = "\u03A1"
SIGMA_c: str = "\u03A2"
TAU_c: str = "\u03A3"
UPSILON_c: str = "\u03A4"
PHI_c: str = "\u03A5"
CHI_c: str = "\u03A6"
PSI_c: str = "\u03A8"
OMEGA_c: str = "\u03A9"

ALPHA_s: str = "\u03B1"
BETA_s: str = "\u03B2"
GAMMA_s: str = "\u03B3"
DELTA_s: str = "\u03B4"
EPSILON_s: str = "\u03B5"
ZETA_s: str = "\u03B6"
ETA_s: str = "\u03B7"
THETA_s: str = "\u03B8"
IOTA_s: str = "\u03B9"
KAPPA_s: str = "\u03BA"
LAMBDA_s: str = "\u03BB"
MU_s: str = "\u03BC"
NU_s: str = "\u03BD"
XI_s: str = "\u03BE"
OMICRON_s: str = "\u03BF"
PI_s: str = "\u03C0"
RHO_s: str = "\u03C1"
SIGMA_s: str = "\u03C3"
TAU_s: str = "\u03C4"
UPSILON_s: str = "\u03C5"
PHI_s: str = "\u03C6"
CHI_s: str = "\u03C7"
PSI_s: str = "\u03C8"
OMEGA_s: str = "\u03C9"

PLUSMINUS: str = "\u00B1"
TILDE: str = "\u007E"
MINUSTILDE: str = "\u2242"
NOTEQUALTO: str = "\u2260"

# **************************************** Elements
SI_ELEMENTS: Dict[str, str] = {
    "Silicium": "Si",
    "Eisen": "Fe",
    "Kupfer": "Cu",
    "Mangan": "Mn",
    "Magnesium": "Mg",
    "Zink": "Zn",
    "Nickel": "Ni",
    "Chrom": "Cr",
    "Blei": "Pb",
    "Zinn": "Sn",
    "Titan": "Ti",
    "Bismut": "Bi",
    "Natrium": "Na",
    "Phosphor": "P",
    "Antimon": "Sb",
    "Strontium": "Sr",
    "Lithium": "Li",
    "Vanadium": "V",
    "Zirconium": "Zr",
    "Cobalt": "Co",
    "Aluminum": "Al",
}
