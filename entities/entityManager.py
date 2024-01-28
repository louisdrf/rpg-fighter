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
