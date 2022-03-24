from src_py.util.menu import Menu
from src_py.pattern_menus.animations import Animations
from src_py.pattern_menus.data_structures import DataStructures
from src_py.pattern_menus.math_algorithms import MathAlgorithms


class MainPattern:
    def __init__(self):
        super().__init__()
        self.name = "Main Menu P"

        one = Animations()
        two = DataStructures()
        three = MathAlgorithms()
        self.options = [one, two, three]

    def main(self):
        m = Menu("----- MAIN MENU P -----", self.options)
        m.menu()
