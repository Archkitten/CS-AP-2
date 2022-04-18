from util import *
from main_menu import MainMenu
from world import World

# Load Data
Config.load_data()

# Main Menu
main = MainMenu()
main()

world = World()
world()

# Save Data
Config.save_data()

# Exit
pygame.quit()
sys.exit()