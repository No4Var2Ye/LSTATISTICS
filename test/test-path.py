
import os
import sys
from pathlib import Path

print("Current working directory:", os.getcwd())

current_file = __file__
# 为什么也获得了绝对路径
print("Current file:", current_file)

print("Absolute path of the script:", os.path.abspath(__file__))
file_name = os.path.basename(current_file)
print("Filefg name:", file_name)

current_dir = os.path.dirname(os.path.abspath(current_file))
print("Current directory:", current_dir)

os.path.join(current_dir, "test-path.py")

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
print("Project root directory:", project_root)


current_file2 = Path(__file__).resolve()
print("Current file (Path):", current_file2)
current_dir2 = current_file2.parent
print("Current directory (Path):", current_dir2)
project_root2 = current_file2.parents[1]
if project_root2 not in sys.path:
    sys.path.insert(0, str(project_root2))
print("Project root directory (Path):", project_root2)

config_path2 = project_root2 / "config" / "settings.json"
print(config_path2)
