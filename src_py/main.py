from menu import Menu
from src_py.week0.week_0 import Week0
from src_py.week1.week_1 import Week1

# List of options, easily editable. Let's go lazy programming!
week_0 = Week0()
week_1 = Week1()

week_list = [week_1, week_0]

# Run menu().
m = Menu("MAIN MENU", week_list)
m.menu()
