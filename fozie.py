import pygame

from character import Character

class Fozie(Character):

    def __init__(self, game):
        super().__init__(game)

        self.image = pygame.image.load("sprites/fozie.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.settings.width/2, self.settings.height/2)
        self.loc = 1
    
    def blit_fozie(self):
        self.screen.blit(self.image, self.rect)

    def attack(self):
        