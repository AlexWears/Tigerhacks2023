import pygame
from settings import Settings

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game:
    # initialize pygame and create window
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # For sound
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Five Nights at JimR's")
        self.clock = pygame.time.Clock()     # For syncing the FPS
        self.clock.tick(Settings.FPS)     # will make the loop run at the same speed all the time

        Settings.define_screen(pygame.display.get_surface().get_height(), pygame.display.get_surface().get_width())

        ## group all the sprites together for ease of update
        self.sprites = pygame.sprite.Group()

    def run(self):
        # Game loop
        running = True
        print(Settings.screen_left)
        print(Settings.screen_top)
        while running:

            #1 Process input/events
            for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
                ## listening for the the X button at the top
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False


            #2 Update
            self.sprites.update()


            #3 Draw/render
            self.screen.fill(BLACK)
            pygame.draw.rect(self.screen, GREEN, pygame.Rect(Settings.screen_left, Settings.screen_top, Settings.width, Settings.height), 0)

            self.sprites.draw(self.screen)

            # Done after drawing everything to the screen
            pygame.display.flip()       

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()