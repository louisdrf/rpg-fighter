from entities.entity import Entity


class Player(Entity):
    def __init__(self, jsonFile):
        super().__init__(jsonFile)

        self.experience = 0
        self.weapon = None
        self.armor = None
