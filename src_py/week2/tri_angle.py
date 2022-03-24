from src_py.util.option import Option
import math


class TriAngle(Option):
    def __init__(self):
        super().__init__()
        self.name = "Tri Angle"

    def __call__(self):
        # target_x = int(input("Target x value? "))
        # target_y = int(input("Target y value? "))
        # a = Angles(0, 0, target_x, target_y)
        # a.print_coordinates()
        print("\nParticle starts at (0, 0) and goes to (5, 5):")
        a = Angles(0, 0, 5, 5)
        a.print_coordinates()

        print("\nParticle starts at (0, 0) and goes to (-3, -3):")
        b = Angles(0, 0, -3, -3)
        b.print_coordinates()

        print("\nParticle starts at (5.5, 8) and goes to (-6.23, 11.1):")
        c = Angles(5.5, 8, -6.23, 11.1)
        c.print_coordinates()


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
