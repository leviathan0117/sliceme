from collections import deque
import compilation_tools as tools


def run(code):
    """
    :param list code: List of rules
    :return: List of primitive shapes to be drawn
    """

    scene = []      # list of basic objects
    rules = []      # list of equations that describe points of the basic objects

    # compile code into equations
    for line in code:
        scene, rules = compile_rule(line, scene, rules)

    compiled_scene = compile_scene(scene, rules)

    final_scene = pack_scene(compiled_scene)

    return final_scene


def compile_scene(scene, rules):
    """
    Solve rules equations
    :param list scene: List of objects
    :return: A scene that meet the rules
    """

    # todo
    return scene


def compile_rule(line, scene, rules):
    """
    translates command into an equation
    :return: modified scene and rules
    """

    command = deque(line)
    if not command:
        return scene, rules

    if command[0] == 'new':
        command.popleft()
        # clear scene
        scene = []
        rules = []
        if not command:
            raise RuntimeError(f"Command '{' '.join(line)}' cannot be parsed")
        is_regular = False
        if command[0] == 'regular':
            command.popleft()
            is_regular = True
        shape_type = command[0]
        command.popleft()
        shape_name = ''
        if command:
            shape_name = command[0]
            command.popleft()
        scene_part, rules_part = tools.build_shape(shape_type, shape_name, is_regular)
        return scene + scene_part, rules + rules_part
    else:
        raise RuntimeError(f"Command '{' '.join(line)}' cannot be parsed")


def pack_scene(scene):
    """
    :param iterable scene: List of basic components
    :return: List of primitive shapes that can be passes to the client-side renderer
    """

    # todo
    return str(scene)
