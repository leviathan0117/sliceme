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


class Plane:

    normal = Vector3()
    dist = 0                # distance from (0; 0; 0) to the plane
    content = set()         # basic components that lie on the plane

    def __init__(self, *args):
        if len(args) == 0:
            pass
        elif len(args) == 2:
            if type(args[1]) == int:
                # Plane(normal : Vector3, dist : float)
                self.normal = args[0]
                self.dist = args[1]
            else:
                # Plane(normal : Vector3, point : Point)
                self.normal = args[0]
                self.dist = self.__calculate_dist_by_point(self.normal, args[1])
        elif len(args) == 4:
            # Plane(A : float, B : float, C : float, D : float)
            self.normal = Vector3(*args[:3])
            self.dist = args[3]
        elif len(args) == 6:
            # Plane(A : float, B : float, C : float, Px : float, Py : float, Pz : float)
            self.normal = Vector3(*args[:3])
            self.dist = self.__calculate_dist_by_point(self.normal, Point(*args[3:]))
        else:
            raise ValueError(f"{type(self).__name__} expected 0, 1, 2, 4 or 6 arguments, got {len(args)}")

    def __calculate_dist_by_point(self, normal, point):
        # todo
        pass

    def add_content(self, item):
        self.content.add(item)


class Polygon:

    vertexes = []
    parent_plane = Plane()

    def __init__(self, plane, *points):
        # Polygon(plane : Plane, Point, Point, Point, ...)
        if type(plane) != Plane:
            raise ValueError(f"First parameter for Polygon must be Plane, got {type(plane).__name__}")
        if len(points) < 3:
            raise ValueError(f"At least 3 vertexes are required for Polygon, got {len(points)}")
        for item in points:
            if type(item) != Point:
                raise ValueError(f"Polygon expected Point, got {type(item).__name__}")
        self.parent_plane = plane
        plane.add_content(self)
        self.vertexes = points[::]