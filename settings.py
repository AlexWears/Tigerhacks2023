import pygame

class Settings:
    
    # Some Basic Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    
    FPS = 30

    # The height of the game screen
    height = 360
    width = 480

    # Where the screen is at compared to the full display
    screen_left = 0
    screen_right = 0
    screen_top = 0
    screen_bottom = 0

    # Character aggression settings [night 1, 2, 3, 4, 5] (between 1 and 20) (-1 to disable character)
    benny_ag =   [0,2,6,5,16] #first night 1
    charlie_ag = [0,5,4,6,12] #first night 1
    fozie_ag =   [0,0,2,5,10] #first night 3
    frank_ag =   [0,1,2,3,4] #first night 0
    j0mr_ag = [-1,-1,-1,-1,-1]

    # Character start locations
    benny_s_loc = "H"
    charlie_s_loc = "H"
    fozie_s_loc = "H"
    frank_s_loc = "G"
    j0mr_s_loc = 0
    
    # Current Night (0 through 4)
    night = 0
    keep_track_of_time = False

    @classmethod
    def reset_settings(self):

        #Timer
        self.old_time = 0
        self.new_time = 0
        self.clock_time = 12
        self.new_clock_time = 0
        self.old_clock_time = 0
            
        # Camera settings
        self.current_screen = 'A' #default to main room

        # Current Night (0 through 4)
        self.night = 0

        # Movement opportunity (milliseconds)
        self.time_between_moves = 1000 #should be 5000 for final version
        self.next_movement = 0

            #Power settings
        self.door1power = 0
        self.door2power = 0
        self.cameraPower = 0
        self.cameraCurrent = 0
        self.powerLevel = 10 #change back to 100
        self.powerUsage = .1

    @classmethod
    def define_screen(self, display_height, display_width):
        if (display_width / display_height) > (16 / 9):
            self.height = display_height
            self.width = (16 / 9) * display_height

        elif (display_width / display_height) < (16 / 9):
            self.width = display_width
            self.height = (9 / 16) * display_width

        else:
            self.height = display_height
            self.width = display_width

        height_gaps = (display_height - self.height) / 2
        width_gaps = (display_width -  self.width) / 2

        self.screen_left = width_gaps
        self.screen_right = width_gaps + self.width
        self.screen_top = height_gaps
        self.screen_bottom = height_gaps + self.height