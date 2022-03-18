from src_py.util.menu import Menu
from src_py.util.option import Option
from src_py.week0.number_swap import NumberSwap
from src_py.week0.matrix_format import MatrixFormat
from src_py.week0.build_stairs import BuildStairs
from src_py.week0.cat_laptop import CatLaptop


class Week0(Option):
    def __init__(self):
        super().__init__()
        self.name = "Week 0"

        one = NumberSwap()
        two = MatrixFormat()
        three = BuildStairs()
        four = CatLaptop()
        self.options = [one, two, three, four]

    def tester(self):
        m = Menu("----- WEEK 0 -----", self.options)
        m.menu()
