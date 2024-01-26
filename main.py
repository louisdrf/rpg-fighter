import pygame

from perso.perso import Perso
from screen import *
from game import *


if __name__ == '__main__':
    # setup game
    pygame.init()
    main_screen = Screen(500, 500, "premier jeu")
    game = Game()
    perso = Perso()

    # create the screen and launch loop
    main_screen.create()
    game.launch_loop()

    pygame.quit()
