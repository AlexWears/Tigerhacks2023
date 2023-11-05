import pygame
from scene import Scene, Location
from camera_scene import CameraScene
from settings import Settings

class NightDividerScene(Scene):

    def __init__(self, game, location):
        self.game = game
        game.screen.fill((25,25,25))
        self.font_night = pygame.font.Font("font/corbel.ttf",40)
        self.font_continue = pygame.font.Font("font/corbel.ttf",20)
        self.night_text = self.font_night.render("Night " + str(Settings.night + 1), True, Settings.WHITE)
        self.continue_text = self.font_continue.render("Press any key to continue...", True, Settings.WHITE)
        pygame.mixer.music.pause()

    def draw(self):
        self.game.screen.fill((25,25,25))
        self.game.screen.blit(self.night_text, (self.game.screen.get_width()/2 - self.night_text.get_width()/2, self.game.screen.get_height()/2 - self.night_text.get_height()/2))
        self.game.screen.blit(self.continue_text, (self.game.screen.get_width()/2 - self.continue_text.get_width()/2, self.game.screen.get_height()/1.3 - self.continue_text.get_height()/2))


    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            pygame.mixer.music.play()
            self.game.scene = CameraScene(self.game, "A")
            try: 
                pygame.mixer.music.load("sounds/phone calls/night" + str(Settings.night+1) + ".mp3")
                pygame.mixer.music.queue("sounds/Grinch's Ultimatum - Pilotredsun [Extended].mp3")
                pygame.mixer.music.set_volume(.25)
                pygame.mixer.music.play()
            except:
                pass