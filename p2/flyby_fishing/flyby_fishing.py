from intro import Intro
from main import Main
import json
import pygame
import sys

intro = Intro()
intro()

main_menu = Main()
main_menu()

pygame.quit()
sys.exit()
