import pygame

from game import *

if __name__ == '__main__':
    # setup game
    pygame.init()
    game = Game()

    # charger les entités du jeu
    game.entityManager.loadEntityFromJsonFile('C:/Users/louis/PycharmProjects/platform-fighter/entities/entitiesDatas/monsters/golem.json', 'golem')
    # game.entityManager.loadEntitiesFromJsonFile('C:/Users/louis/PycharmProjects/platform-fighter/entities/entitiesDatas/pnjs.json', 'pnj')
    game.entityManager.printMonsters()
    game.run()
