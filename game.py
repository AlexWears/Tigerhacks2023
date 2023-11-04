import pygame
from settings import Settings

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

        self.background_image_path = "backgrounds/cam4.bmp"

        #characters = []
        #characters.append(Character("Benny", 'H', 1, "benny.bmp"))
        #characters.append(Character("Charlie", 'H', 1, "charlie.bmp"))
        #characters.append(Character("Fozie", 'H', 1, "fozie.bmp"))
        #characters.append(Character("Frank", 'G', 1, "frank.bmp"))
        #characters.append(Character("J0mR", 0, 1, "j0mr.bmp"))

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
            
            self.update_and_display()

        pygame.quit()

    def update_and_display(self):
            # Update all sprites
            self.sprites.update()

            # Draw/render
            self.full_screen.fill(Settings.BLACK)
            self.full_screen.blit(self.screen, (Settings.screen_left, Settings.screen_top))
            self.screen.fill(Settings.GREEN)

            self.background_image = pygame.image.load(self.background_image_path).convert()
            self.background_image = pygame.transform.scale(self.background_image, (Settings.width, Settings.height))
            self.screen.blit(self.background_image, (0, 0))

            self.sprites.draw(self.screen)

            # Done after drawing everything to the screen
            pygame.display.flip()       



if __name__ == "__main__":
    game = Game()
    game.run()