import pygame

from animation.animation import AnimateSprite


class Entity(AnimateSprite):
    def __init__(self, jsonFileData, entityManager):
        super().__init__(jsonFileData['sprite_sheet_path'],
                         jsonFileData['sprite_sheet_array'],
                         jsonFileData['animation_indexes'],
                         jsonFileData['cut_direction'],
                         jsonFileData['height'],
                         jsonFileData['width'],
                         jsonFileData['anim_velocity'])

        self.entityManager = entityManager
        self.type = jsonFileData['type']
        self.sprite_sheet = jsonFileData['sprite_sheet_path']
        self.life = jsonFileData['health']
        self.mana = jsonFileData['mana']
        self.caracs = jsonFileData['caracs']
        self.level = jsonFileData['level']
        self.position = jsonFileData['position']
        self.old_position = self.position.copy()
        self.current_animation = jsonFileData['current_anim']
        self.current_image = self.images[self.current_animation][0]
        self.rect = self.current_image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.current_action = "nothing"

    def save_location(self):
        self.old_position = self.position.copy()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def move_back(self):
        self.position = self.old_position

    def idle(self):
        if self.current_action != "nothing":
            self.animation_index = 0
        self.current_animation = "idle1"
        self.current_action = "nothing"
        self.change_anim()

    def move(self, direction):
        self.save_location()

        for entity in self.entityManager.entities:
            if entity != self:
                if self.rect.colliderect(entity.rect):
                    self.position = [0, 0]
                    break

        if direction == "right":
            self.orientation = "right"
            self.position[0] += self.velocity
        elif direction == "left":
            self.orientation = "left"
            self.position[0] -= self.velocity
        if direction == "up":
            self.position[1] -= self.velocity
        elif direction == "down":
            self.position[1] += self.velocity

        self.current_animation = "move1"
        self.current_action = "moving"
        self.change_anim()
