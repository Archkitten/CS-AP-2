from src_py.util.menu import Menu
from src_py.util.option import Option
from src_py.week1.recursive_a import RecursiveA
from src_py.week1.info_loops import InfoLoops
from src_py.week1.fibonacci import Fibonacci


class Week1(Option):
    def __init__(self):
        super().__init__()
        self.name = "Week 1"

        one = RecursiveA()
        two = InfoLoops()
        three = Fibonacci()
        self.options_list = [one, two, three]

    def __call__(self):
        print(self.name)
        m = Menu("----- WEEK 1 -----", self.options_list)
        m.menu()
