import pygame
from settings import settings


class character(pygame.sprite.Sprite):

    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load(".")
        self.health = 0
        self.c_loc = 0
        self.s_loc = 0


    def blit_character(self):
        self.screen.blit(self.image, self.rect)

    def update(self):


    def attack(self):
