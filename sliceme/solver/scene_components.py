class Point:
    def __init__(self, name):
        self.name = name


class Polygon:
    def __init__(self, *points):
        self.points = points


class Segment:
    def __init__(self, a, b):
        self.points = (a, b)