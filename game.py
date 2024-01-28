import pygame
from entities.entityManager import entityManager
from player.player import Player
from screen import Screen


class Game:
    def __init__(self):
        self.main_screen = Screen(500, 500, "premier jeu")
        self.main_screen.create()

        self.entityManager = entityManager
        self.player = Player('C:/Users/louis/PycharmProjects/platform-fighter/sprite_sheets/player.png')

    def run(self):
        clock = pygame.time.Clock()
        # boucle principale
        running = True

        while running:

            # self.player.save_location()
            # self.handle_input()
            # self.update()
            # self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
