import pygame

from settings import Settings
import character

class Location:

    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.adj_loc = []


