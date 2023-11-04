import pygame
from scene import Scene
from settings import Settings

class CameraScene(Scene):

    HEIGHT = Settings.height
    WIDTH = Settings.width

    # white color 
    color = (255,255,255) 
    
    # light shade of the button 
    color_light = (170,170,170) 
    
    # dark shade of the button 
    color_dark = (100,100,100) 

    smallfont = pygame.font.SysFont('Corbel',35) 
    largefont = pygame.font.SysFont('Corbel',38) 
    tinyfont = pygame.font.SysFont('Corbel',20) 
    minifont = pygame.font.SysFont('Corbel',13)

    # rendering a text written in 
    # this font 
    #remote buttons
    cam1 = smallfont.render('1' , True , color) 
    cam2 = smallfont.render('2' , True , color) 
    cam3 = smallfont.render('3' , True , color) 
    cam4 = smallfont.render('4' , True , color) 
    cam5 = smallfont.render('5' , True , color) 
    cam6 = smallfont.render('6' , True , color) 
    door1 = largefont.render('1' , True , color) 
    door2 = largefont.render('2' , True , color) 

    #remote words
    cameras = smallfont.render('Cameras', True, color)
    doors = smallfont.render('Doors', True, color)

    #map labels
    you = tinyfont.render('You', True, color)
    mapCam1 = minifont.render('Cam 1', True, color)
    mapCam2 = minifont.render('Cam 2', True, color)
    mapCam3 = minifont.render('Cam 3', True, color)
    mapCam4 = minifont.render('Cam 4', True, color)
    mapCam5 = minifont.render('Cam 5', True, color)
    mapCam6 = minifont.render('Cam 6', True, color)
    
    #power bar words
    power = smallfont.render('Power left:', True, color)
    usage = smallfont.render('Usage:',True, color)
    #varables for power
    door1power = 0
    door2power = 0
    cameraPower = 0
    cameraCurrent = 0
    powerLevel = 100
    powerPercent = smallfont.render(str(powerLevel) + '%',True,color)
    powerUsage = .01

    def __init__(self, game, location):
        super().__init__(self, game, location)

        
    def create_scene_sprites(self):
        for c in self.game.characters:
            if c.loc == self.location:
                #draw characters in the room
                pass

    def draw(self):
        
        pass
    def event_handler(self, event):
        # defining a font 
        smallfont = pygame.font.SysFont('Corbel',35) 
        largefont = pygame.font.SysFont('Corbel',38) 
        tinyfont = pygame.font.SysFont('Corbel',20) 
        minifont = pygame.font.SysFont('Corbel',13)

        # rendering a text written in 
        # this font 
        #remote buttons
        cam1 = smallfont.render('1' , True , self.color) 
        cam2 = smallfont.render('2' , True , self.color) 
        cam3 = smallfont.render('3' , True , self.color) 
        cam4 = smallfont.render('4' , True , self.color) 
        cam5 = smallfont.render('5' , True , self.color) 
        cam6 = smallfont.render('6' , True , self.color) 
        door1 = largefont.render('1' , True , self.color) 
        door2 = largefont.render('2' , True , self.color) 

        #remote words
        cameras = smallfont.render('Cameras', True, self.color)
        doors = smallfont.render('Doors', True, self.color)

        #map labels
        you = tinyfont.render('You', True, self.color)
        mapCam1 = minifont.render('Cam 1', True, self.color)
        mapCam2 = minifont.render('Cam 2', True, self.color)
        mapCam3 = minifont.render('Cam 3', True, self.color)
        mapCam4 = minifont.render('Cam 4', True, self.color)
        mapCam5 = minifont.render('Cam 5', True, self.color)
        mapCam6 = minifont.render('Cam 6', True, self.color)
        
        #power bar words
        power = smallfont.render('Power left:', True, self.color)
        usage = smallfont.render('Usage:',True, self.color)
        #varables for power
        door1power = 0
        door2power = 0
        cameraPower = 0
        cameraCurrent = 0
        powerLevel = 100
        powerPercent = smallfont.render(str(powerLevel) + '%',True,self.color)
        powerUsage = .01

        if event.type == pygame.MOUSEBUTTONDOWN: 
        #cameras
            #1
            if self.WIDTH-180 <= mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-350 <= mouse[1] <= self.HEIGHT-350+40: 
                if cameraPower == 0: 
                    cameraPower = 1
                    cameraCurrent = 1
                elif cameraPower == 1 and cameraCurrent == 1:
                    cameraPower = 0
                    cameraCurrent = 0
                elif cameraPower == 1 and not cameraCurrent == 1:
                    cameraCurrent = 1
            #2
            if self.WIDTH-100 <= mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-350 <= mouse[1] <= self.HEIGHT-350+40: 
                if cameraPower == 0: 
                    cameraPower = 1
                    cameraCurrent = 2
                elif cameraPower == 1 and cameraCurrent == 2:
                    cameraPower = 0
                    cameraCurrent = 0
                elif cameraPower == 1 and not cameraCurrent == 2:
                    cameraCurrent = 2
            #3
            if self.WIDTH-180 <= mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-300 <= mouse[1] <= self.HEIGHT-300+40: 
                if cameraPower == 0: 
                    cameraPower = 1
                    cameraCurrent = 3
                elif cameraPower == 1 and cameraCurrent == 3:
                    cameraPower = 0
                    cameraCurrent = 0
                elif cameraPower == 1 and not cameraCurrent == 3:
                    cameraCurrent = 3 
            #4
            if self.WIDTH-100 <= mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-300 <= mouse[1] <= self.HEIGHT-300+40: 
                if cameraPower == 0: 
                    cameraPower = 1
                    cameraCurrent = 4
                elif cameraPower == 1 and cameraCurrent == 4:
                    cameraPower = 0
                    cameraCurrent = 0
                elif cameraPower == 1 and not cameraCurrent == 4:
                    cameraCurrent = 4
            #5
            if self.WIDTH-180 <= mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-250 <= mouse[1] <= self.HEIGHT-250+40: 
                if cameraPower == 0: 
                    cameraPower = 1
                    cameraCurrent = 5
                elif cameraPower == 1 and cameraCurrent == 5:
                    cameraPower = 0
                    cameraCurrent = 0
                elif cameraPower == 1 and not cameraCurrent == 5:
                    cameraCurrent = 5
            #6
            if self.WIDTH-100 <= mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-250 <= mouse[1] <= self.HEIGHT-250+40: 
                if cameraPower == 0: 
                    cameraPower = 1
                    cameraCurrent = 6
                elif cameraPower == 1 and cameraCurrent == 6:
                    cameraPower = 0
                    cameraCurrent = 0
                elif cameraPower == 1 and not cameraCurrent == 6:
                    cameraCurrent = 6

            #doors
            #1
            if self.WIDTH-180 <= mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-150 <= mouse[1] <= self.HEIGHT-150+105: 
                if door1power == 0: 
                    door1power = 1
                elif door1power == 1:
                    door1power = 0
            #2
            if self.WIDTH-100 <= mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-150 <= mouse[1] <= self.HEIGHT-150+105: 
                if door2power == 0: 
                    door2power = 1
                elif door2power == 1:
                    door2power = 0

            mouse = pygame.mouse.get_pos() 

        
        

