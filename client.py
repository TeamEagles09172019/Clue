import pygame
from network import Network
from clue import Player
from Dashboard import Dashboard
import threading
import sys

width = 625
height = 625
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")





clientNumber = 0

TILE_WIDTH = 25
TILE_HEIGHT = 25
TILE_MARGIN = 1
TILE_SIZE = TILE_WIDTH+TILE_MARGIN
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
RED = 255, 0, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0
BROWN = 128, 128, 0

def func1(a):
	from Tkinter import *
	top = Tk()
	top.geometry('200x200')
	btn = Button(top, text = 'Make Suggestion', bd = '5', command = top.destroy)
	btn.pack(side = 'top')

	btn = Button(top, text = 'Approve Suggestion', bd = '5', command = top.destroy)
	btn.pack(side = 'top')
	btn = Button(top, text = 'Disprove Suggestion', bd = '5', command = top.destroy)
	btn.pack(side = 'top')
	btn = Button(top, text = 'Show Suggestion', bd = '5', command = top.destroy)
	btn.pack(side = 'top')
	top.mainloop()

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


	
	

def main():
    print "Calling the application's main"
    run = True
    print "Creating network instance"
    print "n = Network()"

    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    
	
    #thread1 = threading.Thread(target = func1, args = (1,))
    #thread1.start()

    #D = Dashboard()

    

    while run:
        clock.tick(60)
	p2 = n.send(p)
        for event in pygame.event.get():
	    #if event.type == pygame.MOUSEBUTTONDOWN:
		#p.user_input()
            if event.type == pygame.QUIT:
            	run = False

	if event.type == pygame.MOUSEBUTTONDOWN:
		p.user_input()

        p.move()
       	redrawWindow(win, p, p2) #put dashboard updates in redrawwindow function
	
   

main()


