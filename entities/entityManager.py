import json
from entities.entity import Entity


class EntityManager:
    def __init__(self):
        self.monsters = []
        self.pnjs = []

    def loadEntitiesFromJsonFile(self, jsonFilePath, entityType):
        with open(jsonFilePath, 'r') as file:
            entities_data = json.load(file)
            entities_list = entities_data.get(entityType, [])
            for entity_data in entities_list:
                self.addEntityToGame(entity_data, entityType)

    def addEntityToGame(self, entityData, entityType):
        entity = Entity(entityData)
        if entityType == 'monster':
            self.monsters.append(entity)
        if entityType == 'pnj':
            self.monsters.append(entity)

    def printMonsters(self):
        print("Liste des monstres :")
        for monster in self.monsters:
            print(f"Monstre ID: {monster.id}")
            print(f"Type: {monster.type}")
            print(f"Sprite sheet path: {monster.sprite_sheet}")
            print(f"Health: {monster.life}")
            print(f"Mana: {monster.mana}")
            print(f"Caractéristiques: {monster.caracs}")
            print(f"Level: {monster.level}")
            print(f"Position: {monster.position}")
            print(f"Velocity: {monster.velocity}")
            print()  # Ligne vide pour la clarté


entityManager = EntityManager()
