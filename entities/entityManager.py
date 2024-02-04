import json
from entities.entity import Entity
from player.player import Player


class EntityManager:
    def __init__(self):
        self.entities = []
        self.player = None

    def loadEntityFromJsonFile(self, jsonFilePath, entityType):
        with open(jsonFilePath, 'r') as file:
            entity_data = json.load(file).get(entityType)
            if entity_data:
                self.addEntityToGame(entity_data, entityType)

    def addEntityToGame(self, entityData, entityType):
        if entityType == 'player':
            self.player = Player(entityData)
        else:
            entity = Entity(entityData)
            self.entities.append(entity)


entityManager = EntityManager()
