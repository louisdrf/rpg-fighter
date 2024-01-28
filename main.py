import pygame

from screen import *
from game import *
from entities.entityManager import EntityManager

if __name__ == '__main__':
    # setup game
    pygame.init()
    main_screen = Screen(500, 500, "premier jeu")
    main_screen.create()

    game = Game()
    entityManager = EntityManager()
    entityManager.loadMonstersFromJsonFile('C:/Users/louis/PycharmProjects/platform-fighter/entities/entitiesDatas/monsters.json')
    print(entityManager.monsters)

    # create the screen and launch loop
    game.launch_loop()

    pygame.quit()
