import pygame
import secrets
import random

from settings import Settings
from scene import Location


class Character(pygame.sprite.Sprite):
    #name is character name (string), s_loc is start location (a character in string A-J), aggression is a list of integers, sprite is sprite bmp filename, position is an integer 0 through 3
    def __init__(self, game, name, s_loc, aggression, sprite, position):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(sprite)
        
        self.name = name
        self.loc = s_loc
        self.aggression = aggression
        self.position = position

        self.on_screen = False

        self.rect = self.image.get_rect()
        self.rect.update((position * Settings.width / 4), 0, (Settings.width / 4), Settings.height)


    def update(self):
        if(self.loc == Settings.current_screen):
            self.on_screen = True
        else:
            self.on_screen = False

        if (secrets.randbelow(20) + 1) <= self.aggression[Settings.night]: #if random number (between 1 and 20) is less than aggression (as nights go by, aggression increases so there is a greater chance to take the movement opportunity each night.)
            self.prev_loc = self.loc
            #take even random chance to go to any adjacent room
            self.loc = random.choice(Location.adjacent_locations[self.loc])
            print(self.name + " has taken the opportunity to move from " + self.prev_loc + " " + self.loc + ".\n")

    def draw(self):
        if self.on_screen:
            self.game.scene.blit(self.image, self.rect)
        
        pass







