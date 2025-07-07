# -*- coding: utf-8 -*-
# =====================================================================
# --- Package: nostats.viz
# =====================================================================

import os
import sys
from pathlib import Path


# =====================================================================

__all__ = ["VizSettings"]


# =====================================================================

class VizSettings:
    PACKAGE_ROOT = Path(__file__).resolve().parent
    CONFIG_PATH = PACKAGE_ROOT / "config"
    ASSETS_PATH = PACKAGE_ROOT / "assets"


# print(f"{VizSettings.CONFIG_PATH}")
# print(f"{VizSettings.ASSETS_PATH}")
