import pygame
import pytmx
import pyscroll

from player import Player
from src.map import MapManager


class Game:

    def __init__(self):

        # create the window game
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tut")

        # generate the player
        self.player = Player(0, 0)
        self.map_manager = MapManager(self.screen, self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
            print("haut")
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
            print("bas")
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
            print("gauche")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
            print("droite")

    def update(self):
        self.map_manager.update()

    def run(self):

        clock = pygame.time.Clock()

        # game while
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
