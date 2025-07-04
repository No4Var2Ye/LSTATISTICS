# -*- coding: utf-8 -*-
# =====================================================================
# --- File: utils/device-parms.py
# =====================================================================

"""
这是一个用于获取和显示设备参数的脚本。

提供有关设备参数的获取和显示功能。
Author: NoVarYe
Date: 2025-07-03
"""

# =====================================================================

import os
import sys
import platform
import time
import logging
import subprocess
from pathlib import Path
import yaml

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.progress import track
from rich.progress import Progress
from rich import print as rprint
from rich.pretty import pprint

import psutil
import pynvml

from utils.rich_style import load_rich_table_config, create_rich_table

# =====================================================================

EXPORT_SVG = False

# =====================================================================
rich_table_config = load_rich_table_config()

if EXPORT_SVG:
    console = Console(record=True)
else:
    console = Console()


def bytes_to_human_readable(num_bytes):
    units = ["B", "KB", "MB", "GB", "TB"]
    index = 0
    while num_bytes >= 1024 and index < len(units) - 1:
        num_bytes /= 1024
        index += 1
    return f"{num_bytes:.2f} {units[index]}"


# =====================================================================
# --- Get Operating System Information
# =====================================================================
def get_os_info() -> dict[str, str]:
    os_info = {
        "os_name": platform.system(),
        "os_version": platform.version(),
        "os_release": platform.release(),
        "os_architecture": platform.architecture()[0],
        "os_machine": platform.machine(),
        "os_processor": platform.processor(),
    }

    # Get additional information for Linux
    if os_info["os_name"] == "Linux":
        try:
            with open("/etc/os-release", "r") as f:
                for line in f:
                    if "=" in line:
                        key, value = line.strip().split("=", 1)
                        os_info[key] = value.strip('"')
        except (FileNotFoundError, PermissionError, Exception) as e:
            logging.warning(
                f"Failed to read /etc/os-release: {e}. Using default Linux distribution name."
            )
    return os_info


# =====================================================================
# --- Get CPU Information
# =====================================================================
def get_cpu_info() -> dict[str, str]:
    os_name = platform.system()
    cpu_info = {}

    # Get CPU Name
    # Windows
    if os_name == "Windows":
        result = subprocess.check_output(
            ["wmic", "cpu", "get", "Name"], universal_newlines=True
        )
        cpu_info["name"] = result.strip().replace("Name", "").strip()

    # Linux
    elif os_name == "Linux":
        with open("/proc/cpuinfo", "r") as f:
            for line in f:
                if "model name" in line:
                    cpu_info["name"] = line.split(":")[1].strip()
                    break
        cpu_info["name"] = "Unknown Linux Distribution"

    # macOS
    elif os_name == "Darwin":
        result = subprocess.check_output(
            ["sysctl", "-n", "machdep.cpu.brand_string"], universal_newlines=True
        )
        cpu_info["name"] = result.strip()

    # Other OS
    else:
        cpu_info["name"] = "Unknown OS"

    # Pyhysical and Logical Cores
    cpu_info["cores"] = psutil.cpu_count(logical=False)
    cpu_info["threads"] = psutil.cpu_count(logical=True)

    # Current and Max Frequency
    try:
        freq = psutil.cpu_freq()
        cpu_info["current_freq"] = f"{freq.current:.2f} MHz"
        cpu_info["max_freq"] = f"{freq.max:.2f} MHz"
    except Exception:
        cpu_info["current_freq"] = "N/A"
        cpu_info["max_freq"] = "N/A"

    return cpu_info


# =====================================================================
# --- Get Memory Information
# =====================================================================
def get_memory_info() -> dict[str, str]:
    mem = psutil.virtual_memory()

    return {
        "total": bytes_to_human_readable(mem.total),
        "available": bytes_to_human_readable(mem.available),
        "used": bytes_to_human_readable(mem.used),
        "free": bytes_to_human_readable(mem.free),
        "percent": str(mem.percent),
    }


# =====================================================================
# --- Get GPU Information
# =====================================================================
def get_gpu_info():
    try:
        pynvml.nvmlInit()
        device_count = pynvml.nvmlDeviceGetCount()

        gpus = []

        if device_count == 0:
            return {"available": False, "message": "Undetected NVIDIA GPU"}

        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            name = pynvml.nvmlDeviceGetName(handle)
            mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)

            gpus.append(
                {
                    "index": str(i),
                    "name": name,
                    "total": bytes_to_human_readable(mem_info.total),
                    "used": bytes_to_human_readable(mem_info.used),
                    "free": bytes_to_human_readable(mem_info.free),
                }
            )
        return {"available": True, "gpus": gpus}

    except pynvml.NVMLError as e:
        return {"available": False, "message": f"NVML error: {e}"}
    except Exception as e:
        return {"available": False, "message": f"Uknown error {e}"}


# =====================================================================
# --- Display Device Information
# =====================================================================
def display_os_info():
    os_info = get_os_info()

    os_table = create_rich_table(rich_table_config, title="OS Information")

    os_table.add_column("Item", style="cyan", width=24)
    os_table.add_column("Value", width=60)
    os_table.add_row("OS Name", os_info["os_name"])
    os_table.add_row("OS Version", os_info["os_version"])
    os_table.add_row("OS Release", os_info["os_release"])
    os_table.add_row("OS Architecture", os_info["os_architecture"])
    os_table.add_row("OS Machine", os_info["os_machine"])
    os_table.add_row("OS Processor", os_info["os_processor"])

    console.print(os_table)


def display_cpu_info():
    cpu_info = get_cpu_info()

    cpu_table = create_rich_table(rich_table_config, title="CPU Information")

    cpu_table.add_column("Item", style="cyan", width=24)
    cpu_table.add_column("Value", width=60)

    cpu_table.add_row("CPU Name", cpu_info["name"])
    cpu_table.add_row("CPU Pyhysical Cores", str(cpu_info["cores"]))
    cpu_table.add_row("CPU Logical Threads", str(cpu_info["threads"]))
    cpu_table.add_row("CPU Current Frequency", cpu_info["current_freq"])
    cpu_table.add_row("CPU Max Frequency", cpu_info["max_freq"])

    console.print(cpu_table)


def display_memory_info():
    memory_info = get_memory_info()

    memory_table = create_rich_table(rich_table_config, title="Memory Information")

    memory_table.add_column("Item", style="cyan", width=24)
    memory_table.add_column("Value", width=60)

    memory_table.add_row("Total Memory", memory_info["total"])
    memory_table.add_row("Available Memory", memory_info["available"])
    memory_table.add_row("Used Memory", memory_info["used"])
    memory_table.add_row("Free Memory", memory_info["free"])
    memory_table.add_row("Memory Usage Percentage", f"{memory_info['percent']}%")

    console.print(memory_table)


def display_gpu_info():
    gpu_info = get_gpu_info()

    gpu_table = create_rich_table(rich_table_config, title="GPU Information")

    gpu_table.add_column("ID", style="cyan", width=10)
    gpu_table.add_column("GPU Model", width=40)
    gpu_table.add_column("Total VRAM", justify="right", width=10)
    gpu_table.add_column("Used VRAM", justify="right", width=10)
    gpu_table.add_column("Free VRAM", justify="right", width=10)

    if gpu_info["available"]:
        for gpu in gpu_info["gpus"]:
            gpu_table.add_row(
                gpu["index"], gpu["name"], gpu["total"], gpu["used"], gpu["free"]
            )
    else:
        gpu_table.add_row("", gpu_info["message"], "", "", "")

    console.print(gpu_table)


def display_device_info():
    display_os_info()
    display_cpu_info()
    display_memory_info()
    display_gpu_info()

    if EXPORT_SVG:
        svg_content = console.export_svg()

        with open("device-params.svg", "w", encoding="utf-8") as f:
            f.write(svg_content)


def main():
    display_device_info()


if __name__ == "__main__":
    main()
