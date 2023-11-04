import pygame

from character import Character

class Frank(Character):

    def __init__(self, game):
        super().__init__(game)

        self.image = pygame.image.load("sprites/frank.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.settings.width/2, self.settings.height/2)
        self.s_loc = 2
    
    def blit_frank(self):
        self.screen.blit(self.image, self.rect)

    def attack(self):
        