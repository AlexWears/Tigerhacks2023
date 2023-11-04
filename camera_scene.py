import pygame
from scene import Scene
from settings import Settings

class CameraScene(Scene):

    def __init__(self, game, location):
        super().__init__(game, location)
        self.mouse = pygame.mouse.get_pos() 
        self.HEIGHT = Settings.height
        self.WIDTH = Settings.width

        # white color 
        self.color = (255,255,255) 
        
        # light shade of the button 
        self.color_light = (170,170,170) 
        
        # dark shade of the button 
        self.color_dark = (100,100,100) 

        self.smallfont = pygame.font.SysFont('Corbel',35) 
        self.largefont = pygame.font.SysFont('Corbel',38) 
        self.tinyfont = pygame.font.SysFont('Corbel',20) 
        self.minifont = pygame.font.SysFont('Corbel',13)

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

        #remote words
        self.cameras = self.smallfont.render('Cameras', True, self.color)
        self.doors = self.smallfont.render('Doors', True, self.color)

        #map labels
        self.you = self.tinyfont.render('You', True, self.color)
        self.mapcam1 = self.minifont.render('Cam 1', True, self.color)
        self.mapcam2 = self.minifont.render('Cam 2', True, self.color)
        self.mapCam3 = self.minifont.render('Cam 3', True, self.color)
        self.mapCam4 = self.minifont.render('Cam 4', True, self.color)
        self.mapCam5 = self.minifont.render('Cam 5', True, self.color)
        self.mapCam6 = self.minifont.render('Cam 6', True, self.color)
        
        #power bar words
        self.power = self.smallfont.render('Power left:', True, self.color)
        self.usage = self.smallfont.render('Usage:',True, self.color)
        #varables for power
        self.powerLevel = 100
        self.powerPercent = self.smallfont.render(str(self.powerLevel) + '%',True,self.color)

        
    def create_scene_sprites(self):
        for c in self.game.characters:
            if c.loc == self.location:
                #draw characters in the room
                pass

    def draw(self):
        super().draw()
        self.mouse = pygame.mouse.get_pos() 
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(self.WIDTH-200, self.HEIGHT-400, 180, 380),  0, 3)
    
        self.game.screen.blit(self.cameras, (self.WIDTH-159,self.HEIGHT-385))
        self.game.screen.blit(self.doors, (self.WIDTH-145,self.HEIGHT-190))

        # if self.mouse is hovered on a button it 
        # changes to lighter shade  
        #camera 1
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-293 <= self.mouse[1] <= self.HEIGHT-293+40: 
            pygame.draw.rect(self.game.screen,(0,0,0),[self.WIDTH-180,self.HEIGHT-350,60,40]) 
            
        else: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-180,self.HEIGHT-350,60,40]) 

        # superimposing the text onto our button 
        self.game.screen.blit(self.cam1 , (self.WIDTH-157,self.HEIGHT-342))  

        #camera 2
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-293 <= self.mouse[1] <= self.HEIGHT-293+40: 
            pygame.draw.rect(self.game.screen,(0,0,0),[self.WIDTH-100,self.HEIGHT-350,60,40]) 
            
        else: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-100,self.HEIGHT-350,60,40]) 

        # superimposing the text onto our button 
        self.game.screen.blit(self.cam2 , (self.WIDTH-77,self.HEIGHT-342))  
        
        #camera 3
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-243 <= self.mouse[1] <= self.HEIGHT-243+40: 
            pygame.draw.rect(self.game.screen,(0,0,0),[self.WIDTH-180,self.HEIGHT-300,60,40]) 
            
        else: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-180,self.HEIGHT-300,60,40]) 

        # superimposing the text onto our button 
        self.game.screen.blit(self.cam3 , (self.WIDTH-157,self.HEIGHT-292))  
        
        #camera 4
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-243 <= self.mouse[1] <= self.HEIGHT-243+40: 
            pygame.draw.rect(self.game.screen,(0,0,0),[self.WIDTH-100,self.HEIGHT-300,60,40]) 
            
        else: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-100,self.HEIGHT-300,60,40]) 

        # superimposing the text onto our button 
        self.game.screen.blit(self.cam4 , (self.WIDTH-77,self.HEIGHT-292))  
        
        #camera 5
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-193 <= self.mouse[1] <= self.HEIGHT-193+40: 
            pygame.draw.rect(self.game.screen,(0,0,0),[self.WIDTH-180,self.HEIGHT-250,60,40]) 
            
        else: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-180,self.HEIGHT-250,60,40]) 

        # superimposing the text onto our button 
        self.game.screen.blit(self.cam5 , (self.WIDTH-157,self.HEIGHT-242))  
        
        #camera 6
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-193 <= self.mouse[1] <= self.HEIGHT-193+40: 
            pygame.draw.rect(self.game.screen,(0,0,0),[self.WIDTH-100,self.HEIGHT-250,60,40]) 
            
        else: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-100,self.HEIGHT-250,60,40]) 
        
        # superimposing the text onto our button 
        self.game.screen.blit(self.cam6 , (self.WIDTH-77,self.HEIGHT-242))  

        #door 1
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-93 <= self.mouse[1] <= self.HEIGHT-93+105: 
            pygame.draw.rect(self.game.screen,(0,0,0),[self.WIDTH-180,self.HEIGHT-150,60,105]) 
            
        else: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-180,self.HEIGHT-150,60,105]) 
        
        # superimposing the text onto our button 
        self.game.screen.blit(self.door1 , (self.WIDTH-157,self.HEIGHT-112))  

        #door 2
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-93 <= self.mouse[1] <= self.HEIGHT-93+105: 
            pygame.draw.rect(self.game.screen,(0,0,0),[self.WIDTH-100,self.HEIGHT-150,60,105]) 
            
        else: 
            pygame.draw.rect(self.game.screen,self.color_light,[self.WIDTH-100,self.HEIGHT-150,60,105]) 
        
        # superimposing the text onto our button 
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
        pygame.draw.rect(self.game.screen, (91, 91, 91), pygame.Rect(150, 100, 10, 10),  0, 5)
        #you word
        self.game.screen.blit(self.you, (144,85)) 
        #camera 1
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-293 <= self.mouse[1] <= self.HEIGHT-293+40: 
            pygame.draw.rect(self.game.screen,(238,44,44),[85,22,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 1:
                pygame.draw.rect(self.game.screen,(238,44,44),[85,22,30,20]) 
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[85,22,30,20])
        self.game.screen.blit(self.mapcam1, (88,28)) 
        #camera 2
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-293 <= self.mouse[1] <= self.HEIGHT-293+40:
            pygame.draw.rect(self.game.screen,(238,44,44),[15,100,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 2:
                pygame.draw.rect(self.game.screen,(238,44,44),[15,100,30,20]) 
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[15,100,30,20])
        self.game.screen.blit(self.mapcam2, (18,105)) 
        #camera 3
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-243 <= self.mouse[1] <= self.HEIGHT-243+40: 
            pygame.draw.rect(self.game.screen,(238,44,44),[107,238,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 3:
                pygame.draw.rect(self.game.screen,(238,44,44),[107,238,30,20]) 
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[107,238,30,20])
        self.game.screen.blit(self.mapCam3, (110,244)) 
        #camera 4
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-243 <= self.mouse[1] <= self.HEIGHT-243+40:  
            pygame.draw.rect(self.game.screen,(238,44,44),[95,55,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 4:
                pygame.draw.rect(self.game.screen,(238,44,44),[95,55,30,20]) 
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[95,55,30,20])
        self.game.screen.blit(self.mapCam4, (98,61)) 
        #camera 5
        if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-193 <= self.mouse[1] <= self.HEIGHT-193+40:  
            pygame.draw.rect(self.game.screen,(238,44,44),[95,103,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 5:
                pygame.draw.rect(self.game.screen,(238,44,44),[95,103,30,20]) 
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[95,103,30,20])
        self.game.screen.blit(self.mapCam5, (98,109)) 
        #camera 6
        if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-193 <= self.mouse[1] <= self.HEIGHT-193+40:
            pygame.draw.rect(self.game.screen,(238,44,44),[55,205,30,20]) 
            
        else: 
            if Settings.cameraPower == 1 and Settings.cameraCurrent == 6:
                pygame.draw.rect(self.game.screen,(238,44,44),[55,205,30,20]) 
            else:
                pygame.draw.rect(self.game.screen,(91,91,91),[55,205,30,20])
        self.game.screen.blit(self.mapCam6, (58,211)) 

        #power bar
        self.game.screen.blit(self.power, (20,270)) 
        self.game.screen.blit(self.powerPercent, (150,270))
        self.game.screen.blit(self.usage, (20,295)) 
        pygame.draw.rect(self.game.screen,(0,201,87),[110,295,20,30])
        if Settings.cameraPower + Settings.door1power + Settings.door2power == 1:
            pygame.draw.rect(self.game.screen,(0,201,87),[130,295,20,30])
            Settings.powerUsage = .02
        elif Settings.cameraPower + Settings.door1power + Settings.door2power == 2:
            pygame.draw.rect(self.game.screen,(0,201,87),[130,295,20,30])
            pygame.draw.rect(self.game.screen,(255,215,0),[150,295,20,30])
            Settings.powerUsage = .03
        elif Settings.cameraPower + Settings.door1power + Settings.door2power == 3:
            pygame.draw.rect(self.game.screen,(0,201,87),[130,295,20,30])
            pygame.draw.rect(self.game.screen,(255,215,0),[150,295,20,30])
            pygame.draw.rect(self.game.screen,(238,44,44),[170,295,20,30])
            Settings.powerUsage = .04
        else: Settings.powerUsage = .01

        pass
    def event_handler(self, event):
        # defining a font 
        self.smallfont = pygame.font.SysFont('Corbel',35) 
        self.largefont = pygame.font.SysFont('Corbel',38) 
        self.tinyfont = pygame.font.SysFont('Corbel',20) 
        self.minifont = pygame.font.SysFont('Corbel',13)

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

        #remote words
        self.cameras = self.smallfont.render('Cameras', True, self.color)
        self.doors = self.smallfont.render('Doors', True, self.color)

        #map labels
        self.you = self.tinyfont.render('You', True, self.color)
        self.mapcam1 = self.minifont.render('Cam 1', True, self.color)
        self.mapcam2 = self.minifont.render('Cam 2', True, self.color)
        self.mapCam3 = self.minifont.render('Cam 3', True, self.color)
        self.mapCam4 = self.minifont.render('Cam 4', True, self.color)
        self.mapCam5 = self.minifont.render('Cam 5', True, self.color)
        self.mapCam6 = self.minifont.render('Cam 6', True, self.color)
        
        #power bar words
        self.power = self.smallfont.render('Power left:', True, self.color)
        self.usage = self.smallfont.render('Usage:',True, self.color)
        #varables for power
        self.powerPercent = self.smallfont.render(str(self.powerLevel) + '%',True,self.color)

        if event.type == pygame.MOUSEBUTTONDOWN: 
        #cameras
            #1
            if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-293 <= self.mouse[1] <= self.HEIGHT-293+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 1
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 1:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 1:
                    Settings.cameraCurrent = 1
            #2
            if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-293 <= self.mouse[1] <= self.HEIGHT-293+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 2
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 2:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 2:
                    Settings.cameraCurrent = 2
            #3
            if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-243 <= self.mouse[1] <= self.HEIGHT-243+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 3
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 3:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 3:
                    Settings.cameraCurrent = 3 
            #4
            if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-243 <= self.mouse[1] <= self.HEIGHT-243+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 4
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 4:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 4:
                    Settings.cameraCurrent = 4
            #5
            if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-193 <= self.mouse[1] <= self.HEIGHT-193+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 5
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 5:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 5:
                    Settings.cameraCurrent = 5
            #6
            if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-193 <= self.mouse[1] <= self.HEIGHT-193+40: 
                if Settings.cameraPower == 0: 
                    Settings.cameraPower = 1
                    Settings.cameraCurrent = 6
                elif Settings.cameraPower == 1 and Settings.cameraCurrent == 6:
                    Settings.cameraPower = 0
                    Settings.cameraCurrent = 0
                elif Settings.cameraPower == 1 and not Settings.cameraCurrent == 6:
                    Settings.cameraCurrent = 6

            #doors
            #1
            if self.WIDTH-180 <= self.mouse[0] <= self.WIDTH-180+60 and self.HEIGHT-93 <= self.mouse[1] <= self.HEIGHT-93+105: 
                if Settings.door1power == 0: 
                    Settings.door1power = 1
                elif Settings.door1power == 1:
                    Settings.door1power = 0
            #2
            if self.WIDTH-100 <= self.mouse[0] <= self.WIDTH-100+60 and self.HEIGHT-93 <= self.mouse[1] <= self.HEIGHT-93+105: 
                if Settings.door2power == 0: 
                    Settings.door2power = 1
                elif Settings.door2power == 1:
                    Settings.door2power = 0

        
        

