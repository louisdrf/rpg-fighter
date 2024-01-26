import pygame
from screen import *
from game import *

if __name__ == '__main__':
    pygame.init()
    main_screen = Screen(500, 500, "premier jeu")
    game = Game()
    game.launch_loop()
    pygame.quit()

