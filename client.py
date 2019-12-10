
import pygame, sys
from network import Network
from clue import Player
from pygame.locals import *
import os, random
from Deck import Deck


pygame.init()
width = 900
height = 940
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


clientNumber = 0
offset = (30 + 0)

TILE_WIDTH = 30
TILE_HEIGHT = 30
TILE_MARGIN = 0
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


## Setting up a dict of list values that contain the 2 column values and 2 row values that will determine the dimensions of the rooms/hallways
tile_ids = {}
tile_ids["Study"] = [1,6,1,6]
tile_ids["Hall"] = [10,18,1,6]
tile_ids["Lounge"] = [22,27,1,6]
tile_ids["Library"] = [1,6,11,16]
tile_ids["Billiard Room"] = [10,18,10,17]
tile_ids["Dining Room"] = [22,27,11,16]
tile_ids["Conservatory"] = [1,6,21,28]
tile_ids["Ballroom"] = [10,18,21,28]
tile_ids["Kitchen"] = [22,27,21,28]
tile_ids["SL"] = [3,4,6,11]
tile_ids["SH"] = [6,10,3,4]
tile_ids["LH"] = [18,22,3,4]
tile_ids["LD"] = [24,25,6,11]
tile_ids["KD"] = [24,25,16,21]
tile_ids["KB"] = [18,22,24,25]
tile_ids["CL"] = [3,4,16,21]
tile_ids["CB"] = [6,10,24,25]
tile_ids["BL"] = [6,10,13,14]
tile_ids["BH"] = [13,14,6,10]
tile_ids["BD"] = [18,22,13,14]
tile_ids["BB"] = [13,14,17,21]

## these are the valid spaces a player can move to
move_ids = {}
move_ids["Study"] = [tile_ids["SL"], tile_ids["SH"]]
move_ids["Hall"] = [tile_ids["SH"], tile_ids["LH"], tile_ids["BH"]]
move_ids["Lounge"] = [tile_ids["LH"], tile_ids["LD"]]
move_ids["Library"] = [tile_ids["CL"], tile_ids["SL"], tile_ids["BL"]]
move_ids["Billiard Room"] = [tile_ids["BL"], tile_ids["BH"], tile_ids["BD"], tile_ids["BB"]]
move_ids["Dining Room"] = [tile_ids["BD"], tile_ids["KD"], tile_ids["LD"]]
move_ids["Conservatory"] = [tile_ids["CL"], tile_ids["CB"]]
move_ids["Ballroom"] = [tile_ids["CB"], tile_ids["BB"], tile_ids["KB"]]
move_ids["Kitchen"] = [tile_ids["KB"], tile_ids["KD"]]
move_ids["SL"] = [tile_ids["Study"], tile_ids["Library"]]
move_ids["SH"] = [tile_ids["Study"], tile_ids["Hall"]]
move_ids["LH"] = [tile_ids["Hall"], tile_ids["Lounge"]]
move_ids["LD"] = [tile_ids["Lounge"], tile_ids["Dining Room"]]
move_ids["KD"] = [tile_ids["Kitchen"], tile_ids["Dining Room"]]
move_ids["KB"] = [tile_ids["Kitchen"], tile_ids["Ballroom"]]
move_ids["CL"] = [tile_ids["Conservatory"], tile_ids["Library"]]
move_ids["CB"] = [tile_ids["Conservatory"], tile_ids["Ballroom"]]
move_ids["BL"] = [tile_ids["Billiard Room"], tile_ids["Library"]]
move_ids["BH"] = [tile_ids["Billiard Room"], tile_ids["Hall"]]
move_ids["BD"] = [tile_ids["Billiard Room"], tile_ids["Dining Room"]]
move_ids["BB"] = [tile_ids["Billiard Room"], tile_ids["Ballroom"]]

font = pygame.font.SysFont(None,25) # default font set at 21 points
player_font = pygame.font.SysFont(None,50)

def resetColorRects(location_color, col, row):
	color = location_color[col,row]
	pygame.draw.rect(win, color, [TILE_SIZE*col + TILE_MARGIN, TILE_SIZE* row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])

def drawText(text, font, surface, x, y):
	textobj = font.render(text, 1, BLACK)  ## defining the text object with font and color
	textrect = textobj.get_rect() # getting size and location of this text object
	textrect.topleft = (x,y) ## setting the location of the text object
	surface.blit(textobj, textrect) ## displaying the textobject at the text location

def drawRoomText(win):
	drawText("Study", font, win, 40, 80)
	drawText("Hall", font, win, 330, 80)
	drawText("Lounge", font, win, 700, 80)
	drawText("Library", font, win, 40, 390)
	drawText("Billiard Room", font, win, 330, 390)
	drawText("Dining Room", font, win, 700, 390)
	drawText("Conservatory", font, win, 40, 690)
	drawText("Ballroom", font, win, 330, 690)
	drawText("Kitchen", font, win, 700, 690)


def show_dashboard():
		print '***************************'
		print '* 1 - Make Accusation     *'
		print '* 2 - Make Suggestion     *'
		print '* 3 - Disprove Accusation *'
		print '* 4 - Approve Accusation  *'
		print '***************************'

def move(win):
	# doctor
	column = 10
	row = 10
	# pygame.draw.rect(win, BLACK, [TILE_SIZE*column+TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN,TILE_WIDTH,TILE_HEIGHT])
	drawText("D", player_font, win, TILE_SIZE*column, TILE_SIZE*row)

# print(nurseImage)
# DRAW HALLWAYS
hall = WHITE
def draw(col1, col2, row1, row2):
	for column in range(col1,col2):
		for row in range(row1,row2):
			pygame.draw.rect(win, (hall), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])

def draw(tile_id_values, color): ## pass in the 2 column values and 2 row values that determine the dimensions of the room/halls
	col1, col2, row1, row2 = tile_id_values[0], tile_id_values[1], tile_id_values[2], tile_id_values[3]
	for column in range(col1,col2):
		for row in range(row1,row2):
			pygame.draw.rect(win, (color), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (color)
			
def drawRoomsHalls(win):
	# Hallways
	## Study to Library
	draw(tile_ids["SL"], WHITE)
	## Library to Conservatory
	draw(tile_ids["CL"], WHITE)
	## Conservatory to Ballroom
	draw(tile_ids["CB"], WHITE)
	## Ballroom to Kitchen
	draw(tile_ids["KB"], WHITE)
	## Kitchen to Dining
	draw(tile_ids["KD"], WHITE)
	## Dining to Lounge
	draw(tile_ids["LD"], WHITE)
	## Lounge to Hall
	draw(tile_ids["LH"], WHITE)
	## Study to Hall
	draw(tile_ids["SH"], WHITE)
	## Billiard to Library
	draw(tile_ids["BL"], WHITE)
	## Billiard to Dining
	draw(tile_ids["BD"], WHITE)
	## Billiard to Ballroom
	draw(tile_ids["BB"], WHITE)
	## Billiard to Hall
	draw(tile_ids["BH"], WHITE)
	# Rooms
	## Study
	draw(tile_ids["Study"], VIOLET)
	## Hall
	draw(tile_ids["Hall"], SAFFRON)
	## Lounge
	draw(tile_ids["Lounge"],GRAY)
	## Library
	draw(tile_ids["Library"], AQUA)
	## Billiard Room
	draw(tile_ids["Billiard Room"], LIGHT_GREEN)
	## Dining Room
	draw(tile_ids["Dining Room"], BLUE)
	## Conservatory
	draw(tile_ids["Conservatory"], RED)
	## Ballroom
	draw(tile_ids["Ballroom"], PINK)
	## Kitchen
	draw(tile_ids["Kitchen"], LIGHT_BLUE)
	
	
color_rects = {}
def redrawWindow(win, player, player2):

	win.fill((52,54,54))  ## the color of the tile margins -- for now will have a slightly lighter color so the labels themselves can pop out more

	## draw out the yellow tiles and create tile ID to record the color of the tile associated with column, row values
	for column in range(TILE_WIDTH):
		for row in range(TILE_HEIGHT):
			pygame.draw.rect(win, (YELLOW), [TILE_SIZE*column + TILE_MARGIN, TILE_SIZE*row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
			color_rects[(column,row)] = (YELLOW)
			
	## invoke method to draw rooms and hallways
	drawRoomsHalls(win)
	drawRoomText(win)
	
	player.draw(win)
	player2.draw(win)
	
	player.show_accusation_and_suggestion()
	player2.show_accusation_and_suggestion()

	pygame.display.update()
	#move(win)


def terminate():
	pygame.quit()
	sys.exit()
	
def card_solution(DC, NoP):
	keys = pygame.key.get_pressed()
	if keys[pygame.K_d]:
		for i in range(NoP):
			print('Your cards: ', ', '.join(DC[i]))

def main():
	#hostname = socket.gethostname()
	#IPAddr = socket.gethostbyname(hostname)
	
	Server_IP = '172.20.10.5'
	port_num = 5555
	
	
	n = Network(Server_IP, port_num)
   	p = n.getP()
	clock = pygame.time.Clock()
	
	NoP = 1
	D = Deck()
	DC = D.DistributeCards(NoP)
	run = True
	counter = 0

	
	while run:
		clock.tick(900)
		p2 = n.send(p)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		if counter == 0:		
			p.player_info()
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			p.show_cards()
		#card_solution(DC, NoP)
		#p.move()
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = event.pos
			p.move(mouse_pos[0], mouse_pos[1])
			
		#if keys[pygame.K_LEFT]:
		#	p.move('LEFT')
##
		#if keys[pygame.K_RIGHT]:
		#	p.move('RIGHT')
##
		#if keys[pygame.K_UP]:
		#	p.move('UP')
##
		#if keys[pygame.K_DOWN]:
		#	p.move('DOWN')
		
		if keys[pygame.K_f]:
			show_dashboard()
			choice = raw_input('Enter choice: ')
			p.make_accusation_and_suggestion(x,y,choice)
			
		
		redrawWindow(win, p, p2)
		counter += 1
		#pygame.display.update()
main()
