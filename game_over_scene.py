import pygame
from scene import Scene, Location
from camera_scene import CameraScene
from settings import Settings

class GameOverScene(Scene):

    def __init__(self, game, location):
        super().__init__(game, location)
        for character in self.game.