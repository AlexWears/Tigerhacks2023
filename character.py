import pygame
import secrets

from settings import Settings
from scene import Location


class Character(pygame.sprite.Sprite):
    #name is character name (string), s_loc is start location (a character in string A-J), aggression is a list of integers, sprite is sprite bmp filename
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
        if pygame.time.get_ticks() >= Settings.next_movement: #if it is time for a movement opportunity
            print("Movement opportunity\n")
            if (secrets.randbelow(10) + 1) <= self.aggression[Settings.night]: #if random number (between 1 and 10) is less than aggression (as nights go by, aggression increases so there is a greater chance to take the movement opportunity each night.)
                print(self.name + " has taken the opportunity to move\n")
                #take even chance to go to any adjacent room (figuring this out)
                pass
            Settings.next_movement = pygame.time.get_ticks() + Settings.time_between_moves
        pass

    def draw(self):
        pass
        #for c in game.characters:
         #   if c.loc == Settings.current_screen:
          #      c.on_screen = True
           # else:
            #    c.on_screen = False







