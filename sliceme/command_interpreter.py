from collections import deque
from scene_objects import Point, ComplexShape
import re
from sympy.core.symbol import symbols
import describe as desc


def build_shape(shape_type: str, shape_name: str, is_regular: bool) -> (list, list, list):
    """Describes a required shape with equations"""

    vertexes = re.findall(r'[A-Z][0-9]*', shape_name)
    var = {vertex: list(symbols(vertex + '(x:z)')) for vertex in vertexes}
    variables = [variable for item in var.values() for variable in item]
    scene = []
    rules = []

    if shape_type == 'cube':
        scene = [
            ComplexShape('polygon', [vertexes[0], vertexes[1], vertexes[2], vertexes[3]]),
            ComplexShape('polygon', [vertexes[0], vertexes[1], vertexes[4], vertexes[5]]),
            ComplexShape('polygon', [vertexes[1], vertexes[2], vertexes[5], vertexes[6]]),
            ComplexShape('polygon', [vertexes[2], vertexes[3], vertexes[6], vertexes[7]]),
            ComplexShape('polygon', [vertexes[3], vertexes[0], vertexes[7], vertexes[4]]),
            ComplexShape('polygon', [vertexes[4], vertexes[5], vertexes[6], vertexes[7]])
        ]
        rules = [
            desc.perpendicular(vertexes[0], vertexes[1], vertexes[0], vertexes[3], var),
            desc.perpendicular(vertexes[0], vertexes[1], vertexes[1], vertexes[2], var),
            desc.perpendicular(vertexes[1], vertexes[2], vertexes[2], vertexes[3], var),
            desc.perpendicular(vertexes[0], vertexes[1], vertexes[0], vertexes[4], var),
            desc.perpendicular(vertexes[0], vertexes[3], vertexes[0], vertexes[4], var),
            desc.parallel(vertexes[0], vertexes[4], vertexes[1], vertexes[5], var),
            desc.parallel(vertexes[0], vertexes[4], vertexes[2], vertexes[6], var),
            desc.parallel(vertexes[0], vertexes[4], vertexes[3], vertexes[7], var),
            desc.parallel(vertexes[0], vertexes[1], vertexes[4], vertexes[5], var),
            desc.parallel(vertexes[1], vertexes[2], vertexes[5], vertexes[6], var),
            desc.parallel(vertexes[2], vertexes[3], vertexes[6], vertexes[7], var),
            desc.parallel(vertexes[3], vertexes[0], vertexes[7], vertexes[4], var),
            desc.equate(desc.point_distance(vertexes[0], vertexes[1], var),
                        desc.point_distance(vertexes[0], vertexes[4], var)),
            desc.equate(desc.point_distance(vertexes[0], vertexes[1], var),
                        desc.point_distance(vertexes[0], vertexes[3], var))
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
