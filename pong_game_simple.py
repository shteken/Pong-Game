"""
pong_game_simple.py
Pong game which sends the game data to bigquery for analysis
the data should be used for authentication
"""

import pygame

pygame.init()

FPS = 60
width, height = 640, 480
mainloop = True
ballx, bally = 550,240
dx,dy  = 600, 50                 # speed of ball surface in pixel per second !
barx, bary = 5,240
wall_thickness = 30
clock = pygame.time.Clock()        #create pygame clock object
screen = pygame.display.set_mode((width,height))
screenrect = screen.get_rect()

background = pygame.Surface(screen.get_size()) #create surface for background
background.fill((28, 28, 28))     #fill the background white (red,green,blue)
# pygame.draw.line(surface, color, start_pos, end_pos, width)
pygame.draw.line(background, (170,170,170), (0, 0), (width, 0), wall_thickness)
pygame.draw.line(background, (170,170,170), (0, height), (width, height), wall_thickness)
pygame.draw.line(background, (170,170,170), (width, 0), (width, height), wall_thickness)
background = background.convert()  #convert surface for faster blitting
screen.blit(background, (0,0))

ballsurface = pygame.Surface((10,10))     #create a new surface (black by default)
ballsurface.set_colorkey((0,0,0))         #make black the transparent color (red,green,blue)
# pygame.draw.circle(surface, color, center, radius, width)
pygame.draw.circle(ballsurface, (238,238,238), (5,5), 5) # paint white circle
ballsurface = ballsurface.convert_alpha()
ballrect = ballsurface.get_rect()

barsurface = pygame.Surface((10,50))     #create a new surface (black by default)
barsurface.set_colorkey((0,0,0))         #make black the transparent color (red,green,blue)
# pygame.draw.rect(surface, color, rect)
barrect = barsurface.get_rect()
pygame.draw.rect(barsurface, (170,170,170), (0,0,10,50)) # paint gray bar
barsurface = barsurface.convert_alpha() 

#gameover_surface = pygame.Surface((100,50)) 
myfont = pygame.font.SysFont("None", 50)
textsurface = myfont.render("Game Over", True, (170,170,170))
textsurface = textsurface.convert_alpha()
textrect = textsurface.get_rect()


def end_game():
    endloop = True
    while endloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endloop = False # pygame window closed by user
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    endloop = False # user pressed ESC
        screen.blit(textsurface, (int(width/2 - textrect.width/2), int(height/2 - textrect.height/2)))
        pygame.display.flip()

while mainloop:
    milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
    seconds = milliseconds / 1000.0 # seconds passed since last frame (float)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC
    mouse_x, mouse_y = pygame.mouse.get_pos()
    bary = mouse_y
    #calculate new center of ball (time-based)
    ballx += dx * seconds # float, since seconds passed since last frame is a decimal value
    bally += dy * seconds 
    screen.blit(background, (0,0)) # paint the background
    # bounce ball if touch the walls
    if ballx < barx + barrect.width: # left
        if bally > bary + barrect.height or bally < bary:
            mainloop = False
            end_game()
            dx = 0
            dy = 0
        else:
            ballx = barx + barrect.width
            dx *= -1 
    elif ballx + ballrect.width > screenrect.width - wall_thickness/2: # right
        ballx = screenrect.width - ballrect.width - wall_thickness/2
        dx *= -1
    if bally < wall_thickness/2: # top
        bally = wall_thickness/2
        dy *= -1
    elif bally + ballrect.height > screenrect.height - wall_thickness/2: # bottom
        bally = screenrect.height - ballrect.height - wall_thickness/2
        dy *= -1
    
    
    screen.blit(ballsurface, (int(ballx), int(bally))) # paint the ball 
    screen.blit(barsurface, (barx, bary)) # paint the bar
    
    pygame.display.flip()  # refresh frame
