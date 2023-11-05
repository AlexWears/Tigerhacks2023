import pygame
from scene import Scene, Location
from settings import Settings

class WinScene(Scene):

    def __init__(self, game, location):
        super().__init__(game, "End Screen")
        self.game = game
        
        self.font_continue = pygame.font.Font("font/corbel.ttf",20)
        
        self.continue_text = self.font_continue.render("Press [Esc] to exit victorious!", True, Settings.WHITE)
        