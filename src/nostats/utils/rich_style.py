# -*- coding: utf-8 -*-
# =====================================================================
# --- File: utils/rich_style.py
# =====================================================================

import yaml
from pathlib import Path

from rich import box
from rich.table import Table
from rich.console import Console

# =====================================================================

# 相对路径写法
# 获取当前py脚本的路径。使配置文件总是相对于当前脚本
CURRENT_DIR = Path(__file__).parent


# =====================================================================
def load_rich_table_config(config_path: str = "config/rich_style_config.yaml") -> dict:
    full_path = (CURRENT_DIR / config_path).resolve()

    with open(full_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    table_config = config.get("rich_table", {})

    if "box" in table_config:
        box_name = table_config["box"]
        table_config["box"] = getattr(box, box_name, box.SQUARE)

    return table_config


def create_rich_table(config: dict, title: str | None = None) -> Table:
    table_title = title if title is not None else config.get("title", "Untitled Table")
    show_header = config.get("show_header", True)
    header_style = config.get("header_style", "bold magenta")
    show_lines = config.get("show_lines", False)
    table_box = config.get("box", box.SQUARE)
    border_style = config.get("border_style", "cyan")
    row_styles = config.get("row_styles", ["", ""])

    table = Table(
        title=table_title,
        show_header=show_header,
        header_style=header_style,
        show_lines=show_lines,
        box=table_box,
        border_style=border_style,
        row_styles=row_styles,
    )

    return table


def main():
    console = Console()

    table_config = load_rich_table_config()
    table = create_rich_table(table_config)

    table.add_column(header="Test Header1")
    table.add_column(header="Test Header2")

    table.add_row("test data11", "test data12")
    table.add_row("test data21", "test data22")

    console.print(table)


if __name__ == "__main__":
    main()
