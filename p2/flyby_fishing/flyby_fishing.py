from config import *
from intro import Intro
from main import Main
import json
import pygame
import sys

intro = Intro()
intro()

main_menu = Main()
main_menu()

with open("config.txt", 'w') as config_file:
    json.dump(data, config_file)

pygame.quit()
sys.exit()
