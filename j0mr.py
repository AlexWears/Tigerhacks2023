import pygame

from character import Character

class J0mR(Character):

    def __init__(self, game):
        super().__init__(game)

        self.image = pygame.image.load("sprites/j0mr.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.settings.width/2, self.settings.height/2)
        self.s_loc = 0
    
    def blit_darkj0mr(self):
        self.screen.blit(self.image, self.rect)

    def attack(self):
        