class FighterEntity:
    def __init__(self):
        self.life = None
        self.mana = None
        self.caracs = {
            "agility": 0,
            "intelligence": 0,
            "chance": 0,
            "force": 0
        },
        self.experience = 0,
        self.level = 0,
        self.position = [0, 0]
        self.velocity = None

    def load_datas_from_file(self, filepath):
        print('have to load entity data from json file')
