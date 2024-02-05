import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self,
                 sprite_sheet_path,
                 sprite_sheet_array,
                 animation_indexes,
                 cut_direction,
                 height, width,
                 velocity):
        super().__init__()
        self.current_mask = None
        self.current_image = None
        self.animation_index = 0
        self.current_animation = None
        self.orientation = None
        self.velocity = velocity
        self.clock = 0
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.cut_direction = cut_direction
        self.sprite_sheet_array = sprite_sheet_array
        self.animation_indexes = animation_indexes
        self.images = self.get_images_and_masks(height, width)[0]
        self.collide_masks = self.get_images_and_masks(height, width)[1]

    def get_image_from_spritesheet(self, startX, startY, spriteHeight, spriteWidth):
        image = pygame.Surface([spriteWidth, spriteHeight], pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (startX, startY, spriteWidth, spriteHeight))
        return image

    def get_images_and_masks(self, height, width):
        images = {}
        masks = {}
        if self.cut_direction == 'TORIGHT':
            i = 0
            for animation_name, array in self.sprite_sheet_array.items():
                images_and_masks = self.cut_images_in_width(array, height, width, i)
                images[animation_name] = images_and_masks[0]
                masks[animation_name] = images_and_masks[1]
                i += 1
        return [images, masks]

    def cut_images_in_width(self, array, height, width, animationIndex):
        images = []
        masks = []
        i = 0
        for index in array:
            if index == 1:
                x = i * width
                image = self.get_image_from_spritesheet(x, animationIndex * height, height, width)
                mask = pygame.mask.from_surface(image)
                images.append(image)
                masks.append(mask)
            i += 1
        return [images, masks]

    def change_anim(self):
        if self.current_animation in self.images:
            current_animation_images = self.images[self.current_animation]
            current_mask = self.collide_masks[self.current_animation]
            current_anim_nb_images = len(current_animation_images)
            self.clock += self.velocity * 11

            if self.clock >= 120:
                self.animation_index += 1
                self.current_mask = current_mask[self.animation_index - 1]
                self.current_image = current_animation_images[self.animation_index - 1].convert_alpha()
                if self.orientation == "left":
                    self.current_image = pygame.transform.flip(self.current_image, True, False)
                    self.current_mask = pygame.mask.from_surface(self.current_image)

                if self.animation_index >= current_anim_nb_images:
                    self.animation_index = 0

                self.clock = 0


