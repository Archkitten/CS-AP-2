from src_py.util.menu import Menu
from src_py.util.option import Option
from src_py.week0.number_swap import NumberSwap
from src_py.week0.matrix_format import MatrixFormat

# List of options, easily editable. Let's go lazy programming!
one = NumberSwap()
two = MatrixFormat()

options = [one, two]


class Week0(Option):
    def __init__(self):
        super().__init__()
        self.name = "Week 0"

    def tester(self):
        m = Menu("----- WEEK 0 -----", options)
        m.menu()
