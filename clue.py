import pygame
from Tkinter import *
import threading
import random

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

class Player():
    def __init__(self, x, y, width, height, color, accusation, suggestion, name, die_roll_value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 2
	self.player_name = ''
	self.text_variable = ''
	self.accusation = accusation
	self.suggestion = suggestion
	self.name = name
	self.die_roll_value = die_roll_value

    def draw(self, win):
	font = pygame.font.SysFont(None,25) # default font set at 21 points
	player_font = pygame.font.SysFont(None,50)

	pygame.draw.rect(win, self.color, self.rect)
	textobj = font.render(self.name, 1, BLACK)
	textrect = textobj.get_rect()
	textrect.topleft = (self.x, self.y)
	win.blit(textobj, textrect)
		
    def show_accusation_and_suggestion(self):
	keys = pygame.key.get_pressed()
	if keys[pygame.K_s]:
		if self.accusation != 'No accusation':
			print 'Accusation: ', self.accusation
		if self.suggestion != 'No suggestion':
			print 'Suggestion ', self.suggestion
		if self.die_roll_value:
			print ('{0} rolled a {1}'.format(self.name, self.die_roll_value))
    def make_accusation_and_suggestion(self):
	keys = pygame.key.get_pressed()
	if keys[pygame.K_f]:
		print '***************************'
		print '* 1 - Make Accusation     *'
		print '* 2 - Make Suggestion     *'
		print '* 3 - Disprove Accusation *'
		print '* 4 - Roll Dice           *'
		print '***************************'
		choice = raw_input('Enter choice: ')
		if choice == '1':	
			self.accusation = raw_input('Enter accusation: ')
		if choice == '2':
			self.suggestion = raw_input('Enter suggestion: ')
		if choice == '3':
			pass
		if choice == '4':
			self.die_roll_value = random.randint(0, 6)
			print 'You rolled a ' , self.die_roll_value


    def die_roll(self):
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_d]:
		self.die_roll_value = random.randint(0, 6)
		 
    
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
	
	#self.is_valid_move(3,4,6,11)
	#self.is_valid_move(3,4,16,21)


        self.rect = (self.x, self.y, self.width, self.height)
 	self.update()

    def update(self):
	self.rect = (self.x, self.y, self.width, self.height)
	


