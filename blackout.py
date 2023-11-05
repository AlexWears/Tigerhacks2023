import pygame
from scene import Scene, Location
from game_over_scene import GameOverScene
from settings import Settings

class BlackoutScene(Scene):

    def __init__(self, game, location):
        super().__init__(game, "j0mr")
        pygame.mixer.music.pause()
        self.game = game

        #print(pygame.time.get_ticks())
        self.target_time = pygame.time.get_ticks() + 5000
        #print(self.target_time)
        

        
        
    def update(self):
        if pygame.time.get_ticks() >= self.target_time:
            self.game.scene = GameOverScene(self.game, "")

        

    