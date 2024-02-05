import pygame

from game import *

if __name__ == '__main__':
    # setup game
    pygame.init()
    game = Game()

    # charger les entités du jeu
    game.entityManager.loadEntityFromJsonFile('C:/Users/louis/PycharmProjects/platform-fighter/entities/entitiesDatas/monsters/golem.json', 'golem')
    game.entityManager.loadEntityFromJsonFile('C:/Users/louis/PycharmProjects/platform-fighter/entities/entitiesDatas/monsters/demon.json', 'demon')

    game.entityManager.loadEntityFromJsonFile('C:/Users/louis/PycharmProjects/platform-fighter/entities/entitiesDatas/player/player.json', 'player')
    game.entityManager.addSpritesGroup()
    game.run()
