class Point:
    """Single-point shape"""

    name = ''
    x = 0
    y = 0
    z = 0

    def __init__(self, name: str):
        self.name = name

    def __hash__(self):
        return hash(self.name)


class ComplexShape:
    """A shape that contains multiple points"""

    content = list()
    type = 'undefined'

    def __init__(self, shape_type: str, points: list):
        self.content = points[::]
        self.type = shape_type
