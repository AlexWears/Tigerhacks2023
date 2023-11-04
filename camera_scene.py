import pygame
from scene import Scene

class CameraScene(Scene):

    def __init__(self, game, location):
        super().__init__(self, game, location)

        
    def create_scene_sprites(self):
        for c in self.game.characters:
            if c.loc == self.location:
                #draw characters in the room
                pass

    def draw(self):
        pass

    def event_handler(self, event):
        

        
        

