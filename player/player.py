from entities.entity import Entity


class Player(Entity):
    def __init__(self, jsonFile, entityManager):
        super().__init__(jsonFile, entityManager)

        self.experience = 0
        self.weapon = None
        self.armor = None

