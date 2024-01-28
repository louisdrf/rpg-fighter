from animation.animation import AnimateSprite


class Entity(AnimateSprite):
    def __init__(self, jsonFileData):
        super().__init__(jsonFileData['sprite_sheet_path'])
        self.id = None  # to generate randomly
        self.type = None
        self.sprite_sheet = jsonFileData['sprite_sheet_path']
        self.life = jsonFileData['health']
        self.mana = jsonFileData['mana']
        self.caracs = jsonFileData['caracs']
        self.level = jsonFileData['level'],
        self.position = jsonFileData['position']
        self.velocity = jsonFileData['velocity']
