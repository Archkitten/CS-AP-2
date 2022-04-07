from config import *
from intro import Intro
from main import Main
import pygame
import sys

# Load Data
# load_data()

intro = Intro()
intro()

main_menu = Main()
main_menu()

# Save Data
# save_data()

pygame.quit()
sys.exit()
