import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import Settings

print(f"Config directory: {Settings.CONFIG_PATH}")
