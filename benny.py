import pygame

from character import Character

class Benny(Character):

    def __init__(self, game):
        super().__init__(game)

        self.image = pygame.image.load("sprites/benny.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.settings.width/2, self.settings.height/2)
        self.loc = 1
    
    def blit_benny(self):
        self.screen.blit(self.image, self.rect)

    def attack(self):
