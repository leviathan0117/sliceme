class Point:
    def __init__(self, x, y, z, name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

    def debug_print(self):
        print("Point \"" + self.name + "\" :", self.x, self.y, self.z)

    def get_type(self):
        return "point"

    def get_name(self):
        return self.name

    def get_response_line(self):
        response_line = "point not implemented"
        return response_line


class Parallelepiped:
    def __init__(self, width, height, length, name):
        self.width = width
        self.height = height
        self.length = length
        self.name = name
        self.points = []

    def process(self, context):
        self.points.append(Point(0, 0, 0, self.name + "_A"))
        self.points.append(Point(self.width, 0, 0, self.name + "_B"))
        self.points.append(Point(self.width, 0, self.length, self.name + "_C"))
        self.points.append(Point(0, 0, self.length, self.name + "_D"))
        self.points.append(Point(0, self.height, 0, self.name + "_A1"))
        self.points.append(Point(self.width, self.height, 0, self.name + "_B1"))
        self.points.append(Point(self.width, self.height, self.length, self.name + "_C1"))
        self.points.append(Point(0, self.height, self.length, self.name + "_D1"))

        for point in self.points:
            context.objects.append(point)

    def debug_print(self):
        print("Parallelepiped \"" + self.name + "\" :", self.width, self.height, self.length, "\n")
        print("    Points array:")
        for j in self.points:
            j.debug_print()

    def get_type(self):
        return "parallelepiped"

    def get_name(self):
        return self.name

    def get_response_line(self):
        response_line = "parallelepiped not implemented"
        return response_line

class Slice:
    def __init__(self):
        self.name = "NO NAME"
        self.points = []

    def get_type(self):
        return "slice"

    def get_name(self):
        return self.name

    def get_response_line(self):
        response_line = "slice not implemented"
        return response_line

class Solver:
    def __init__(self):
        self.objects = []
        self.response = ""

    def solve(self, code):
        command_list = self.split_code(code)

        for command in command_list:
            command_data = self.split_command(command)
            command_type = command_data[0]

            if command_type == "new":
                self.create_new_object(command_data)
            elif command_type == "slice":
                self.slice(command_data)

        # Debug output:
        '''for item in self.objects:
            print("")
            item.debug_print()'''

        self.create_response()
        print("         Response:")
        print(self.response)

        return self.response

    def create_response(self):
        for item in self.objects:
            self.response += item.get_response_line() + "\n"

    def split_code(self, code):
        out = code.split('\n')
        return out

    def split_command(self, command):
        out = command.split(' ')
        return out

    def create_new_object(self, command_data):
        if command_data[1] == "parallelepiped":

            width = 0
            height = 0
            length = 0
            name = "NO NAME"

            # Extract parameters
            for i in range(2, len(command_data)):
                if command_data[i] == "-w":
                    width = int(command_data[i + 1])
                if command_data[i] == "-h":
                    height = int(command_data[i + 1])
                if command_data[i] == "-l":
                    length = int(command_data[i + 1])
                if command_data[i] == "-n":
                    name = command_data[i + 1]

            self.objects.append(Parallelepiped(width, height, length, name))
            self.objects[-1].process(self)
        elif command_data[1] == "point":
            x = 0
            y = 0
            z = 0
            name = "NO NAME"

            # Extract parameters
            for i in range(2, len(command_data)):
                if command_data[i] == "-x":
                    x = int(command_data[i + 1])
                if command_data[i] == "-y":
                    y = int(command_data[i + 1])
                if command_data[i] == "-z":
                    z = int(command_data[i + 1])
                if command_data[i] == "-n":
                    name = command_data[i + 1]

            self.objects.append(Point(x, y, z, name))
        else:
            print("error - unknown object")

    def slice(self, command_data):
        figure_name = command_data[1]
        figure_id = self.find_object_id_by_name(figure_name)
        point1_name = command_data[2]
        point1_id = self.find_object_id_by_name(point1_name)
        point2_name = command_data[3]
        point2_id = self.find_object_id_by_name(point2_name)
        point3_name = command_data[4]
        point3_id = self.find_object_id_by_name(point3_name)

        self.objects.append(Slice())

        print("Created slice of", self.objects[figure_id].get_name(),
              self.objects[point1_id].get_name(),
              self.objects[point2_id].get_name(),
              self.objects[point3_id].get_name(), )

    def find_object_id_by_name(self, object_name):
        for i in range(0, len(self.objects)):
            if self.objects[i].get_name() == object_name:
                return i

        # error
        return 0



