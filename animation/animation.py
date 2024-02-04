import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_path, sprite_sheet_array, animation_indexes, cut_direction, height, width):
        super().__init__()
        self.animation_index = 0
        self.velocity = 2
        self.clock = 0
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.cut_direction = cut_direction
        self.sprite_sheet_array = sprite_sheet_array
        self.animation_indexes = animation_indexes
        self.images = self.cut_all_sprite_sheet_images(height, width)

    def get_image_from_spritesheet(self, startX, startY, spriteHeight, spriteWidth):
        image = pygame.Surface([spriteWidth, spriteHeight], pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (startX, startY, spriteWidth, spriteHeight))
        return image

    def cut_all_sprite_sheet_images(self, height, width):
        images = {}
        if self.cut_direction == 'TORIGHT':
            i = 0
            for animation_name, array in self.sprite_sheet_array.items():
                images[animation_name] = self.cut_images_in_width(array, height, width, i)
                i += 1
        return images

    def cut_images_in_width(self, array, height, width, animationIndex):
        images = []
        i = 0
        for index in array:
            if index == 1:
                x = i * width
                image = self.get_image_from_spritesheet(x, animationIndex * height, height, width)
                images.append(image)
            i += 1
        return images
