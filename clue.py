import pygame
import random
import socket


width = 625
height = 625
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")



offset = 30
## Setting up a dict of list values that contain the 2 column values and 2 row values that will determine the dimensions of the rooms/hallways
tile_ids = {}
tile_ids["Study"] = [1 * offset,6 * offset,1 * offset ,6 * offset]
tile_ids["Hall"] = [10 * offset,18* offset,1* offset,6* offset]
tile_ids["Lounge"] = [22* offset,27* offset,1* offset,6* offset]
tile_ids["Library"] = [1* offset,6* offset,11* offset,16* offset]
tile_ids["Billiard Room"] = [10* offset,18* offset,10* offset,17* offset]
tile_ids["Dining Room"] = [22* offset,27* offset,11* offset,16* offset]
tile_ids["Conservatory"] = [1* offset,6* offset,21* offset,28* offset]
tile_ids["Ballroom"] = [10* offset,18* offset,21* offset,28* offset]
tile_ids["Kitchen"] = [22* offset,27* offset,21* offset,28* offset]
tile_ids["SL"] = [3* offset,4* offset,6* offset,11* offset]
tile_ids["SH"] = [6* offset,10* offset,3* offset,4* offset]
tile_ids["LH"] = [18* offset,22* offset,3* offset,4* offset]
tile_ids["LD"] = [24* offset,25* offset,6* offset,11* offset]
tile_ids["KD"] = [24* offset,25* offset,16* offset,21* offset]
tile_ids["KB"] = [18* offset,22* offset,24* offset,25* offset]
tile_ids["CL"] = [3* offset,4* offset,16* offset,21* offset]
tile_ids["CB"] = [6* offset,10* offset,24* offset,25* offset]
tile_ids["BL"] = [6* offset,10* offset,13* offset,14* offset]
tile_ids["BH"] = [13* offset,14* offset,6* offset,10* offset]
tile_ids["BD"] = [18* offset,22* offset,13* offset,14* offset]
tile_ids["BB"] = [13* offset,14* offset,17* offset,21* offset]

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

PlayerNames = {
    -1: '-',
    0 : 'Colonel Mustard',
    1 : 'Miss Scarlet',
    2 : 'Professor Plum',
    3 : 'Mr. Green',
    4 : 'Mrs. White',
    5 : 'Mrs. Peacock'
    }

WeaponNames = {
    -1: '-',
    0 : 'Rope',
    1 : 'Lead Pipe',
    2 : 'Knife',
    3 : 'Wrench',
    4 : 'Candlestick',
    5 : 'Revolver'
    }

RoomNames = {
    -1: '-',
    0 : 'Study Room',
    1 : 'Hall',
    2 : 'Lounge',
    3 : 'Library',
    4 : 'Billiard Room',
    5 : 'Dining Room',
    6 : 'Conservatory',
    7 : 'Ball Room',
    8 : 'Kitchen'
    }


class Player():
	def __init__(self, x, y, width, height, color, accusation, suggestion, ipAddr, port, room, cards):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.rect = (x,y,width,height)
		self.text_variable = ''
		self.accusation = accusation
		self.suggestion = suggestion
		self.name = ''
		self.approve_disprove = ''
		self.ip = ipAddr
		self.port = port
		self.room = room
		self.shuffled_cards = cards
		
	def show_cards(self):
		print('Your cards: ', self.shuffled_cards)
		
	def identifyRoom(self, col, row):
		## iterate through the list of tile_id col/row values to find which room holds the player's current col/row in order to identify his/her current room
		for key, value in tile_ids.items():
			room_col1, room_col2, room_row1, room_row2 = value[0], value[1], value[2], value[3]
			if (col >= room_col1) and (col <= room_col2) and (row >= room_row1) and (row <= room_row2):
				return key ## returns string value of current room/hallway
			
	def player_info(self):
		print '**********'
		print '*C L U E *'
		print '**********'
		name = raw_input('Enter player name: ')
		self.name = name[0]
		
	def draw(self,win):
	
		font = pygame.font.SysFont(None,25) # default font set at 21 points
		if self.room:
			pygame.draw.rect(win, self.color, self.rect)
			textobj = font.render(self.name, 1, BLACK)
			textrect = textobj.get_rect()
			textrect.topleft = (self.x, self.y)
			win.blit(textobj, textrect)
			
		if self.room is None:
			pygame.draw.rect(win, self.color, (self.prev_pos_x, self.prev_pos_y, TILE_WIDTH, TILE_HEIGHT))
			textobj = font.render(self.name, 1, BLACK)
			textrect = textobj.get_rect()
			textrect.topleft = (self.prev_pos_x, self.prev_pos_y)
			win.blit(textobj, textrect)
		
	
	def show_accusation_and_suggestion(self):
		hostname = socket.gethostname()
		IPAddr = socket.gethostbyname(hostname)
		self.ip = IPAddr
		if self.accusation != 'No accusation':
			print self.name +"'s("+self.ip+ ':' + str(self.port) + ')' +' accusation: ', self.accusation
		if self.suggestion != 'No suggestion':
			print self.name + "'s("+self.ip+':' + str(self.port) + ')' + ' suggestion: ', self.suggestion
	
				
	def make_accusation_and_suggestion(self, x,y,choice):
		#Do this only if player is in a room
		if choice == '1':	
			if self.room and len(self.room) != 2:
				name = raw_input('Enter name of player: ')	
				weapon = raw_input('Enter weapon: ')
				
				if name in PlayerNames.values() and weapon in WeaponNames.values():
					self.accusation = self.name + ' accuses ' + name + ','+ weapon +','+ self.room
				else:
					print 'Invalid Input!'
					self.accusation = ''
			else:
				print 'You have to be in a room to make an accusation'
					
		if choice == '2':
			
			if self.room and len(self.room) != 2:
				name = raw_input('Enter name of player: ')	
				weapon = raw_input('Enter weapon: ')
				if name in PlayerNames.values() and weapon in WeaponNames.values():
					self.suggestion = name + ','+ weapon +','+ room
				else:
					print 'Invalid Input!'
					self.suggestion = ''
			else:
				print 'You have to be in a room to make a suggestion'
		
		if choice == '3':
			self.approve_disprove = False
		if choice == '4':
			self.approve_disprove = True
			
	def creatingPointerRects(self, valid_locations): ## pass in list of lists
		location_rects = {}
		for room in valid_locations:
			col1, col2, row1, row2 = room[0], room[1], room[2], room[3]
			for col in range(col1,col2):
				for row in range(row1,row2):
					r = pygame.Rect([TILE_SIZE*col + TILE_MARGIN, TILE_SIZE* row + TILE_MARGIN, TILE_WIDTH, TILE_HEIGHT])
					location_rects[(col,row)] = r
	
		return location_rects
				
	def move(self, x, y):
		self.x = x
		self.y = y
		pos = (self.x, self.y)
		self.room = self.identifyRoom(self.x, self.y)
		
		if self.room is not None:
			self.rect = (self.x, self.y, TILE_WIDTH, TILE_HEIGHT)
			self.prev_pos_x = self.x
			self.prev_pos_y = self.y
			print 'Valid Move ', self.x, self.y 		
						
		else:
			print 'Move is invalid, try again: Previous Pos is: ', self.prev_pos_x, self.prev_pos_y
			
			
		#if direction == 'LEFT':
		#	self.x -= self.vel

		#if direction == 'RIGHT':
		#	self.x += self.vel
		#

		#if direction == 'UP':
		#	self.y -= self.vel
		#
		#if direction == 'DOWN':
		#	self.y += self.vel
		
	def update(self):
		self.rect = (self.x, self.y, TILE_WIDTH, TILE_HEIGHT)
	


