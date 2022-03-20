from src_py.util.option import Option
import math


class TriAngle(Option):
    def __init__(self):
        super().__init__()
        self.name = "Tri Angle"

    def tester(self):
        target_x = int(input("Target x value? "))
        target_y = int(input("Target y value? "))
        a = Angles(0, 0, target_x, target_y)
        a.print_coordinates()


class Angles:
    def __init__(self, x, y, tx, ty):
        self.x = x
        self.y = y
        angle = math.atan2(ty - y, tx - x)
        self.tx = math.cos(angle)
        self.ty = math.sin(angle)

    def print_coordinates(self):
        print("X Rotation: " + str(self.tx))
        print("Y Rotation: " + str(self.ty))
