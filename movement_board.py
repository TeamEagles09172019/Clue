import pygame, sys
# from network import Network
# from clue import Player
from pygame.locals import *
import os, random
os.chdir("/Users/tomtom/Documents/JHU_MS_CS/Foundations_Software_Eng/Clue")

pygame.init()
width = 900
height = 940
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
player_font = pygame.font.SysFont(None,50)

def drawText(text, font, surface, x, y):
	textobj = font.render(text, 1, BLACK)  ## defining the text object with font and color
	textrect = textobj.get_rect() # getting size and location of this text object
	textrect.topleft = (x,y) ## setting the location of the text object
	surface.blit(textobj, textrect) ## displaying the textobject at the text location

########## DRAWING BOARD

color_rects = {}
def drawBoard(win):

	win.fill((52,54,54))  ## the color of the tile margins -- for now will have a slightly lighter color so the labels themselves can pop out more

	pygame.draw.rect(win, (0, 0, 0), [0, 0, TILE_WIDTH, TILE_HEIGHT])

## draw out the yellow tiles and create tile ID to record the color of the tile associated with column, row values
	for column in range(TILE_WIDTH):
		for row in range(TILE_HEIGHT):
			pygame.draw.rect(win, (YELLOW), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (YELLOW)
## Top Level Rooms

	# Add Study
	for column in range(1,6):
		for row in range(1,6):
			pygame.draw.rect(win, (VIOLET), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (VIOLET)
	drawText("Study", font, win, 40, 80)

	# Add Hall
	for column in range(10, 18):
		for row in range(1,6):
			pygame.draw.rect(win, (SAFFRON), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (SAFFRON)
	drawText("Hall", font, win, 330, 80)

	# Add Lounge
	for column in range(22,27):
		for row in range(1,6):
			pygame.draw.rect(win, (GRAY), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (GRAY)
	drawText("Lounge", font, win, 700, 80)

## Middle Level Rooms

	# Add Library
	for column in range(1,6):
		for row in range(11, 16):
			pygame.draw.rect(win, (AQUA), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (AQUA)
	drawText("Library", font, win, 40, 390)

	# Add Billiard
	for column in range(10, 18):
		for row in range(10, 17):
			pygame.draw.rect(win, (LIGHT_GREEN), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (LIGHT_GREEN)
	drawText("Billiard Room", font, win, 330, 390)

	# Add Dining
	for column in range(22, 27):
		for row in range(11, 16):
			pygame.draw.rect(win, (BLUE), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (BLUE)
	drawText("Dining Room", font, win, 700, 390)

## Bottom Level Rooms

	# Add Conservatory
	for column in range(1, 6):
		for row in range(21, 28):
			pygame.draw.rect(win, (RED), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (RED)
	drawText("Conservatory", font, win, 40, 690)

	# Add Ballroom
	for column in range(10, 18):
		for row in range(21, 28):
			pygame.draw.rect(win, (PINK), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (PINK)
	drawText("Ballroom", font, win, 330, 690)

	# Add Kitchen
	for column in range(22,27):
		for row in range(21,28):
			pygame.draw.rect(win, (LIGHT_BLUE), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (LIGHT_BLUE)
	drawText("Kitchen", font, win, 700, 690)

	drawHalls(win)

# DRAW HALLWAYS
hall = WHITE
def draw(col1, col2, row1, row2):
	for column in range(col1,col2):
		for row in range(row1,row2):
			pygame.draw.rect(win, (hall), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (hall)

def drawHalls(win):
	## Study to Library
	draw(3,4,6,11)
	## Library to Conservatory
	draw(3,4,16,21)
	## Conservatory to Ballroom
	draw(6,10,24,25)
	## Ballroom to Kitchen
	draw(18,22,24,25)
	## Kitchen to Dining
	draw(24,25,16,21)
	## Dining to Lounge
	draw(24,25,6,11)
	## Lounge to Hall
	draw(18,22,3,4)
	## Study to Hall
	draw(6,10,3,4)
	## Library to Billiard
	draw(6,10,13,14)
	## Billiard to Dining
	draw(18,22,13,14)
	## Billiard to Ballroom
	draw(13,14,17,21)
	## Billiard to Hall
	draw(13,14,6,10)

########## END DRAWING BOARD GAME LAYOUT


########## CREATING MOVEMENT

def validSpaces(win, col, row, roll):

	vals = []

	## South East Valid Spaces for movement
	c= col
	r = row
	val = roll
	row_counter = val
	while (row_counter >= 0):
		for i in range(0,val+1):
			col_val = c+i
			row_val = r+row_counter
			vals.append((col_val, row_val))
			row_counter -=1

	## North East Valid Spaces for movement
	c= col
	r = row
	val = roll
	row_counter = val
	while (row_counter>=0):
		for i in range(0,val+1):
			col_val = c + i
			row_val = r - row_counter
			vals.append((col_val, row_val))
			row_counter -=1

	## North West Valid Spaces for movement
	c= col
	r = row
	val = roll
	row_counter = val
	while (row_counter>=0):
		for i in range(0,val+1):
			col_val = c - i
			row_val = r - row_counter
			vals.append((col_val, row_val))
			row_counter -=1

	## South West Valid Spaces for movement
	c= col
	r = row
	val = roll
	row_counter = val
	while (row_counter>=0):
		for i in range(0,val+1):
			col_val = c - i
			row_val = r + row_counter
			vals.append((col_val, row_val))
			row_counter -=1

	valid_vals = list(set(vals))
	## show valid spaces

	return valid_vals

def creatingPointerRects(location_vals):
	location_rects = {}
	for pair in location_vals:
		col, row = pair[0], pair[1]
		r = pygame.Rect([TILE_SIZE*col + TILE_MARGIN, TILE_SIZE* row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
		location_rects[(col,row)] = r
	return location_rects

## TODO// make this a class function for player
def advancePlayerState(win, char, col, row, roll):
	old_position = [col, row]
	pygame.draw.rect(win, (GREEN), [TILE_SIZE*col + TILE_MARGIN, TILE_SIZE* row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
	r = pygame.Rect([TILE_SIZE*col + TILE_MARGIN, TILE_SIZE* row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
	drawText(char, player_font, win, TILE_SIZE*col, TILE_SIZE* row)
	valid_spaces = validSpaces(win, col,row,roll)  ## returns list -- can be edited later to directly pass validSpaces function to creatingPointerRects()
	valid_rects = creatingPointerRects(valid_spaces) ## returns dict of rects that can detect collision with mouse pointer
	return old_position, valid_rects

def resetColorRects(location_color, col, row):
	color = location_color[col,row]
	pygame.draw.rect(win, color, [TILE_SIZE*col + TILE_MARGIN, TILE_SIZE* row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])

def move(win, col, row):
	pygame.draw.rect(win, (GREEN), [TILE_SIZE*col + TILE_MARGIN, TILE_SIZE* row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
	drawText("D", player_font, win, TILE_SIZE*col, TILE_SIZE* row)
	return col,row

########## CREATING MOVEMENT

def die():
	return random.randint(1,6)

def terminate():
	pygame.quit()
	sys.exit()

def main():
	clock = pygame.time.Clock()
	drawBoard(win)

	roll = die()
	print("Die value: {}".format(roll))
	start_col = 10
	start_row = 10
	old_position, valid_rects = advancePlayerState(win, "D", start_col, start_row, roll)

	while True:
		clock.tick(600)
		new_column = 0
		new_row = 0
		continue_roll = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				terminate()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					terminate()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos
				for key, val in valid_rects.items():
					if not val.collidepoint(mouse_pos):
						new_column, new_row = old_position[0], old_position[1]
						old_position, valid_rects = advancePlayerState(win, "D", new_column, new_row,roll)
					else:
						new_column, new_row = move(win, key[0],key[1])
						resetColorRects(color_rects, old_position[0],old_position[1])
						old_position, valid_rects = advancePlayerState(win, "D", new_column, new_row,roll)
						print("Player moved {} spaces!".format(roll))
						continue_roll = True

				if continue_roll:
					roll = die()
					print("Die roll: {}".format(roll))


		pygame.display.update()

main()
