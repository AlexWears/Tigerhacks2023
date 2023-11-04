import pygame
from settings import settings

WIDTH = 360
HEIGHT = 480
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class game:
    # initialize pygame and create window
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # For sound
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Five Nights at JimR's")
        self.clock = pygame.time.Clock()     # For syncing the FPS



        ## group all the sprites together for ease of update
        self.sprites = pygame.sprite.Group()

    def run(self):
        # Game loop
        running = True
        while running:

            #1 Process input/events
            self.clock.tick(FPS)     ## will make the loop run at the same speed all the time
            for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
                ## listening for the the X button at the top
                if event.type == pygame.QUIT:
                    running = False


            #2 Update
            self.sprites.update()


            #3 Draw/render
            self.screen.fill(BLACK)

            

            self.sprites.draw(self.screen)

            # Done after drawing everything to the screen
            pygame.display.flip()       

        pygame.quit()