import time
from src_py.util.option import Option
# from ..util.option import Option


ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"


class Ship(Option):
    def __init__(self):
        super().__init__()
        self.name = "Ship Animation"

    def tester(self):
        self.ship()

    def ocean_print(self):
        # print ocean
        # print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)

        print("\n"*4)
        print(OCEAN_COLOR + "  " * 35)

    # print ship with colors and leading spaces
    def ship_print(self, position):
        print(ANSI_HOME_CURSOR)
        print(RESET_COLOR)
        sp = " " * position
        print(sp + "/|")
        print(sp + "||")
        print(sp + "\|  ᓚᘏᗢ  ")
        print(SHIP_COLOR, end="")
        print(sp + "  \______/  ")
        print(RESET_COLOR)

    # ship function, iterate into this file
    def ship(self):
        # only need to print ocean once
        self.ocean_print()

        # loop control variables
        start = 0  # start at zero
        distance = 60  # how many times to repeat
        step = 2  # count by 2

        # loop purpose is to animate ship sailing
        for position in range(start, distance, step):
            self.ship_print(position)  # call to function with parameter
            time.sleep(.1)
