from animation.animation import AnimateSprite


class Entity(AnimateSprite):
    def __init__(self, jsonFileData):
        super().__init__(jsonFileData['sprite_sheet_path'])
        self.id = jsonFileData['id']
        self.type = jsonFileData['type']
        self.sprite_sheet = jsonFileData['sprite_sheet_path']
        self.life = jsonFileData['health']
        self.mana = jsonFileData['mana']
        self.caracs = jsonFileData['caracs']
        self.level = jsonFileData['level']
        self.position = jsonFileData['position']
        self.velocity = jsonFileData['velocity']
