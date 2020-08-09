from collections import deque
from scene_objects import Point, ComplexShape
from solver_utilities import solve_system
from command_interpreter import interpret_command


def preprocess_code(code: str) -> list:
    """Prepares code for the next steps
    @return: list of deque
    """

    cmd_list = list(code.split('\n'))
    for i, item in enumerate(cmd_list):
        cmd_list[i] = deque(item.split())
    return cmd_list


def interpret_code(code: list) -> (list, list, list):
    """Translates given code into a scene, described with a system of equations
    @return: (scene, variables, equations)
    """

    scene, variables, equations = [], [], []

    for command in code:
        scene, variables, equations = interpret_command(command, scene, variables, equations)

    return scene, variables, equations


def solve(scene_description: list, variables: list, equations: list) -> list:
    """Finds a scene that satisfies given requirements"""

    solution = solve_system(equations, variables)

    for item in scene_description:
        if isinstance(item, Point):
            item.x = solution[item.name + 'x']
            item.y = solution[item.name + 'y']
            item.z = solution[item.name + 'z']
        elif isinstance(item, ComplexShape):
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
        if isinstance(item, Point):
            component['type'] = 'point'
            component['position'] = [
                item.x,
                item.y,
                item.z
            ]
        elif isinstance(item, ComplexShape):
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
