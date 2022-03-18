from src_py.util.menu import Menu
from src_py.util.option import Option
from src_py.week0.number_swap import NumberSwap
from src_py.week0.matrix_format import MatrixFormat
from src_py.week0.ship import Ship


class Week0(Option):
    def __init__(self):
        super().__init__()
        self.name = "Week 0"

        one = NumberSwap()
        two = MatrixFormat()
        three = Ship()
        self.options = [one, two, three]

    def tester(self):
        m = Menu("----- WEEK 0 -----", self.options)
        m.menu()
