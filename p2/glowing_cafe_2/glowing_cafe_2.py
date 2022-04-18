from util import *
from intro_menu import IntroMenu
from main_menu import MainMenu

# Load Data
Config.load_data()

# Intro
intro = IntroMenu()
intro()

# Main Menu
main = MainMenu()
main()

# Save Data
Config.save_data()

# Exit
pygame.quit()
sys.exit()
