import pygame

from game import *

if __name__ == '__main__':
    # setup game
    pygame.init()
    game = Game()

    # charger les entités du jeu
    game.entityManager.loadEntitiesFromJsonFile('C:/Users/louis/PycharmProjects/platform-fighter/entities/entitiesDatas/monsters.json', 'monster')
    # game.entityManager.loadEntitiesFromJsonFile('C:/Users/louis/PycharmProjects/platform-fighter/entities/entitiesDatas/pnjs.json', 'pnj')

    game.run()
