<<<<<<< HEAD
import pygame, sys
from network import Network
from clue import Player
from pygame.locals import *

pygame.init()
width = 900
height = 900
=======
import pygame
from network import Network
from clue import Player
import sys

width = 625
height = 625
>>>>>>> 5e0172ffcc3eff328fc8d828c1476fde0931cf3b
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


clientNumber = 0

<<<<<<< HEAD
TILE_WIDTH = 30
TILE_HEIGHT = 30
=======
TILE_WIDTH = 25
TILE_HEIGHT = 25
>>>>>>> 5e0172ffcc3eff328fc8d828c1476fde0931cf3b
TILE_MARGIN = 1
TILE_SIZE = TILE_WIDTH+TILE_MARGIN
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
<<<<<<< HEAD
LIGHT_GREEN = 38, 77, 0
RED = 255, 0, 0
YELLOW = 250, 230, 0
BROWN = 128, 128, 0
SAFFRON = 255,153,51
LIGHT_BLUE = 201, 255, 229
PINK = 241, 156, 187
AQUA =  16,206,200
GRAY = 160,160,160
GOLD = 181, 152, 73
VIOLET = 153, 51, 255
BLUE = 68, 106, 255

font = pygame.font.SysFont(None,25) # default font set at 21 points

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)  ## defining the text object with font and color
    textrect = textobj.get_rect() # getting size and location of this text object
    textrect.topleft = (x,y) ## setting the location of the text object
    surface.blit(textobj, textrect) ## displaying the textobject at the text location

# def redrawWindow(win, player, player2):

def drawHalls(win):

    
    pass
def redrawWindow(win):

    win.fill((52,54,54))  ## the color of the tile margins -- for now will have a slightly lighter color so the labels themselves can pop out more

    pygame.draw.rect(win, (0, 0, 0), [0, 0, TILE_WIDTH, TILE_HEIGHT])

    ## draw out the yellow tiles
    for column in range(TILE_WIDTH):
        for row in range(TILE_HEIGHT):
            pygame.draw.rect(win, (YELLOW), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
## Top Level Rooms

    # Add Study
    for column in range(1,6):
        for row in range(1,6):
            pygame.draw.rect(win, (VIOLET), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Study", font, win, 40, 80)

    # Add Hall
    for column in range(10, 18):
        for row in range(1,6):
            pygame.draw.rect(win, (SAFFRON), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Hall", font, win, 330, 80)

    # Add Lounge
    for column in range(22,27):
        for row in range(1,6):
            pygame.draw.rect(win, (GRAY), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Lounge", font, win, 700, 80)

## Middle Level Rooms

    # Add Library
    for column in range(1,6):
        for row in range(11, 16):
            pygame.draw.rect(win, (AQUA), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Library", font, win, 40, 390)

    # Add Billiard
    for column in range(10, 18):
        for row in range(10, 17):
            pygame.draw.rect(win, (LIGHT_GREEN), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Billiard Room", font, win, 330, 390)

    # Add Dining
    for column in range(22, 27):
        for row in range(11, 16):
            pygame.draw.rect(win, (BLUE), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Dining Room", font, win, 700, 390)

## Bottom Level Rooms

    # Add Conservatory
    for column in range(1, 6):
        for row in range(21, 28):
            pygame.draw.rect(win, (RED), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Conservatory", font, win, 40, 690)

    # Add Ballroom
    for column in range(10, 18):
        for row in range(21, 28):
            pygame.draw.rect(win, (PINK), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Ballroom", font, win, 330, 690)

    # Add Kitchen
    for column in range(22,27):
        for row in range(21,28):
            pygame.draw.rect(win, (LIGHT_BLUE), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
    drawText("Kitchen", font, win, 700, 690)
    # Player.draw(win)
    # Player2.draw(win)
    pygame.display.update()

def terminate():
    pygame.quit()
    sys.exit()
=======
RED = 255, 0, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0
BROWN = 128, 128, 0

def redrawWindow(win,player, player2):
    win.fill((0,0,0))
 
    pygame.draw.rect(win, (0,0,0), [0, 0, TILE_WIDTH, TILE_HEIGHT])
		
    for row in range(25):
	for column in range(25):	
		pygame.draw.rect(win, (255,255,0), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN,TILE_WIDTH,TILE_HEIGHT])
	

    #Add Kitchen
    for row in range(7):
	for column in range(4):
    		pygame.draw.rect(win, (BLACK), [TILE_SIZE*row + TILE_MARGIN, TILE_SIZE*column+    TILE_MARGIN,TILE_WIDTH, TILE_HEIGHT])
    #Add lounge
    for row in range(9,14):
	for column in range(7):
    		pygame.draw.rect(win, (BLUE), [TILE_SIZE*row + TILE_MARGIN, TILE_SIZE*column+    TILE_MARGIN,TILE_WIDTH, TILE_HEIGHT])

    #Add Hall
    for row in range(16,24):
   	for column in range(6):
    		pygame.draw.rect(win, (RED), [TILE_SIZE*row + TILE_MARGIN, TILE_SIZE*column+ TILE_MARGIN,TILE_WIDTH, TILE_HEIGHT])

    #Add dinning room
    for row in range(6):
   	for column in range(6,10):
    		pygame.draw.rect(win, (GREEN), [TILE_SIZE*row + TILE_MARGIN, TILE_SIZE*column+ TILE_MARGIN,TILE_WIDTH, TILE_HEIGHT])

   #Add study
    for row in range(6):
   	for column in range(12,16):
    		pygame.draw.rect(win, (BLUE), [TILE_SIZE*row + TILE_MARGIN, TILE_SIZE*column+ TILE_MARGIN,TILE_WIDTH, TILE_HEIGHT])

   #Add Conservatory
    for row in range(5):
   	for column in range(18,24):
    		pygame.draw.rect(win, (RED), [TILE_SIZE*row + TILE_MARGIN, TILE_SIZE*column+ TILE_MARGIN,TILE_WIDTH, TILE_HEIGHT])

  #Add Clue
    for row in range(8, 13):
   	for column in range(8, 14):
    		pygame.draw.rect(win, (GREEN), [TILE_SIZE*row + TILE_MARGIN, TILE_SIZE*column+ TILE_MARGIN,TILE_WIDTH, TILE_HEIGHT])

  #Add Ballroom
    for row in range(15,24):
   	for column in range(8,15):
    		pygame.draw.rect(win, (BLACK), [TILE_SIZE*row + TILE_MARGIN, TILE_SIZE*column+ TILE_MARGIN,TILE_WIDTH, TILE_HEIGHT])


    player.draw(win)
    player2.draw(win)
    pygame.display.update()
>>>>>>> 5e0172ffcc3eff328fc8d828c1476fde0931cf3b


def main():
    run = True
<<<<<<< HEAD
    # n = Network()
    # p = n.getP()
=======
    n = Network()
    p = n.getP()
>>>>>>> 5e0172ffcc3eff328fc8d828c1476fde0931cf3b
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
<<<<<<< HEAD
        # p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            # p.move()
            # redrawWindow(win, p, p2)

        redrawWindow(win)
=======
	p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
            	pygam.quit()

        p.move()
        redrawWindow(win, p, p2)
>>>>>>> 5e0172ffcc3eff328fc8d828c1476fde0931cf3b

main()
