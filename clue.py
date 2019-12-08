import pygame
from Tkinter import *
import random
import socket



TESTING = 1
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
text_variable = ''
Show_Accusation_label = ''
inputUser4 = ''

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
	def __init__(self, x, y, width, height, color, accusation, suggestion, ipAddr, port):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.rect = (x,y,width,height)
		self.vel = 2
		self.text_variable = ''
		self.accusation = accusation
		self.suggestion = suggestion
		self.name = ''
		self.approve_disprove = ''
		self.ip = ipAddr
		self.port = port
		self.location = ''

			
	def player_info(self):
		print '**********'
		print '*C L U E *'
		print '**********'
		name = raw_input('Enter player name: ')
		self.name = name[0]
		
	def draw(self, win):
		font = pygame.font.SysFont(None,25) # default font set at 21 points
		player_font = pygame.font.SysFont(None,50)

		pygame.draw.rect(win, self.color, self.rect)
		textobj = font.render(self.name, 1, BLACK)
		textrect = textobj.get_rect()
		textrect.topleft = (self.x, self.y)
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
		if choice == '1':	
			#Do this only if player is in a room
			room = 'N/A'
			name = raw_input('Enter name of player: ')	
			weapon = raw_input('Enter weapon: ')
			
			if name in PlayerNames.values() and weapon in WeaponNames.values():
				self.accusation = self.name + ' accuses ' + name + ','+ weapon +','+ room
			else:
				self.accusation = ''
				
		if choice == '2':
			#Do this only if player is in a room
			room = 'N/A'
			name = raw_input('Enter name of player: ')	
			weapon = raw_input('Enter weapon: ')
			
			if name in PlayerNames.values() and weapon in WeaponNames.values():
				self.suggestion = name + ','+ weapon +','+ room
			else:
				self.suggestion = ''
				
		if choice == '3':
			self.approve_disprove = False
		if choice == '4':
			self.approve_disprove = True
				
	def move(self, direction):

		if direction == 'LEFT':
			self.x -= self.vel
			self.rect = (self.x, self.y, self.width, self.height)
			self.update()
			return self.x

		if direction == 'RIGHT':
			self.x += self.vel
			self.rect = (self.x, self.y, self.width, self.height)
			self.update()
			return self.x

		if direction == 'UP':
			self.y -= self.vel
			self.rect = (self.x, self.y, self.width, self.height)
			self.update()
			return self.y

		if direction == 'DOWN':
			self.y += self.vel
			self.rect = (self.x, self.y, self.width, self.height)
			self.update()
			return self.y

	def update(self):
		self.rect = (self.x, self.y, self.width, self.height)
	


