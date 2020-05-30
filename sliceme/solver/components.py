'''
File contains classes that represent basic components of a scene such as point, segment, plane
'''


class Point:

    x = 0
    y = 0
    z = 0

    def __init__(self, *args):
        if len(args) == 0:
            pass
        if len(args) == 3:
            self.x, self.y, self.z = args[0], args[1], args[2]
        else:
            raise ValueError(f"Point expected 0 or 3 arguments, got {len(args)}")
