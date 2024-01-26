import pygame


# screen setup
class Screen:
    def __init__(self, height, width, caption):
        self.screen = None
        self.height = height
        self.width = width
        self.caption = caption

    def create(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
