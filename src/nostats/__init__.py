# -*- coding: utf-8 -*-
# =====================================================================
# --- Package: nostats
# =====================================================================

import importlib
import logging

# =====================================================================

__version__ = "1.0.0"
__all__ = []

# =====================================================================

logging.basicConfig(level=logging.INFO)

# =====================================================================

logger = logging.getLogger(__name__)

logger.info("Package NoStats initialized.")

# 懒加载
# class LazyLoader:
#     def __init__(self, module_name):
#         self._module_name = module_name
#         self._module = None
#     def __getattr__(self, name):
#         if self._module is None:
#             self._module = importlib.import_module(self._module_name)
#         return getattr(self._module, name)
# subpackage1 = LazyLoader("mypackage.subpackage1")
# subpackage2 = LazyLoader("mypackage.subpackage2")
# __all__ = ["subpackage1", "subpackage2"]
