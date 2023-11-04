import pygame 
import sys 
from settings import Settings
  
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (720,720) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
clock = pygame.time.Clock()     # For syncing the FPS
clock.tick(Settings.FPS)

# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
WIDTH = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
HEIGHT = screen.get_height() 
  
# defining a font 
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

while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            #cameras
            #1
            if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-350 <= mouse[1] <= HEIGHT-350+40: 
                if cameraPower == 0: 
                    cameraPower = 1
                    cameraCurrent = 1
                elif cameraPower == 1 and cameraCurrent == 1:
                    cameraPower = 0
                    cameraCurrent = 0
                elif cameraPower == 1 and not cameraCurrent == 1:
                    cameraCurrent = 1
            #2
            if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-350 <= mouse[1] <= HEIGHT-350+40: 
                if cameraPower == 0: 
                    cameraPower = 1
                    cameraCurrent = 2
                elif cameraPower == 1 and cameraCurrent == 2:
                    cameraPower = 0
                    cameraCurrent = 0
                elif cameraPower == 1 and not cameraCurrent == 2:
                    cameraCurrent = 2
            #3
            if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-300 <= mouse[1] <= HEIGHT-300+40: 
                if cameraPower == 0: 
                    cameraPower = 1
                    cameraCurrent = 3
                elif cameraPower == 1 and cameraCurrent == 3:
                    cameraPower = 0
                    cameraCurrent = 0
                elif cameraPower == 1 and not cameraCurrent == 3:
                    cameraCurrent = 3 
            #4
            if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-300 <= mouse[1] <= HEIGHT-300+40: 
                if cameraPower == 0: 
                    cameraPower = 1
                    cameraCurrent = 4
                elif cameraPower == 1 and cameraCurrent == 4:
                    cameraPower = 0
                    cameraCurrent = 0
                elif cameraPower == 1 and not cameraCurrent == 4:
                    cameraCurrent = 4
            #5
            if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-250 <= mouse[1] <= HEIGHT-250+40: 
                if cameraPower == 0: 
                    cameraPower = 1
                    cameraCurrent = 5
                elif cameraPower == 1 and cameraCurrent == 5:
                    cameraPower = 0
                    cameraCurrent = 0
                elif cameraPower == 1 and not cameraCurrent == 5:
                    cameraCurrent = 5
            #6
            if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-250 <= mouse[1] <= HEIGHT-250+40: 
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
            if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-150 <= mouse[1] <= HEIGHT-150+105: 
                if door1power == 0: 
                    door1power = 1
                elif door1power == 1:
                    door1power = 0
            #2
            if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-150 <= mouse[1] <= HEIGHT-150+105: 
                if door2power == 0: 
                    door2power = 1
                elif door2power == 1:
                    door2power = 0
                  
    # fills the screen with a color 
    screen.fill((60,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
    
    
    pygame.draw.rect(screen, (91, 91, 91), pygame.Rect(WIDTH-200, HEIGHT-400, 180, 380),  0, 3)
    
    screen.blit(cameras, (WIDTH-159,HEIGHT-385))
    screen.blit(doors, (WIDTH-145,HEIGHT-190))

    # if mouse is hovered on a button it 
    # changes to lighter shade  
    #camera 1
    if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-350 <= mouse[1] <= HEIGHT-350+40: 
        pygame.draw.rect(screen,(0,0,0),[WIDTH-180,HEIGHT-350,60,40]) 
          
    else: 
        pygame.draw.rect(screen,color_light,[WIDTH-180,HEIGHT-350,60,40]) 

    # superimposing the text onto our button 
    screen.blit(cam1 , (WIDTH-157,HEIGHT-342))  

    #camera 2
    if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-350 <= mouse[1] <= HEIGHT-350+40: 
        pygame.draw.rect(screen,(0,0,0),[WIDTH-100,HEIGHT-350,60,40]) 
          
    else: 
        pygame.draw.rect(screen,color_light,[WIDTH-100,HEIGHT-350,60,40]) 

    # superimposing the text onto our button 
    screen.blit(cam2 , (WIDTH-77,HEIGHT-342))  
     
    #camera 3
    if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-300 <= mouse[1] <= HEIGHT-300+40: 
        pygame.draw.rect(screen,(0,0,0),[WIDTH-180,HEIGHT-300,60,40]) 
          
    else: 
        pygame.draw.rect(screen,color_light,[WIDTH-180,HEIGHT-300,60,40]) 

    # superimposing the text onto our button 
    screen.blit(cam3 , (WIDTH-157,HEIGHT-292))  
     
    #camera 4
    if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-300 <= mouse[1] <= HEIGHT-300+40: 
        pygame.draw.rect(screen,(0,0,0),[WIDTH-100,HEIGHT-300,60,40]) 
          
    else: 
        pygame.draw.rect(screen,color_light,[WIDTH-100,HEIGHT-300,60,40]) 

    # superimposing the text onto our button 
    screen.blit(cam4 , (WIDTH-77,HEIGHT-292))  
     
    #camera 5
    if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-250 <= mouse[1] <= HEIGHT-250+40: 
        pygame.draw.rect(screen,(0,0,0),[WIDTH-180,HEIGHT-250,60,40]) 
          
    else: 
        pygame.draw.rect(screen,color_light,[WIDTH-180,HEIGHT-250,60,40]) 

    # superimposing the text onto our button 
    screen.blit(cam5 , (WIDTH-157,HEIGHT-242))  
     
    #camera 6
    if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-250 <= mouse[1] <= HEIGHT-250+40: 
        pygame.draw.rect(screen,(0,0,0),[WIDTH-100,HEIGHT-250,60,40]) 
          
    else: 
        pygame.draw.rect(screen,color_light,[WIDTH-100,HEIGHT-250,60,40]) 
      
    # superimposing the text onto our button 
    screen.blit(cam6 , (WIDTH-77,HEIGHT-242))  

    #door 1
    if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-150 <= mouse[1] <= HEIGHT-150+105: 
        pygame.draw.rect(screen,(0,0,0),[WIDTH-180,HEIGHT-150,60,105]) 
          
    else: 
        pygame.draw.rect(screen,color_light,[WIDTH-180,HEIGHT-150,60,105]) 
      
    # superimposing the text onto our button 
    screen.blit(door1 , (WIDTH-157,HEIGHT-112))  

    #door 2
    if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-150 <= mouse[1] <= HEIGHT-150+105: 
        pygame.draw.rect(screen,(0,0,0),[WIDTH-100,HEIGHT-150,60,105]) 
          
    else: 
        pygame.draw.rect(screen,color_light,[WIDTH-100,HEIGHT-150,60,105]) 
      
    # superimposing the text onto our button 
    screen.blit(door2 , (WIDTH-77,HEIGHT-112))  

    #room map
    pygame.draw.rect(screen, (91, 91, 91), pygame.Rect(50, 50, 180, 180),  2, 0)
    #bathroom
    pygame.draw.rect(screen, (91, 91, 91), pygame.Rect(50, 50, 80, 50),  2, 0)
    #bedroom
    pygame.draw.rect(screen, (91, 91, 91), pygame.Rect(50, 98, 80, 60),  2, 0)
    #kitchen
    pygame.draw.rect(screen, (91, 91, 91), pygame.Rect(50, 156, 80, 74),  2, 0)
    #hallway
    pygame.draw.rect(screen, (91, 91, 91), pygame.Rect(128, 156, 102, 74),  2, 0)
    #sunroom
    pygame.draw.rect(screen, (91, 91, 91), pygame.Rect(150, 22, 80, 30),  2, 0)
    #you dot
    pygame.draw.rect(screen, (91, 91, 91), pygame.Rect(150, 100, 10, 10),  0, 5)
    #you word
    screen.blit(you, (144,85)) 
    #camera 1
    if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-350 <= mouse[1] <= HEIGHT-350+40: 
        pygame.draw.rect(screen,(238,44,44),[85,22,30,20]) 
          
    else: 
        if cameraPower == True and cameraCurrent == 1:
            pygame.draw.rect(screen,(238,44,44),[85,22,30,20]) 
        else:
            pygame.draw.rect(screen,(91,91,91),[85,22,30,20])
    screen.blit(mapCam1, (88,28)) 
    #camera 2
    if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-350 <= mouse[1] <= HEIGHT-350+40:
        pygame.draw.rect(screen,(238,44,44),[15,100,30,20]) 
          
    else: 
        if cameraPower == True and cameraCurrent == 2:
            pygame.draw.rect(screen,(238,44,44),[15,100,30,20]) 
        else:
            pygame.draw.rect(screen,(91,91,91),[15,100,30,20])
    screen.blit(mapCam2, (18,105)) 
    #camera 3
    if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-300 <= mouse[1] <= HEIGHT-300+40: 
        pygame.draw.rect(screen,(238,44,44),[107,238,30,20]) 
          
    else: 
        if cameraPower == True and cameraCurrent == 3:
            pygame.draw.rect(screen,(238,44,44),[107,238,30,20]) 
        else:
            pygame.draw.rect(screen,(91,91,91),[107,238,30,20])
    screen.blit(mapCam3, (110,244)) 
    #camera 4
    if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-300 <= mouse[1] <= HEIGHT-300+40:  
        pygame.draw.rect(screen,(238,44,44),[95,55,30,20]) 
          
    else: 
        if cameraPower == True and cameraCurrent == 4:
            pygame.draw.rect(screen,(238,44,44),[95,55,30,20]) 
        else:
            pygame.draw.rect(screen,(91,91,91),[95,55,30,20])
    screen.blit(mapCam4, (98,61)) 
    #camera 5
    if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-250 <= mouse[1] <= HEIGHT-250+40:  
        pygame.draw.rect(screen,(238,44,44),[95,103,30,20]) 
          
    else: 
        if cameraPower == True and cameraCurrent == 5:
            pygame.draw.rect(screen,(238,44,44),[95,103,30,20]) 
        else:
            pygame.draw.rect(screen,(91,91,91),[95,103,30,20])
    screen.blit(mapCam5, (98,109)) 
    #camera 6
    if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-250 <= mouse[1] <= HEIGHT-250+40:
        pygame.draw.rect(screen,(238,44,44),[55,205,30,20]) 
          
    else: 
        if cameraPower == True and cameraCurrent == 6:
            pygame.draw.rect(screen,(238,44,44),[55,205,30,20]) 
        else:
            pygame.draw.rect(screen,(91,91,91),[55,205,30,20])
    screen.blit(mapCam6, (58,211)) 

    #power bar
    screen.blit(power, (20,270)) 
    screen.blit(powerPercent, (150,270))
    screen.blit(usage, (20,295)) 
    pygame.draw.rect(screen,(0,201,87),[110,295,20,30])
    if cameraPower + door1power + door2power == 1:
        pygame.draw.rect(screen,(0,201,87),[130,295,20,30])
    elif cameraPower + door1power + door2power == 2:
        pygame.draw.rect(screen,(0,201,87),[130,295,20,30])
        pygame.draw.rect(screen,(255,215,0),[150,295,20,30])
    elif cameraPower + door1power + door2power == 3:
        pygame.draw.rect(screen,(0,201,87),[130,295,20,30])
        pygame.draw.rect(screen,(255,215,0),[150,295,20,30])
        pygame.draw.rect(screen,(238,44,44),[170,295,20,30])

    # updates the frames of the game 
    pygame.display.update()