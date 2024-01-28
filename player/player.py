from animation.animation import AnimateSprite


class Player(AnimateSprite):
    def __init__(self, sprite_sheet_path):
        super().__init__(sprite_sheet_path)

        self.sprite_sheet = sprite_sheet_path
        self.experience = 0
        self.weapon = None
        self.armor = None
        self.life = 100
        self.mana = 100
        self.caracs = {
            "agility": 0,
            "intelligence": 0,
            "chance": 0,
            "force": 0
        },
        self.level = 1
        self.position = {"x": 0, "y": 0}
        self.velocity = {"dx": 0, "dy": 0}
