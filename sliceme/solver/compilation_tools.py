import scene_components as components
import re

DEFAULT_SHAPE_NAMES = {
    'cube': 'ABCDA1B1C1D1'
}


def build_shape(shape_type, shape_name, is_regular):
    if not shape_name:
        shape_name = DEFAULT_SHAPE_NAMES[shape_type]
    vertexes = re.findall(r'[A-Z][0-9]*', shape_name)

    if shape_type == 'cube':
        scene = [
            components.Polygon(vertexes[0], vertexes[1], vertexes[2], vertexes[3]),
            components.Polygon(vertexes[0], vertexes[1], vertexes[4], vertexes[5]),
            components.Polygon(vertexes[1], vertexes[2], vertexes[5], vertexes[6]),
            components.Polygon(vertexes[2], vertexes[3], vertexes[6], vertexes[7]),
            components.Polygon(vertexes[3], vertexes[0], vertexes[7], vertexes[4]),
            components.Polygon(vertexes[4], vertexes[5], vertexes[6], vertexes[7])
        ]
        rules = [
            describe_perpendicular(vertexes[0], vertexes[1], vertexes[0], vertexes[3]),
            describe_perpendicular(vertexes[0], vertexes[1], vertexes[1], vertexes[2]),
            describe_perpendicular(vertexes[1], vertexes[2], vertexes[2], vertexes[3]),
            describe_perpendicular(vertexes[0], vertexes[1], vertexes[0], vertexes[4]),
            describe_perpendicular(vertexes[0], vertexes[3], vertexes[0], vertexes[4]),
            describe_parallel(vertexes[0], vertexes[4], vertexes[1], vertexes[5]),
            describe_parallel(vertexes[0], vertexes[4], vertexes[2], vertexes[6]),
            describe_parallel(vertexes[0], vertexes[4], vertexes[3], vertexes[7]),
            describe_parallel(vertexes[0], vertexes[1], vertexes[4], vertexes[5]),
            describe_parallel(vertexes[1], vertexes[2], vertexes[5], vertexes[6]),
            describe_parallel(vertexes[2], vertexes[3], vertexes[6], vertexes[7]),
            describe_parallel(vertexes[3], vertexes[0], vertexes[7], vertexes[4]),
            equate(describe_segment_length(vertexes[0], vertexes[1]),
                   describe_segment_length(vertexes[0], vertexes[4])),
            equate(describe_segment_length(vertexes[0], vertexes[1]),
                   describe_segment_length(vertexes[0], vertexes[3]))
        ]


def describe_angle(a, b, c, d):
    """
    :return: expression of angle between AB and CD
    """
    # todo
    return ''


def describe_segment_length(a, b):
    """
    :return: expression of distance between A and B
    """
    # todo
    return ''


def describe_perpendicular(a, b, c, d):
    """
    :return: equation of AB and CD being perpendicular
    """
    # todo
    return ''


def describe_parallel(a, b, c, d):
    """
    :return: equation of AB and CD being parallel
    """
    # todo
    return ''


def equate(a, b):
    return str(a) + ' = ' + str(b)
