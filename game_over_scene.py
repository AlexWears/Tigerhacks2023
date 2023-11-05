import pygame
from scene import Scene, Location
from settings import Settings
from main_menu import MainMenuScene

class GameOverScene(Scene):

    def __init__(self, game, location):
        super().__init__(game, location)
        self.game.scene = self
        for character in self.game.character_sprites.sprites():
            if character.loc == "B" or character.loc == "F":
                self.name = character.name.lower()
                break
        else:
            self.name = "benny"
        self.current_image = 1
                

    def draw(self):
        try:
            self.background_image_path = "sprites/" + self.name + "_jumpscare/" + self.name + "_jumpscare_frame" + str(self.current_image) + ".png"
            self.game.screen.fill((40,40,40))
            self.background_image = (pygame.image.load(self.background_image_path)).convert()
            self.background_image = pygame.transform.scale(self.background_image, (Settings.width, Settings.height))
            self.game.screen.blit(self.background_image, (0, 0))
            pygame.display.flip()
            pygame.display.update()
            self.current_image = self.current_image + 1
        except:
            self.game.screen.fill((40,40,40))
            self.font_continue = pygame.font.Font("font/corbel.ttf",20)
            self.continue_text = self.font_continue.render("Press any key to continue...", True, Settings.WHITE)
            self.game.screen.blit(self.continue_text, (self.game.screen.get_width()/2 - self.continue_text.get_width()/2, self.game.screen.get_height()/1.3 - self.continue_text.get_height()/2))
            try: 
                pygame.mixer.music.pause()
            except:
                pass

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN and self.current_image >= 10:
            Settings.reset_settings()
            pygame.mixer.music.play()
            self.game.scene = MainMenuScene(self.game, "")
