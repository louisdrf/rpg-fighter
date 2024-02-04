from animation.animation import AnimateSprite


class Entity(AnimateSprite):
    def __init__(self, jsonFileData):
        super().__init__(jsonFileData['sprite_sheet_path'],
                         jsonFileData['sprite_sheet_array'],
                         jsonFileData['animation_indexes'],
                         jsonFileData['cut_direction'],
                         jsonFileData['height'],
                         jsonFileData['width'])

        self.type = jsonFileData['type']
        self.sprite_sheet = jsonFileData['sprite_sheet_path']
        self.life = jsonFileData['health']
        self.mana = jsonFileData['mana']
        self.caracs = jsonFileData['caracs']
        self.level = jsonFileData['level']
        self.position = jsonFileData['position']
        self.current_animation = jsonFileData['current_anim']
        self.current_image = self.images[self.current_animation][0]

    def change_anim(self):
        if self.current_animation in self.images:
            current_animation_images = self.images[self.current_animation]
            current_anim_nb_images = len(current_animation_images)
            self.clock += self.velocity * 8

            if self.clock >= 120:
                self.animation_index += 1
                self.current_image = current_animation_images[self.animation_index - 1]

                if self.animation_index >= current_anim_nb_images:
                    self.animation_index = 0

                self.clock = 0

    def move_right(self):
        self.change_anim()
        self.position[0] += self.velocity

    def move_left(self):
        self.change_anim()
        self.position[0] -= self.velocity

    def move_up(self):
        self.change_anim()
        self.position[1] -= self.velocity

    def move_down(self):
        self.change_anim()
        self.position[1] += self.velocity
