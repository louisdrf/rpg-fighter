import pygame
from entities.entityManager import entityManager
from player.player import Player
from screen import Screen


class Game:
    def __init__(self):
        self.main_screen = Screen(700, 700, "premier jeu")
        self.main_screen.create()

        self.entityManager = entityManager
        # self.player = Player('C:/Users/louis/PycharmProjects/platform-fighter/sprite_sheets/player.png')

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            clock.tick(60)  # Limitez la vitesse d'affichage à 10 images par seconde

        pygame.quit()
