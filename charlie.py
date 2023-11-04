import pygame

from character import Character

class Charlie(Character):

    def __init__(self, game):
        super().__init__(game)

        self.image = pygame.image.load("sprites/charlie.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.settings.width/2, self.settings.height/2)
        self.loc = 'H'
    
    def blit_charlie(self):
        self.screen.blit(self.image, self.rect)

    def attack(self):
        