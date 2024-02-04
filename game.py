import pygame
from entities.entityManager import entityManager
from player.player import Player
from screen import Screen


class Game:
    def __init__(self):
        self.main_screen = Screen(700, 700, "premier jeu")
        self.main_screen.create()

        self.entityManager = entityManager

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Effacez l'écran à chaque itération
            self.main_screen.screen.fill((0, 0, 0))

            # Affichage des images de l'animation "move1" du premier monstre à 10 pixels d'intervalle
            monster_images_move1 = self.entityManager.player.images["spell1"]
            x_position = 0
            for image in monster_images_move1:
                self.main_screen.screen.blit(image, (x_position, 56))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
