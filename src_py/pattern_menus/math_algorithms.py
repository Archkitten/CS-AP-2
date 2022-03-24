from src_py.util.menu import Menu
from src_py.util.option import Option
from src_py.week0.number_swap import NumberSwap
from src_py.week1.fibonacci import Fibonacci
from src_py.week2.factorial import Factorial
from src_py.week2.tri_angle import TriAngle


class MathAlgorithms(Option):
    def __init__(self):
        super().__init__()
        self.name = "Math Algorithms"

        self.options = [NumberSwap(), Fibonacci(), Factorial(), TriAngle()]

    def __call__(self):
        m = Menu("----- Math Algorithms -----", self.options)
        m.menu()
