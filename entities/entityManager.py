import json

import pygame

from entities.entity import Entity
from player.player import Player


class EntityManager:
    def __init__(self):
        self.entities = []
        self.sprites = pygame.sprite.Group()
        self.player = None

    def loadEntityFromJsonFile(self, jsonFilePath, entityType):
        with open(jsonFilePath, 'r') as file:
            entity_data = json.load(file).get(entityType)
            if entity_data:
                self.addEntityToGame(entity_data, entityType)

    def addEntityToGame(self, entityData, entityType):
        if entityType == 'player':
            self.player = Player(entityData, self)
        else:
            entity = Entity(entityData, self)
            self.entities.append(entity)

    def addSpritesGroup(self):
        self.sprites.add(self.entities)
        self.sprites.add(self.player)


entityManager = EntityManager()
