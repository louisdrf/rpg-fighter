from animation.animation import AnimateSprite


class Entity(AnimateSprite):
    def __init__(self, sprite_sheet_path):
        super().__init__(sprite_sheet_path)
        self.id = None  # to generate randomly
        self.image = None
        self.rect = None
        self.life = None
        self.mana = None
        self.caracs = {
            "agility": 0,
            "intelligence": 0,
            "chance": 0,
            "force": 0
        },
        self.level = 0,
        self.position = [0, 0]
        self.velocity = 0
