from collections import deque


def preprocess_code(code: str) -> deque:
    """Prepares code for the next steps"""

    cmd_list = code.split('\n')
    return deque(cmd_list)


def interpret_code(code: deque) -> (list, list, list):
    """Translates given code into a scene, described with a system of equations"""

    pass


def solve(scene_description: list, variables: list, equations: list) -> list:
    """Finds a scene that satisfies given requirements"""

    pass


def pack_scene(scene: list) -> list:
    """Translates given scene so it can be read by renderer"""

    pass


def process(raw_code: str) -> list:
    """Builds scene from given code"""

    code = preprocess_code()

    scene_description, variables, equations = interpret_code(code)

    scene = solve(scene_description, variables, equations)

    packed_scene = pack_scene(scene)

    return packed_scene
