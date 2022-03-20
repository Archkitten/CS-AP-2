from src_py.util.menu import Menu
from src_py.util.option import Option
from src_py.week2.factorial import Factorial
from src_py.week2.palindrome import Palindrome


class Week2(Option):
    def __init__(self):
        super().__init__()
        self.name = "Week 2"

        one = Factorial()
        two = Palindrome()
        self.options_list = [one, two]

    def tester(self):
        print(self.name)
        m = Menu("----- WEEK 2 -----", self.options_list)
        m.menu()
