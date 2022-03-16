from src_py.menu import Menu
from src_py.week1.recursive_a import RecursiveA

# List of options, easily editable. Let's go lazy programming!
recursive_a = RecursiveA()

options_list = [recursive_a]


class Week1:
    def __init__(self):
        self.name = "Week 1"

    def get_name(self):
        return self.name

    def process(self):
        print(self.name)
        m = Menu("Week 1 Options:", options_list)
        m.menu()
