import pygame

from settings import Settings

class Location:

    adjacent_locations = {
        "A": ["B", "F"],
        "B": ["H"],
        "C": ["B", "D", "G", "H"],
        "D": ["C", "E"],
        "E": ["D", "H"],
        "F": ["H"],
        "G": ["C", "H", "J"],
        "H": ["C", "E", "G", "I"],
        "I": ["F", "H"],
        "J": ["G", "F"]
    }

    location_image = {
        "Main Menu": "backgrounds/Title Screen.bmp",
        "End Screen": "",
        "Blackout": "backgrounds/power_off_lvr.bmp",
        "A": "backgrounds/lvr00.bmp",
        "B": "",
        "C": "backgrounds/cam6.bmp",
        "D": "backgrounds/cam5.bmp",
        "E": "backgrounds/cam4.bmp",
        "F": "",
        "G": "backgrounds/cam3.bmp",
        "H": "backgrounds/cam2.bmp",
        "I": "backgrounds/cam1.bmp",
        "J": ""
    }

class Scene:
    def __init__(self, game, location):
        self.location = location
        self.game = game
        try:
            self.background_image = pygame.image.load(Location.location_image[location]).convert()
            game.background_image = pygame.transform.scale(self.background_image, (Settings.width, Settings.height))
        except:
            pass
        self.scene_sprites = pygame.sprite.Group()
        Settings.keep_track_of_time = False

    def update(self):
        pass
    
    def draw(self):
        self.background_image = pygame.image.load(Location.location_image[self.location]).convert()
        self.background_image = pygame.transform.scale(self.background_image, (Settings.width, Settings.height))
        self.game.screen.blit(self.background_image, (0, 0))

    def event_handler(self, event):
        pass

    def create_scene_sprites(self):
        pass

    