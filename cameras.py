import pygame 
import sys 
  
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (720,720) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
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

# rendering a text written in 
# this font 
cam1 = smallfont.render('1' , True , color) 
cam2 = smallfont.render('2' , True , color) 
cam3 = smallfont.render('3' , True , color) 
cam4 = smallfont.render('4' , True , color) 
cam5 = smallfont.render('5' , True , color) 
cam6 = smallfont.render('6' , True , color) 
door1 = largefont.render('1' , True , color) 
door2 = largefont.render('2' , True , color) 

cameras = smallfont.render('Cameras', True, color)
doors = smallfont.render('Doors', True, color)
  
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
                pygame.quit() 
            #2
            if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-350 <= mouse[1] <= HEIGHT-350+40: 
                pygame.quit() 
            #3
            if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-300 <= mouse[1] <= HEIGHT-300+40: 
                pygame.quit() 
            #4
            if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-300 <= mouse[1] <= HEIGHT-300+40: 
                pygame.quit() 
            #5
            if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-250 <= mouse[1] <= HEIGHT-250+40: 
                pygame.quit() 
            #6
            if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-250 <= mouse[1] <= HEIGHT-250+40: 
                pygame.quit() 

            #doors
            #1
            if WIDTH-180 <= mouse[0] <= WIDTH-180+60 and HEIGHT-150 <= mouse[1] <= HEIGHT-150+105: 
                pygame.quit() 
            #2
            if WIDTH-100 <= mouse[0] <= WIDTH-100+60 and HEIGHT-150 <= mouse[1] <= HEIGHT-150+105: 
                pygame.quit() 
                  
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
     
    # updates the frames of the game 
    pygame.display.update()