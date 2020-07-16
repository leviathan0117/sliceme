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
    :param list scene: List of objects
    :return: A scene that meet rules
    """

    # todo
    return scene


def compile_rule(command, scene, rules):
    """
    translates command into an equation
    :return: modified scene and rules
    """
    return


def pack_scene(scene):
    """
    :param iterable scene: List of basic components
    :return: List of primitive shapes that can be passes to the client-side renderer
    """

    # todo
    return str(scene)
