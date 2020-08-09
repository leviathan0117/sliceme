from collections import deque
from scene_objects import Point, ComplexShape
import re
from sympy.core.symbol import symbols
import describe as desc


def build_shape(shape_type: str, shape_name: str, is_regular: bool) -> (list, list, list):
    """Describes a required shape with equations"""

    vertexes = re.findall(r'[A-Z][0-9]*', shape_name)                           # list of symbol names
    var = {vertex: list(symbols(vertex + '(x:z)')) for vertex in vertexes}      # maps names to symbols
    variables = [variable for item in var.values() for variable in item]        # list of all symbols
    scene = []
    rules = []

    if shape_type == 'cube':
        scene = [
            ComplexShape('polygon', [Point(vertexes[0]), Point(vertexes[1]), Point(vertexes[2]), Point(vertexes[3])]),
            ComplexShape('polygon', [Point(vertexes[0]), Point(vertexes[1]), Point(vertexes[4]), Point(vertexes[5])]),
            ComplexShape('polygon', [Point(vertexes[1]), Point(vertexes[2]), Point(vertexes[5]), Point(vertexes[6])]),
            ComplexShape('polygon', [Point(vertexes[2]), Point(vertexes[3]), Point(vertexes[6]), Point(vertexes[7])]),
            ComplexShape('polygon', [Point(vertexes[3]), Point(vertexes[0]), Point(vertexes[7]), Point(vertexes[4])]),
            ComplexShape('polygon', [Point(vertexes[4]), Point(vertexes[5]), Point(vertexes[6]), Point(vertexes[7])])
        ]
        rules = [
            var[vertexes[0]][0],
            var[vertexes[0]][1],
            var[vertexes[0]][2],
            var[vertexes[1]][2],
            var[vertexes[2]][2],
            var[vertexes[3]][2],
            var[vertexes[1]][0],
            var[vertexes[3]][1],
            var[vertexes[5]][0],
            var[vertexes[7]][1],
            var[vertexes[4]][0],
            var[vertexes[4]][1],
            var[vertexes[6]][0] - var[vertexes[3]][0],
            var[vertexes[6]][1] - var[vertexes[1]][1],
            var[vertexes[5]][1] - var[vertexes[1]][1],
            var[vertexes[7]][0] - var[vertexes[3]][0],
            var[vertexes[3]][0] - var[vertexes[1]][1],
            var[vertexes[2]][1] - var[vertexes[1]][1],
            var[vertexes[2]][0] - var[vertexes[3]][0],
            var[vertexes[4]][2] - var[vertexes[1]][1],
            var[vertexes[5]][2] - var[vertexes[4]][2],
            var[vertexes[6]][2] - var[vertexes[4]][2],
            var[vertexes[7]][2] - var[vertexes[4]][2]
        ]

    return scene, variables, rules


def interpret_command(cmd: deque, scene: list, variables: list, equations: list) -> (list, list, list):
    """Translates a single command into equation format"""

    if not cmd:
        return scene, variables, equations
    if cmd[0] == 'new':
        cmd.popleft()
        is_regular = False
        if cmd[0] == 'regular':
            cmd.popleft()
            is_regular = True
        shape_type = cmd[0]
        cmd.popleft()
        shape_name = cmd[0]
        cmd.popleft()
        add_scene, add_vars, add_equations = build_shape(shape_type, shape_name, is_regular)
        return scene + add_scene, variables + add_vars, equations + add_equations
    else:
        return scene, variables, equations
