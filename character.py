import pygame
from settings import Settings


class Character(pygame.sprite.Sprite):
    #name is character name (string), s_loc is start location (a character A-J), aggression is an integer, sprite is sprite bmp filename
    def __init__(self, name, s_loc, aggression, sprite):
        self.image = pygame.image.load(sprite)
        
        self.name = name
        self.loc = s_loc
        self.aggression = aggression

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,0)


    def update(self):
        pass




