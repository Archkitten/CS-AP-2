from src_py.util.menu import Menu
from src_py.util.option import Option
from src_py.week1.info_loops import InfoLoops
from src_py.week2.palindrome import Palindrome


class DataStructures(Option):
    def __init__(self):
        super().__init__()
        self.name = "Data Structures"

        self.options = [InfoLoops(), Palindrome()]

    def __call__(self):
        m = Menu("----- Data Structures -----", self.options)
        m.menu()
