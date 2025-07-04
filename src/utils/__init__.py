# -*- coding: utf-8 -*-
# =====================================================================
# --- Module: utils
# =====================================================================

import os
import sys
from pathlib import Path
import logging

from utils.rich_style import load_rich_table_config, create_rich_table
import utils.convertor as convertor
from utils.device_parms import display_device_info

# =====================================================================

__version__ = "1.0.0"

logging.basicConfig(level=logging.INFO)

# =====================================================================

logger = logging.getLogger(__name__)

logger.info("Package initialized.")


class Settings:
    PACKAGE_ROOT = Path(__file__).resolve().parent
    CONFIG_PATH = PACKAGE_ROOT.parent


# print(f"Package root directory: {Settings.PACKAGE_ROOT}")
# print(f"Config directory: {Settings.CONFIG_PATH}")


__all__ = ["load_rich_table_config", "create_rich_table", "convertor", "display_device_info"]
