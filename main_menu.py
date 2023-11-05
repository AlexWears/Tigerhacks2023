import pygame
from scene import Scene, Location
from camera_scene import CameraScene
from night_divider import NightDividerScene
from settings import Settings

class MainMenuScene(Scene):

    def __init__(self, game, location):
        super().__init__(game, "Main Menu")
        pygame.mixer.music.play()
        self.game = game
        
        self.font_button = pygame.font.Font("font/corbel.ttf",40)

        self.play_btn_text = self.font_button.render("Press Any Button to Play", True, Settings.WHITE)
        self.quit_btn_text = self.font_button.render("[Esc] to Quit", True, Settings.WHITE)
        self.play_rect = self.play_btn_text.get_rect()
        self.quit_rect = self.quit_btn_text.get_rect()
        self.game.create_characters()
        
        

    def draw(self):
        #self.game.screen.fill((25,25,25))
        super().draw()
        self.game.screen.blit(self.play_btn_text, (4*self.game.screen.get_width()/5 - self.play_btn_text.get_width()/2, 2*self.game.screen.get_height()/3 - self.play_btn_text.get_height()/2))
        self.game.screen.blit(self.quit_btn_text, (4*self.game.screen.get_width()/5 - self.quit_btn_text.get_width()/2, 4*self.game.screen.get_height()/5 - self.quit_btn_text.get_height()/2))


    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            pygame.mixer.music.play()
            self.game.scene = NightDividerScene(self.game, "")