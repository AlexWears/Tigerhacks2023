import pygame
from settings import settings


class Character(pygame.sprite.Sprite):

    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load(".")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.settings.width/2, self.settings.height/2)
        self.health = 0
        self.loc = 0


    def blit_character(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.blit_character()
