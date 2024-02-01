import json
from entities.entity import Entity


class EntityManager:
    def __init__(self):
        self.entities = []

    def loadEntityFromJsonFile(self, jsonFilePath, entityType):
        with open(jsonFilePath, 'r') as file:
            entity_data = json.load(file).get(entityType)
            print(entity_data)
            if entity_data:
                self.addEntityToGame(entity_data)

    def addEntityToGame(self, entityData):
        entity = Entity(entityData)
        self.entities.append(entity)

    def printMonsters(self):
        print("Liste des monstres :")
        for monster in self.entities:
            print(f"Type: {monster.type}")
            print(f"Sprite sheet path: {monster.sprite_sheet}")
            print(f"Health: {monster.life}")
            print(f"Mana: {monster.mana}")
            print(f"Caractéristiques: {monster.caracs}")
            print(f"Level: {monster.level}")
            print(f"Position: {monster.position}")
            print(f"Velocity: {monster.velocity}")
            print(f"images: {monster.images}")
            print()  # Ligne vide pour la clarté


entityManager = EntityManager()
