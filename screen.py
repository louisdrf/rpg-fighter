import pygame

# screen setup
class Screen:
    def __init__(self, height, width, caption):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
