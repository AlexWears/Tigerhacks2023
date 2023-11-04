import pygame

from settings import Settings

class Location:

    adjacent_locations = {
        "A": ["B", "F"],
        "B": ["A", "C"],
        "C": ["B", "D", "G", "H"],
        "D": ["C", "E"],
        "E": ["D", "H"],
        "F": ["A", "I"],
        "G": ["C", "H", "J"],
        "H": ["C", "E", "G", "I"],
        "I": ["F", "H"],
        "J": ["G", "F"]
    }

    location_camera_image = {
        "Main Menu": "",
        "End Screen": "",
        "A": "",
        "B": "",
        "C": "",
        "D": "",
        "E": "backgrounds/cam1.bmp",
        "F": "",
        "G": "",
        "H": "",
        "I": "backgrounds/cam1.bmp",
        "J": ""
    }

class Scene:
    def __init__(self, game, location):
        self.location = location
        self.game = game
        self.background_image = pygame.image.load(Location.location_camera_image[location]).convert()
        game.background_image = pygame.transform.scale(self.background_image, (Settings.width, Settings.height))
    
    def draw(self):
        self.background_image = pygame.transform.scale(self.background_image, (Settings.width, Settings.height))
        self.game.screen.blit(self.background_image, (0, 0))


    