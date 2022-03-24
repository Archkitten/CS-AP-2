from src_py.util.menu import Menu
from src_py.util.option import Option
from src_py.week2.factorial import Factorial
from src_py.week2.palindrome import Palindrome
from src_py.week2.tri_angle import TriAngle


class Week2(Option):
    def __init__(self):
        super().__init__()
        self.name = "Week 2"

        one = Factorial()
        two = Palindrome()
        three = TriAngle()
        self.options_list = [one, two, three]

    def __call__(self):
        print(self.name)
        m = Menu("----- WEEK 2 -----", self.options_list)
        m.menu()
