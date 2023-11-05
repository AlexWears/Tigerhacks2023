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
        self.image = pygame.transform.scale(self.image, (Settings.width / 7, Settings.height / 1.7))
        
        self.name = name
        self.loc = s_loc
        self.aggression = aggression
        self.position = position

        self.on_screen = False
        self.blit_location= ((position * Settings.width / 4), Settings.height / 3.2)
        self.rect = self.image.get_rect()

        self.door1_x = 0 - 1/2 * self.rect.width
        self.door2_x = Settings.width - self.rect.width / 2
        #self.rect.update((position * Settings.width / 4 + 25), 0, .25, .25)
        #self.rect.scale_by_ip(.25, .25)


    def update(self):
        #print(self.loc)
        #print(Settings.current_screen)
        if self.on_screen == False:
            if (secrets.randbelow(20) + 1) <= self.aggression[Settings.night]: #if random number (between 1 and 20) is less than aggression (as nights go by, aggression increases so there is a greater chance to take the movement opportunity each night.)
                #if in B and door 2 is open (0) then game over (jumpscare)
                #if in F and door 1 is open (0) then game over (jumpscare)
                #else override move (go to H)
                
                self.prev_loc = self.loc
                self.move = random.choice(Location.adjacent_locations[self.loc]) # Take even random chance to go to any adjacent room
                if self.move != Settings.current_screen: # Then check that the character is not trying to move into the current room
                    self.loc = self.move
                    print(self.name + " has taken the opportunity to move from " + self.prev_loc + " " + self.loc + ".\n")


    def draw(self):
        if self.loc == Settings.current_screen:
            self.on_screen = True
        else:
            self.on_screen = False

        if Settings.current_screen == "A":
            if self.loc == "F" and Settings.door1power == 0:
                self.game.screen.blit(self.image, (self.door1_x, Settings.height / 4.75))
            if self.loc == "B" and Settings.door2power == 0:
                self.game.screen.blit(self.image, (self.door2_x, Settings.height / 4.75))
            else:
                return
        if self.on_screen:
            self.game.screen.blit(self.image, self.blit_location)







