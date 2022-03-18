from src_py.util.menu import Menu
from src_py.util.option import Option
from src_py.week1.recursive_a import RecursiveA

# List of options, easily editable. Let's go lazy programming!
one = RecursiveA()

options_list = [one]


class Week1:
    def __init__(self):
        self.name = "Week 1"

    def get_name(self):
        return self.name

    def tester(self):
        print(self.name)
        m = Menu("----- WEEK 1 -----", options_list)
        m.menu()
