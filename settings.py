import pygame

class Settings:
    
    # Display Settings
    height = 360
    width = 480
    FPS = 30

    screen_left = 0
    screen_right = 0
    screen_top = 0
    screen_bottom = 0

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

        print(self.screen_left)
        print(self.screen_top)