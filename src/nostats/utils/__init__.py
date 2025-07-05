# -*- coding: utf-8 -*-
# =====================================================================
# --- Package: nostats.utils
# =====================================================================

import os
import sys
from pathlib import Path

from nostats.utils.rich_style import load_rich_table_config, create_rich_table
from nostats.utils import convertor
from nostats.utils.device_parms import display_device_info

# =====================================================================

__all__ = [
    "load_rich_table_config",
    "create_rich_table",
    "convertor",
    "display_device_info",
]


# =====================================================================

class Settings:
    PACKAGE_ROOT = Path(__file__).resolve().parent
    CONFIG_PATH = PACKAGE_ROOT.parent


# print(f"Package root directory: {Settings.PACKAGE_ROOT}")
# print(f"Config directory: {Settings.CONFIG_PATH}")
