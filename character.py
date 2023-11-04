import pygame
from settings import Settings


class Character(pygame.sprite.Sprite):
    #name is character name (string), s_loc is start location (a character A-J), aggression is an integer, sprite is sprite bmp filename
    def __init__(self, Game, name, s_loc, aggression, sprite):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load(sprite)
        
        self.name = name
        self.loc = s_loc
        self.aggression = aggression

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.settings.width/2, self.settings.height/2)


    def blit_character(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.blit_character()


characters = []
characters.append(Character("Benny", 'H', 1, "benny.bmp"))
characters.append(Character("Charlie", 'H', 1, "charlie.bmp"))
characters.append(Character("Fozie", 'H', 1, "fozie.bmp"))
characters.append(Character("Frank", 'G', 1, "frank.bmp"))
characters.append(Character("J0mR", 0, 1, "j0mr.bmp"))

