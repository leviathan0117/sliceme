from collections import deque
from scene_objects import Point, ComplexShape
from solver_utilities import solve_system


def preprocess_code(code: str) -> deque:
    """Prepares code for the next steps"""

    cmd_list = code.split('\n')
    return deque(cmd_list)


def interpret_code(code: deque) -> (list, list, list):
    """Translates given code into a scene, described with a system of equations"""

    return [], [], []


def solve(scene_description: list, variables: list, equations: list) -> list:
    """Finds a scene that satisfies given requirements"""

    solution = solve_system(equations, variables)

    for item in scene_description:
        if item is Point:
            item.x = solution[item.name + 'x']
            item.y = solution[item.name + 'y']
            item.z = solution[item.name + 'z']
        elif item is ComplexShape:
            for point in item.content:
                point.x = solution[point.name + 'x']
                point.y = solution[point.name + 'y']
                point.z = solution[point.name + 'z']

    return scene_description


def pack_scene(scene: list) -> list:
    """Translates given scene so it can be read by renderer"""

    packed_scene = []
    for item in scene:
        component = {}
        if item is Point:
            component['type'] = 'point'
            component['position'] = [
                item.x,
                item.y,
                item.z
            ]
        elif item is ComplexShape:
            component['type'] = item.type
            component['content'] = []
            for point in item.content:
                component['content'].append([
                    point.x,
                    point.y,
                    point.z
                ])
        packed_scene.append(component)

    return packed_scene


def process(raw_code: str) -> list:
    """Builds scene from given code"""

    code = preprocess_code(raw_code)

    scene_description, variables, equations = interpret_code(code)

    scene = solve(scene_description, variables, equations)

    packed_scene = pack_scene(scene)

    return packed_scene
