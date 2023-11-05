import pygame
from scene import Scene, Location
from camera_scene import CameraScene
from game_over_scene import GameOverScene
from settings import Settings

class BlackoutScene(Scene):

    def __init__(self, game, location):
        super().__init__(game, "Blackout")
        pygame.mixer.music.pause()
        self.game = game
        Settings.keep_track_of_time = True
        
        self.j0mr_time = pygame.time.get_ticks() + 5000 # target time is 20 seconds away
        self.over_time = self.j0mr_time + 5000 # game over time is 5 seconds after j0mr shows up
        

        
    def update(self):
        if pygame.time.get_ticks() >= self.j0mr_time:
            self.game.characters[4].on_screen = True

        if pygame.time.get_ticks() >= self.over_time:
            self.game.characters[4].on_screen = False
            self.game.scene = GameOverScene(self.game, "")

    
        
        

    def draw(self):
        super().draw()
        self.game.characters[4].draw()

    