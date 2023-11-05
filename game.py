import pygame
from settings import Settings
from scene import Location, Scene
from character import Character
from camera_scene import CameraScene
from night_divider import NightDividerScene
from main_menu import MainMenuScene

class Game:
    # initialize pygame and create window
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # For sound
        pygame.mixer.music.load("sounds/Grinch's Ultimatum - Pilotredsun [Extended].mp3")
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(-1)
        Settings.reset_settings()
        self.full_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Five Nights at JimR's")
        self.clock = pygame.time.Clock()     # For syncing the FPS
        self.clock.tick(Settings.FPS)     # will make the loop run at the same speed all the time

        Settings.define_screen(pygame.display.get_surface().get_height(), pygame.display.get_surface().get_width())
        self.screen = pygame.Surface((Settings.width, Settings.height))

        # Group all the sprites together for ease of update
        self.sprites = pygame.sprite.Group()
        #self.scene = CameraScene(self, "A")

        self.characters = []
        
        self.benny = Character(self,"Benny", 'H', Settings.benny_ag, "sprites/benny.png", 0)
        self.charlie = Character(self, "Charlie", 'H', Settings.charlie_ag, "sprites/charlie.png", 1)
        self.fozie = Character(self, "Fozie", 'H', Settings.fozie_ag, "sprites/fozie.png", 2)
        self.frank = Character(self, "Frank", 'G', Settings.frank_ag, "sprites/frank.png", 3)

        self.characters.append(self.benny)
        self.characters.append(self.charlie)
        self.characters.append(self.fozie)
        self.characters.append(self.frank)
        # characters.append(Character("J0mR", 0, 1, "j0mr.bmp"))

        self.character_sprites = pygame.sprite.Group(self.characters)
        self.scene = MainMenuScene(self, "")


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
            if isinstance(self.scene, CameraScene):
                if pygame.time.get_ticks() >= Settings.next_movement: #if it is time for a movement opportunity
                    print("Movement opportunity\n")

                    self.character_sprites.update()
                    Settings.next_movement = pygame.time.get_ticks() + Settings.time_between_moves
            Settings.new_time = pygame.time.get_ticks()
            if Settings.new_time >= Settings.old_time + 1000:
                Settings.powerLevel -= Settings.powerUsage
                Settings.old_time = Settings.new_time
                #blackout
                if Settings.powerLevel <= 0:
                    pass
            Settings.new_clock_time = pygame.time.get_ticks()
            if Settings.new_clock_time >= Settings.old_clock_time + (1000*90):
                Settings.old_clock_time = Settings.new_clock_time
                if Settings.clock_time == 12:
                    Settings.clock_time = 1
                else: Settings.clock_time += 1
                if Settings.clock_time == 6:
                    Settings.new_clock_time = 0
                    Settings.old_clock_time = 0
                    #night change
                    Settings.night += 1
                    #win
                    if Settings.night == 6:
                        pass

            #self.character_sprites.update()

            # Draw
            self.full_screen.fill(Settings.BLACK)
            self.full_screen.blit(self.screen, (Settings.screen_left, Settings.screen_top))

            self.scene.draw()
            for character in self.character_sprites.sprites():
                character.draw()

            # Done after drawing everything to the screen
            pygame.display.flip()
            pygame.display.update()

    def create_characters(self):
        self.characters.clear()
        self.character_sprites.empty()

        self.benny = Character(self,"Benny", 'H', Settings.benny_ag, "sprites/benny.png", 0)
        self.charlie = Character(self, "Charlie", 'H', Settings.charlie_ag, "sprites/charlie.png", 1)
        self.fozie = Character(self, "Fozie", 'H', Settings.fozie_ag, "sprites/fozie.png", 2)
        self.frank = Character(self, "Frank", 'G', Settings.frank_ag, "sprites/frank.png", 3)

        self.characters.append(self.benny)
        self.characters.append(self.charlie)
        self.characters.append(self.fozie)
        self.characters.append(self.frank)

        self.character_sprites = pygame.sprite.Group(self.characters)



if __name__ == "__main__":
    game = Game()
    game.run()