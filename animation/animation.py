import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_path):
        super().__init__()
        self.animation_index = 0
        self.velocity = 0
        self.clock = 0
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.images = None
