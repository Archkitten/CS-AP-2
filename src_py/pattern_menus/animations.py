from src_py.util.menu import Menu
from src_py.util.option import Option
from src_py.week0.matrix_format import MatrixFormat
from src_py.week0.build_stairs import BuildStairs
from src_py.week0.cat_laptop import CatLaptop
import os


class Animations(Option):
    def __init__(self):
        super().__init__()
        self.name = "Animations"
        self.options = [MatrixFormat(), BuildStairs(), CatLaptop()]

    def __call__(self):
        m = Menu("----- Animations -----", self.options)
        m.menu()
