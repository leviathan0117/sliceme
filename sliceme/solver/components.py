"""
File contains classes that represent basic components of a scene such as point, segment, plane
"""


class Vector3:

    x = 0
    y = 0
    z = 0

    def __init__(self, *args):
        if len(args) == 0:
            pass
        elif len(args) == 1:
            self.x, self.y, self.z = args[0].x, args[0].y, args[0].z
        elif len(args) == 3:
            self.x, self.y, self.z = args[0], args[1], args[2]
        else:
            raise ValueError(f"{type(self).__name__} expected 0, 1 or 3 arguments, got {len(args)}")

        # todo implement addition, subtraction, various products


class Point (Vector3):
    """
    A point in 3d space
    """
    pass


class Straight:
    """
    Straight line in 3d space
    """

    point = Vector3()           # point that lies on the line
    direction = Vector3()       # collinear vector

    def __init__(self, *args):
        if len(args) == 0:
            pass
        elif len(args) == 2:
            self.point = Vector3(args[0])
            self.direction = Vector3(args[1])
        elif len(args) == 6:
            self.point = Vector3(*args[:3])
            self.direction = Vector3(*args[3:])
        else:
            raise ValueError(f"{type(self).__name__} expected 0, 2 or 6 arguments, got {len(args)}")


class Segment:

    points = (Point(), Point())         # ends of the segment
    parent = Straight()                 # straight line that contains the segment

    def __init__(self, *args):
        if len(args) == 0:
            pass
        elif len(args) == 2:
            self.points = (Point(args[0]), Point(args[1]))
        elif len(args) == 4:
            self.points = (Point(args[:2]), Point(args[2:]))
        else:
            raise ValueError(f"{type(self).__name__} expected 0, 2 or 4 arguments, got {len(args)}")
        self.__find_parent()

    def __find_parent(self):
        self.parent = Straight(self.points[0], self.points[1] - self.points[0])

