import pygame, sys
# from network import Network
# from clue import Player
from pygame.locals import *

pygame.init()
width = 900
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


clientNumber = 0

TILE_WIDTH = 30
TILE_HEIGHT = 30
TILE_MARGIN = 1
TILE_SIZE = TILE_WIDTH+TILE_MARGIN
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
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
WHITE = 255,255,255
font = pygame.font.SysFont(None,25) # default font set at 21 points

def drawText(text, font, surface, x, y):
	textobj = font.render(text, 1, BLACK)  ## defining the text object with font and color
	textrect = textobj.get_rect() # getting size and location of this text object
	textrect.topleft = (x,y) ## setting the location of the text object
	surface.blit(textobj, textrect) ## displaying the textobject at the text location


hall = WHITE
def draw(col1, col2, row1, row2):
	for column in range(col1,col2):
		for row in range(row1,row2):
			pygame.draw.rect(win, (hall), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])

def drawHalls(win):
	## Study to Library
	draw(2,4,6,11)
	## Library to Conservatory
	draw(2,4,16,21)
	## Conservatory to Ballroom
	draw(6,10,23,25)
	## Ballroom to Kitchen
	draw(18,22,23,25)
	## Kitchen to Dining
	draw(24,26,16,21)
	## Dining to Lounge
	draw(24,26,6,11)
	## Lounge to Hall
	draw(18,22,2,4)
	## Study to Hall
	draw(6,10,2,4)
	## Library to Billiard
	draw(6,10,12,14)
	## Billiard to Dining
	draw(18,22,12,14)
	## Billiard to Ballroom
	draw(13,15,17,21)
	## Billiard to Hall
	draw(13,15,6,10)

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

	drawHalls(win)
	pygame.display.update()


def terminate():
	pygame.quit()
	sys.exit()


def main():
	run = True

	clock = pygame.time.Clock()

	while run:
		clock.tick(60)
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

main()
