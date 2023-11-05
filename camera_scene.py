import pygame
from scene import Scene, Location
from settings import Settings

class CameraScene(Scene):

    def __init__(self, game, location):
        super().__init__(game, location)
        self.mouse = pygame.mouse.get_pos() 
        self.HEIGHT = Settings.height
        self.WIDTH = Settings.width
        self.difference = Settings.height + Settings.screen_bottom + Settings.screen_top

        # white color 
        self.color = (255,255,255) 
        
        # light shade of the button 
        self.color_light = (170,170,170) 
        
        # dark shade of the button 
        self.color_dark = (100,100,100) 

        self.smallfont = pygame.font.Font("font/corbel.ttf",25) 
        self.largefont = pygame.font.Font("font/corbel.ttf",28) 
        self.tinyfont = pygame.font.Font("font/corbel.ttf",10) 
        self.minifont = pygame.font.Font("font/corbel.ttf",9)
        self.hugefont = pygame.font.Font("font/corbel.ttf",40)

        # rendering a text written in 
        # this font 
        #remote buttons
        self.cam1 = self.smallfont.render('1' , True , self.color) 
        self.cam2 = self.smallfont.render('2' , True , self.color) 
        self.cam3 = self.smallfont.render('3' , True , self.color) 
        self.cam4 = self.smallfont.render('4' , True , self.color) 
        self.cam5 = self.smallfont.render('5' , True , self.color) 
        self.cam6 = self.smallfont.render('6' , True , self.color) 
        self.door1 = self.largefont.render('1' , True , self.color) 
        self.door2 = self.largefont.render('2' , True , self.color) 
        self.powerButton = self.smallfont.render('X' , True , self.color) 

        #remote words
        self.cameras = self.smallfont.render('Cameras', True, self.color)
        self.doors = self.smallfont.render('Doors', True, self.color)

        #map labels
        self.you = self.tinyfont.render('You', True, self.color_dark)
        self.youlight = self.tinyfont.render('You', True, self.color)
        self.mapcam1 = self.minifont.render('Cam 1', True, self.color)
        self.mapcam2 = self.minifont.render('Cam 2', True, self.color)
        self.mapCam3 = self.minifont.render('Cam 3', True, self.color)
        self.mapCam4 = self.minifont.render('Cam 4', True, self.color)
        self.mapCam5 = self.minifont.render('Cam 5', True, self.color)
        self.mapCam6 = self.minifont.render('Cam 6', True, self.color)
        self.bathroom = self.hugefont.render('Bathroom',True,self.color)
        self.bedroom = self.hugefont.render('Bedroom',True,self.color)
        self.kitchen = self.hugefont.render('Kitchen',True,self.color)
        self.backyard = self.hugefont.render('Backyard',True,self.color)
        self.sideyard = self.hugefont.render('Sideyard',True,self.color)
        self.driveway = self.hugefont.render('Driveway',True,self.color)
        
        #power bar words
        self.power = self.smallfont.render('Power left:', True, self.color)
        self.powerdark = self.smallfont.render('Power left:', True, self.color_dark)
        self.usage = self.smallfont.render('Usage:',True, self.color)
        self.usagedark = self.smallfont.render('Usage:',True, self.color_dark)
        #varables for power
        self.powerPercent = self.smallfont.render(str(int(Settings.powerLevel)) + '%',True,self.color)
        self.powerPercentDark = self.smallfont.render(str(int(Settings.powerLevel)) + '%',True,self.color_dark)

        #clock
        self.clockTime = self.smallfont.render(str(int(Settings.clock_time)) + 'AM',True,(255,0,0))
        self.dayDisplay = self.smallfont.render('Night',True,self.color)
        self.dayDisplayDark = self.smallfont.render('Night',True,self.color_dark)
        self.dayNumber = self.smallfont.render(str(int(Settings.night + 1)),True,self.color)
        self.dayNumberDark = self.smallfont.render(str(int(Settings.night + 1)),True,self.color_dark)

    def create_scene_sprites(self):
        for c in self.game.characters:
            if c.loc == self.location:
                #draw characters in the room
                pass

    def draw(self):
        super().draw()
        self.mouse = pygame.mouse.get_pos() 
        pygame.draw.rect(self.game.screen, Settings.BLACK, pygame.Rect(self.WIDTH-198, self.HEIGHT-398, 180, 380),  0, 3)
        pygame.draw.rect(self.game.screen, Settings.BLACK, pygame.Rect(self.WIDTH-196, self.HEIGHT-396, 180, 380),  0, 3)
        pygame.draw.rect(self.game.screen, Settings.BLACK, pygame.Rect(self.WIDTH-194, self.HEIGHT-394, 180, 380),  0, 3)
        pygame.draw.rect(self.game.screen, Settings.BLACK, pygame.Rect(self.WIDTH-192, self.HEIGHT-392, 180, 380),  0, 3)
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(self.WIDTH-200, self.HEIGHT-400, 180, 380),  0, 3)
    
        self.game.screen.blit(self.cameras, (self.WIDTH-180,self.HEIGHT-385))
        self.game.screen.blit(self.doors, (self.WIDTH-180,self.HEIGHT-190))

        #power button
        if self.WIDTH-70 <= self.mouse[0] <= self.WIDTH-70+30 and self.HEIGHT-390+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-390+30+Settings.screen_top: 
            pygame.draw.rect(self.game.screen,(255,0,0),[self.WIDTH-64,self.HEIGHT-384,30,30]) 
            self.game.screen.blit(self.powerButton , (self.WIDTH-57,self.HEIGHT-380)) 
            
        else: 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-68,self.HEIGHT-388,30,30]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-66,self.HEIGHT-386,30,30]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-64,self.HEIGHT-384,30,30]) 
            pygame.draw.rect(self.game.screen,(255,0,0),[self.WIDTH-70,self.HEIGHT-390,30,30]) 
            self.game.screen.blit(self.powerButton , (self.WIDTH-63,self.HEIGHT-386)) 

        # if self.mouse is hovered on a button it 
        # changes to lighter shade  
        #remote
        #camera 1
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-350+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-350+40+Settings.screen_top: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-174,self.HEIGHT-344,60,40]) 
            self.game.screen.blit(self.cam1 , (self.WIDTH-151,self.HEIGHT-336)) 
            
        else: 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-178,self.HEIGHT-348,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-176,self.HEIGHT-346,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-174,self.HEIGHT-344,60,40]) 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-180,self.HEIGHT-350,60,40]) 
            self.game.screen.blit(self.cam1 , (self.WIDTH-157,self.HEIGHT-342)) 

        #camera 2
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-350+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-350+40+Settings.screen_top: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-94,self.HEIGHT-344,60,40]) 
            self.game.screen.blit(self.cam2 , (self.WIDTH-71,self.HEIGHT-336))
            
        else: 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-98,self.HEIGHT-348,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-96,self.HEIGHT-346,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-94,self.HEIGHT-344,60,40]) 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-100,self.HEIGHT-350,60,40]) 
            self.game.screen.blit(self.cam2 , (self.WIDTH-77,self.HEIGHT-342)) 
        
        #camera 3
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-300+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-300+40+Settings.screen_top: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-174,self.HEIGHT-294,60,40]) 
            self.game.screen.blit(self.cam3 , (self.WIDTH-151,self.HEIGHT-286)) 
            
        else: 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-178,self.HEIGHT-298,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-176,self.HEIGHT-296,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-174,self.HEIGHT-294,60,40]) 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-180,self.HEIGHT-300,60,40]) 
            self.game.screen.blit(self.cam3 , (self.WIDTH-157,self.HEIGHT-292))  
        
        #camera 4
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-300+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-300+40+Settings.screen_top: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-94,self.HEIGHT-294,60,40]) 
            self.game.screen.blit(self.cam4 , (self.WIDTH-71,self.HEIGHT-286)) 
            
        else: 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-98,self.HEIGHT-298,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-96,self.HEIGHT-296,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-94,self.HEIGHT-294,60,40]) 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-100,self.HEIGHT-300,60,40]) 
            self.game.screen.blit(self.cam4 , (self.WIDTH-77,self.HEIGHT-292)) 
        
        #camera 5
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-250+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-250+40+Settings.screen_top: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-174,self.HEIGHT-244,60,40]) 
            self.game.screen.blit(self.cam5 , (self.WIDTH-151,self.HEIGHT-236)) 
            
        else: 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-178,self.HEIGHT-248,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-176,self.HEIGHT-246,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-174,self.HEIGHT-244,60,40]) 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-180,self.HEIGHT-250,60,40]) 
            self.game.screen.blit(self.cam5 , (self.WIDTH-157,self.HEIGHT-242)) 

        
        #camera 6
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-250+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-250+40+Settings.screen_top: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-94,self.HEIGHT-244,60,40]) 
            self.game.screen.blit(self.cam6 , (self.WIDTH-71,self.HEIGHT-236)) 
            
        else: 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-98,self.HEIGHT-248,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-96,self.HEIGHT-246,60,40]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-94,self.HEIGHT-244,60,40]) 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-100,self.HEIGHT-250,60,40]) 
            self.game.screen.blit(self.cam6 , (self.WIDTH-77,self.HEIGHT-242)) 

        #door 1
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-150+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-150+105+Settings.screen_top: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-174,self.HEIGHT-144,60,105]) 
            self.game.screen.blit(self.door1 , (self.WIDTH-151,self.HEIGHT-104)) 
            
        else: 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-178,self.HEIGHT-148,60,105]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-176,self.HEIGHT-146,60,105]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-174,self.HEIGHT-144,60,105]) 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-180,self.HEIGHT-150,60,105]) 
            self.game.screen.blit(self.door1 , (self.WIDTH-157,self.HEIGHT-112)) 

        #door 2
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-150+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-150+105+Settings.screen_top: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-94,self.HEIGHT-144,60,105]) 
            self.game.screen.blit(self.door2 , (self.WIDTH-71,self.HEIGHT-104))  
            
        else: 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-98,self.HEIGHT-148,60,105]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-96,self.HEIGHT-146,60,105]) 
            pygame.draw.rect(self.game.screen,Settings.BLACK,[self.WIDTH-94,self.HEIGHT-144,60,105])
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-100,self.HEIGHT-150,60,105]) 
            self.game.screen.blit(self.door2 , (self.WIDTH-77,self.HEIGHT-112))  

        #room map
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(50, 50, 180, 180),  2, 0)
        #bathroom
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(50, 50, 80, 50),  2, 0)
        #bedroom
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(50, 98, 80, 60),  2, 0)
        #kitchen
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(50, 156, 80, 74),  2, 0)
        #hallway
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(128, 156, 102, 74),  2, 0)
        #sunroom
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(150, 22, 80, 30),  2, 0)
        #you dot
        pygame.draw.rect(self.game.screen, self.color, pygame.Rect(149, 99, 12, 12),  0, 5)
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(150, 100, 10, 10),  0, 5)
        #you word
        self.game.screen.blit(self.youlight, (143,84))
        self.game.screen.blit(self.youlight, (143,86))
        self.game.screen.blit(self.youlight, (145,84))
        self.game.screen.blit(self.youlight, (145,86))
        self.game.screen.blit(self.you, (144,85)) 
        #camera 1
        pygame.draw.rect(self.game.screen,self.color,[84,21,32,22])
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-350+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-350+Settings.screen_top+40: 
            pygame.draw.rect(self.game.screen,(238,44,44),[85,22,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 1:
                pygame.draw.rect(self.game.screen,(238,44,44),[85,22,30,20]) 
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[85,22,30,20])
        self.game.screen.blit(self.mapcam1, (88,28)) 
        #camera 2
        pygame.draw.rect(self.game.screen,self.color,[14,99,32,22])
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-350+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-350+Settings.screen_top+40:
            pygame.draw.rect(self.game.screen,(238,44,44),[15,100,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 2:
                pygame.draw.rect(self.game.screen,(238,44,44),[15,100,30,20]) 
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[15,100,30,20])
        self.game.screen.blit(self.mapcam2, (18,105)) 
        #camera 3
        pygame.draw.rect(self.game.screen,self.color,[106,237,32,22]) 
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-300+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-300+Settings.screen_top+40: 
            pygame.draw.rect(self.game.screen,(238,44,44),[107,238,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 3:
                pygame.draw.rect(self.game.screen,(238,44,44),[107,238,30,20])  
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[107,238,30,20])
        self.game.screen.blit(self.mapCam3, (110,244)) 
        #camera 4
        pygame.draw.rect(self.game.screen,self.color,[94,54,32,22])
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-300+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-300+Settings.screen_top+40:  
            pygame.draw.rect(self.game.screen,(238,44,44),[95,55,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 4:
                pygame.draw.rect(self.game.screen,(238,44,44),[95,55,30,20])  
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[95,55,30,20])
        self.game.screen.blit(self.mapCam4, (98,61)) 
        #camera 5
        pygame.draw.rect(self.game.screen,self.color,[94,102,32,22]) 
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-250+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-250+Settings.screen_top+40:  
            pygame.draw.rect(self.game.screen,(238,44,44),[95,103,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 5:
                pygame.draw.rect(self.game.screen,(238,44,44),[95,103,30,20]) 
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[95,103,30,20])
        self.game.screen.blit(self.mapCam5, (98,109)) 
        #camera 6
        pygame.draw.rect(self.game.screen,self.color,[54,204,32,22])
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-250+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-250+Settings.screen_top+40:
            pygame.draw.rect(self.game.screen,(238,44,44),[55,205,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 6:
                pygame.draw.rect(self.game.screen,(238,44,44),[55,205,30,20]) 
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[55,205,30,20])
        self.game.screen.blit(self.mapCam6, (58,211))

        #camera labels
        if Settings.cameraCurrent == 1: self.game.screen.blit(self.sideyard, (self.WIDTH/2,self.HEIGHT-50)) 
        elif Settings.cameraCurrent == 2: self.game.screen.blit(self.backyard, (self.WIDTH/2,self.HEIGHT-50)) 
        elif Settings.cameraCurrent == 3: self.game.screen.blit(self.driveway, (self.WIDTH/2,self.HEIGHT-50))
        elif Settings.cameraCurrent == 4: self.game.screen.blit(self.bathroom, (self.WIDTH/2,self.HEIGHT-50))
        elif Settings.cameraCurrent == 5: self.game.screen.blit(self.bedroom, (self.WIDTH/2,self.HEIGHT-50))
        elif Settings.cameraCurrent == 6: self.game.screen.blit(self.kitchen, (self.WIDTH/2,self.HEIGHT-50))

        #power bar
        self.game.screen.blit(self.powerdark, (19,self.HEIGHT-89)) 
        self.game.screen.blit(self.powerdark, (19,self.HEIGHT-91)) 
        self.game.screen.blit(self.powerdark, (21,self.HEIGHT-89)) 
        self.game.screen.blit(self.powerdark, (21,self.HEIGHT-91)) 
        self.game.screen.blit(self.power, (20,self.HEIGHT-90)) 
        self.game.screen.blit(self.powerPercentDark, (134,self.HEIGHT-89))
        self.game.screen.blit(self.powerPercentDark, (134,self.HEIGHT-91))
        self.game.screen.blit(self.powerPercentDark, (136,self.HEIGHT-89))
        self.game.screen.blit(self.powerPercentDark, (136,self.HEIGHT-91))
        self.game.screen.blit(self.powerPercent, (135,self.HEIGHT-90))
        self.game.screen.blit(self.usagedark, (19,self.HEIGHT-51)) 
        self.game.screen.blit(self.usagedark, (19,self.HEIGHT-49)) 
        self.game.screen.blit(self.usagedark, (21,self.HEIGHT-51)) 
        self.game.screen.blit(self.usagedark, (21,self.HEIGHT-49)) 
        self.game.screen.blit(self.usage, (20,self.HEIGHT-50)) 
        pygame.draw.rect(self.game.screen, self.color, pygame.Rect(96, self.HEIGHT-56, 88, 38),  0, 3)
        pygame.draw.rect(self.game.screen, self.color, pygame.Rect(96, self.HEIGHT-47, 94, 21),  0, 3)
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(97, self.HEIGHT-55, 86, 36),  0, 3)
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(97, self.HEIGHT-46, 92, 19),  0, 3)
        pygame.draw.rect(self.game.screen,(0,201,87),[100,self.HEIGHT-52,20,30])
        if Settings.cameraPower + Settings.door1power + Settings.door2power == 1:
            pygame.draw.rect(self.game.screen,(0,201,87),[120,self.HEIGHT-52,20,30])
            Settings.powerUsage = .2
        elif Settings.cameraPower + Settings.door1power + Settings.door2power == 2:
            pygame.draw.rect(self.game.screen,(0,201,87),[120,self.HEIGHT-52,20,30])
            pygame.draw.rect(self.game.screen,(255,215,0),[140,self.HEIGHT-52,20,30])
            Settings.powerUsage = .3
        elif Settings.cameraPower + Settings.door1power + Settings.door2power == 3:
            pygame.draw.rect(self.game.screen,(0,201,87),[120,self.HEIGHT-52,20,30])
            pygame.draw.rect(self.game.screen,(255,215,0),[140,self.HEIGHT-52,20,30])
            pygame.draw.rect(self.game.screen,(238,44,44),[160,self.HEIGHT-52,20,30])
            Settings.powerUsage = .4
        else: Settings.powerUsage = .1

        #clock and day
        pygame.draw.rect(self.game.screen, Settings.BLACK, pygame.Rect(self.WIDTH-170, 25, 100, 50),  0, 3)
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(self.WIDTH-170, 25, 100, 50),  7, 3)
        self.game.screen.blit(self.clockTime, (self.WIDTH-150,40))
        self.game.screen.blit(self.dayDisplayDark, (self.WIDTH-62,26))
        self.game.screen.blit(self.dayDisplayDark, (self.WIDTH-62,28))
        self.game.screen.blit(self.dayDisplayDark, (self.WIDTH-64,26))
        self.game.screen.blit(self.dayDisplayDark, (self.WIDTH-64,28))
        self.game.screen.blit(self.dayDisplay, (self.WIDTH-63,27))
        self.game.screen.blit(self.dayNumberDark, (self.WIDTH-39,51))
        self.game.screen.blit(self.dayNumberDark, (self.WIDTH-39,53))
        self.game.screen.blit(self.dayNumberDark, (self.WIDTH-41,51))
        self.game.screen.blit(self.dayNumberDark, (self.WIDTH-41,53))
        self.game.screen.blit(self.dayNumber, (self.WIDTH-40,52))

        
    def event_handler(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN: 
            #power
            if self.WIDTH-70 <= self.mouse[0] <= self.WIDTH-70+30 and self.HEIGHT-390+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-390+30+Settings.screen_top: 
                Settings.cameraPower = 0
                Settings.cameraCurrent = 0
                Settings.current_screen = "A"
        #cameras
            #1
            if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-350+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-350+Settings.screen_top+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 1
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 1:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 1:
                    Settings.cameraCurrent = 1
                self.game.scene = CameraScene(self.game, "I")
                Settings.current_screen = "I"

            #2
            if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-350+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-350+Settings.screen_top+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 2
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 2:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 2:
                    Settings.cameraCurrent = 2
                self.game.scene = CameraScene(self.game, "H")
                Settings.current_screen = "H"

            #3
            if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-300+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-300+Settings.screen_top+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 3
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 3:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 3:
                    Settings.cameraCurrent = 3 
                self.game.scene = CameraScene(self.game, "G")
                Settings.current_screen = "G"

            #4
            if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-300+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-300+Settings.screen_top+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 4
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 4:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 4:
                    Settings.cameraCurrent = 4
                self.game.scene = CameraScene(self.game, "E")
                Settings.current_screen = "E"

            #5
            if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-250+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-250+Settings.screen_top+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 5
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 5:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 5:
                    Settings.cameraCurrent = 5
                self.game.scene = CameraScene(self.game, "D")
                Settings.current_screen = "D"

            #6
            if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-250+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-250+Settings.screen_top+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 6
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 6:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 6:
                    Settings.cameraCurrent = 6
                self.game.scene = CameraScene(self.game, "C")
                Settings.current_screen = "C"

            if Settings.cameraPower == 0:
                self.game.scene = CameraScene(self.game, "A")
                Settings.current_screen = "A"

            #doors
            #1
            if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-150+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-150+Settings.screen_top+105: 
                if Settings.door1power == 0: 
                    Settings.door1power = 1
                elif Settings.door1power == 1:
                    Settings.door1power = 0
            #2
            if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-150+Settings.screen_top <= self.mouse[1] <= self.HEIGHT-150+Settings.screen_top+105: 
                if Settings.door2power == 0: 
                    Settings.door2power = 1
                elif Settings.door2power == 1:
                    Settings.door2power = 0

    def update(self):
        super().update()
        Location.location_image["A"] = "backgrounds/lvr" + str(Settings.door1power) + str(Settings.door2power) + ".bmp"
         #timer
        Settings.new_time = pygame.time.get_ticks()
        if Settings.new_time >= Settings.old_time + 1000:
            Settings.powerLevel -= Settings.powerUsage
            Settings.old_time = Settings.new_time
            self.powerPercent = self.smallfont.render(str(int(Settings.powerLevel)) + '%',True,self.color)
            self.powerPercentDark = self.smallfont.render(str(int(Settings.powerLevel)) + '%',True,self.color_dark)
        Settings.new_clock_time = pygame.time.get_ticks()
        if Settings.new_clock_time >= Settings.old_clock_time + (1000*90):
            Settings.old_clock_time = Settings.new_clock_time
            if Settings.clock_time == 12:
                Settings.clock_time = 1
            else: Settings.clock_time += 1
            self.clockTime = self.smallfont.render(str(int(Settings.clock_time)) + 'AM',True,self.color)


