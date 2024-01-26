import pygame

from screen import *
from game import *


if __name__ == '__main__':
    # setup game
    pygame.init()
    main_screen = Screen(500, 500, "premier jeu")
    game = Game()
    perso = Perso()
    perso.load_datas_from_file('filepath.json')

    # create the screen and launch loop
    main_screen.create()
    game.launch_loop()

    pygame.quit()
