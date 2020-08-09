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

    def __str__(self):
        return f"{self.name}({self.x}, {self.y}, {self.z})"


class ComplexShape:
    """A shape that contains multiple points"""

    content = list()
    type = 'undefined'

    def __init__(self, shape_type: str, points: list):
        self.content = points[::]
        self.type = shape_type

    def __str__(self):
        return f"{self.type} ({', '.join(map(str, self.content))})"
