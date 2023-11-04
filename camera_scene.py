import pygame
from scene import Scene

class CameraScene(Scene):

    def __init__(self, game, location):
        super().__init__(self, game, location)

        
    def create_scene_sprites(self):
        for c in game.characters:
            if c.loc == self.location:
                #draw characters in the room
                pass

        
        

