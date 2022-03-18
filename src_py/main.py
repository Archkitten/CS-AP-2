from src_py.util.menu import Menu
from src_py.week0.week_0 import Week0
from src_py.week1.week_1 import Week1

one = Week0()
two = Week1()

weeks = [one, two]

m = Menu("----- MAIN MENU -----", weeks)
m.menu()
