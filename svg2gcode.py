import os
from svg2g3d import generate_gcode

with open("template.svg") as f:
    s = f.read()
    gc = generate_gcode(s)
    print(gc)
