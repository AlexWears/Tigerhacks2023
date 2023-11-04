import pygame
from settings import Settings
from scene import Location, Scene
from character import Character
from camera_scene import CameraScene

class Game:
    # initialize pygame and create window
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # For sound
        self.full_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Five Nights at JimR's")
        self.clock = pygame.time.Clock()     # For syncing the FPS
        self.clock.tick(Settings.FPS)     # will make the loop run at the same speed all the time

        Settings.define_screen(pygame.display.get_surface().get_height(), pygame.display.get_surface().get_width())
        self.screen = pygame.Surface((Settings.width, Settings.height))

        # Group all the sprites together for ease of update
        self.sprites = pygame.sprite.Group()
        self.scene = CameraScene(self, "E")

        characters = []
        characters.append(Character("Benny", 'H', Settings.benny_ag[0], "sprites/benny.bmp"))
        characters.append(Character("Charlie", 'H', Settings.charlie_ag[0], "sprites/charlie.bmp"))
        characters.append(Character("Fozie", 'H', Settings.fozie_ag[0], "sprites/fozie.bmp"))
        characters.append(Character("Frank", 'G', Settings.frank_ag[0], "sprites/frank.bmp"))
        # characters.append(Character("J0mR", 0, 1, "j0mr.bmp"))

        self.character_sprites = pygame.sprite.Group(characters)


    def run(self):
        # Game loop
        running = True
        while running:
            # Process input/events
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                self.scene.event_handler(event)
            
            self.update_and_display()

        pygame.quit()

    def update_and_display(self):
            # Update all sprites
            #self.sprites.update()
            self.scene.update()
            if self.scene.isinstance(CameraScene):
                self.character_sprites.update()
            self.character_sprites.update()

            # Draw
            self.full_screen.fill(Settings.BLACK)
            self.full_screen.blit(self.screen, (Settings.screen_left, Settings.screen_top))

            self.scene.draw()
            self.sprites.draw(self.screen)

            # Done after drawing everything to the screen
            pygame.display.flip()       



if __name__ == "__main__":
    game = Game()
    game.run()