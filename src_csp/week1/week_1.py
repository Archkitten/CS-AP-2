from src_csp.util.menu import Menu
from src_csp.util.option import Option
from src_csp.week1.recursive_a import RecursiveA


class Week1(Option):
    def __init__(self):
        super().__init__()
        self.name = "Week 1"

        one = RecursiveA()
        self.options_list = [one]

    def tester(self):
        print(self.name)
        m = Menu("----- WEEK 1 -----", self.options_list)
        m.menu()
