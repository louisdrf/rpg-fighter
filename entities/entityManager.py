import json
from entities.entity import Entity


class EntityManager:
    def __init__(self):
        self.monsters = []

    def loadMonstersFromJsonFile(self, jsonFilePath):
        with open(jsonFilePath, 'r') as file:
            monsters_data = json.load(file)
            monsters_list = monsters_data.get('monsters', [])
            for monster_data in monsters_list:
                self.addMonsterToGame(monster_data)

    def addMonsterToGame(self, monster_data):
        monster_entity = Entity(monster_data)
        self.monsters.append(monster_entity)


entityManager = EntityManager()
