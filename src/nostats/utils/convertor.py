import os

from cairosvg import svg2png

if os.path.exists("example_table.svg"):

    with open("example_table.svg", "r", encoding="utf-8") as svg_file:
        svg_data = svg_file.read()

    svg2png(bytestring=svg_data, write_to="example_table.png")
