import pygame
from settings import Settings


class Character(pygame.sprite.Sprite):
    #name is character name (string), s_loc is start location (a character in string A-J), aggression is an integer, sprite is sprite bmp filename
    def __init__(self, game, name, s_loc, aggression, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(sprite)
        
        self.name = name
        self.loc = s_loc
        self.aggression = aggression
        self.on_screen = False

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,0)


    def update(self):
        #logic for moving around rooms
        pass

    def draw(self):
        for c in game.characters:
            if c.loc == game.current_screen:
                c.on_screen = True






