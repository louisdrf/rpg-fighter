import pygame
from entities.entityManager import entityManager
from player.player import Player
from screen import Screen


class Game:
    def __init__(self):
        self.main_screen = Screen(720, 1080, "premier jeu")
        self.main_screen.create()

        self.entityManager = entityManager

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:

            self.main_screen.screen.fill((0, 0, 0))
            self.handle_input()
            self.main_screen.screen.blit(self.entityManager.player.current_image, self.entityManager.player.position)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.entityManager.player.move()
            self.entityManager.player.move_up()

        elif pressed[pygame.K_DOWN]:
            self.entityManager.player.move()
            self.entityManager.player.move_down()

        elif pressed[pygame.K_LEFT]:
            self.entityManager.player.move()
            self.entityManager.player.move_left()

        elif pressed[pygame.K_RIGHT]:
            self.entityManager.player.move()
            self.entityManager.player.move_right()

        else:
            self.entityManager.player.idle()
