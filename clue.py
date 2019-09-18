import pygame
from network import Network

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

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 1

    def draw(self, win):
	pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)
 	self.update()

    def update(self):
	self.rect = (self.x, self.y, self.width, self.height)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


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
    pygame.init()
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
   
    p = Player(startPos[0],startPos[1],25,25,(BLUE))
    p2 = Player(6,6,25,25,(WHITE))
    clock = pygame.time.Clock()

    while run:
        clock.tick(90)
	p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
	p2.x = p2Pos[0]
	p2.y = p2Pos[1]
	p2.update()

        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
            	pygam.quit()

        p.move()
        redrawWindow(win, p, p2)

main()

