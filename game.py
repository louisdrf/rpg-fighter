import pygame


class Game:
    def __init__(self):
        self.running = True

    def launch_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
