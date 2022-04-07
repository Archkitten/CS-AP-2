from config import *
from intro import Intro
from main import Main
import pygame
import sys

# Load Data
Config.load_data()
# global data
# try:
#     with open('config.txt') as config_file:
#         data = json.load(config_file)
# except FileNotFoundError:
#     pass

intro = Intro()
intro()

main_menu = Main()
main_menu()

# Save Data
Config.save_data()
# with open("config.txt", 'w') as config_file:
#     json.dump(data, config_file)

pygame.quit()
sys.exit()
