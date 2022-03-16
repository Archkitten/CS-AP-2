from src_py.menu import Menu
from src_py.week0.number_swap import NumberSwap
from src_py.week0.matrix_to_text import MatrixToText

# List of options, easily editable. Let's go lazy programming!
number_swap = NumberSwap()
matrix_to_text = MatrixToText()

options_list = [number_swap, matrix_to_text]


class Week0:
    def __init__(self):
        self.name = "Week 0"

    def get_name(self):
        return self.name

    def tester(self):
        print(self.name)
        m = Menu("Week 0 Options:", options_list)
        m.menu()
