from src_csp.util.menu import Menu
from src_csp.week0.week_0 import Week0
from src_csp.week1.week_1 import Week1

one = Week0()
two = Week1()

weeks = [one, two]

m = Menu("----- MAIN MENU -----", weeks)
m.menu()
