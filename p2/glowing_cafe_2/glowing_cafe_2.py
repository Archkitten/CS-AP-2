from config import Config
from intro_menu import IntroMenu
from main_menu import MainMenu
import pygame
import sys

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
