def compile(code):
    """
    :param list code: List of rules
    :return: List of primitive shapes to be drawn
    """

    scene = []

    for rule in code:
        scene = apply_rule(scene, rule)

    final_scene = pack_scene(scene)

    return final_scene


def apply_rule(scene, rule):
    """
    :param iterable scene: Scene to work with
    :param list rule: Rule represented as a list of tokens
    :return: Modified scene
    """

    pass


def pack_scene(scene):
    """
    :param iterable scene: List of basic components
    :return: List of primitive shapes that can be passes to the client-side renderer
    """

    pass
