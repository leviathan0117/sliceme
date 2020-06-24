import rules


def run(code):
    """
    :param list code: List of rules
    :return: List of primitive shapes to be drawn
    """

    scene = []

    for rule in code:
        scene = apply_rule(scene, rule)

    scene = compile_scene(scene)

    scene = deconstruct_scene(scene)

    final_scene = pack_scene(scene)

    return final_scene


def apply_rule(scene, rule):
    """
    :param iterable scene: List of objects
    :param list rule: Rule represented as a list of tokens
    :return: Modified scene
    """

    if rule[0] == 'new':
        if len(rule) == 2:
            scene = rules.new(scene, 'cube', rule[1])
        elif len(rule) == 3:
            scene = rules.new(scene, rule[1], rule[2])
    else:
        raise ValueError(f"Parsing error on rule {' '.join(rule)}")

    return scene


def compile_scene(scene):
    """
    Fill in every necessary parameter of objects in the scene
    :param list scene: List of objects
    :return: Modified scene
    """

    # todo
    return scene


def deconstruct_scene(scene):
    """
    Turns every object in the scene into a primitive
    :param list scene:
    :return: List of primitives
    """

    # todo
    return scene


def pack_scene(scene):
    """
    :param iterable scene: List of basic components
    :return: List of primitive shapes that can be passes to the client-side renderer
    """

    # todo
    return str(scene)
