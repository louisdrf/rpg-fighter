from entities.entity import Entity


class Perso(Entity):
    def __init__(self, sprite_sheet_path):
        super().__init__(sprite_sheet_path)
        self.experience = 0

