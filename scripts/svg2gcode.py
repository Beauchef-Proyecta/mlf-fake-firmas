from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode.compiler import Compiler, interfaces
from gcodeParam import *

def svg2gcode(path):
    gcode_compiler = Compiler(interfaces.Gcode, movement_speed=1000, cutting_speed=300, pass_depth=5)
    curves = parse_file(path) # Parse an svg file into geometric curves

    nombre = 'test.gcode'
    gcode_compiler.append_curves(curves) 
    gcode_compiler.compile_to_file(nombre, passes=2)

    test = svgParam(gcode = nombre, home = (0,0,100))
    test.parametrizadorInador()


