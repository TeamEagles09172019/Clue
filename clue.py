import pygame
from Tkinter import *
import threading

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
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 1
	self.suggestion = ''
	self.player_name = ''
	self.text_variable = ''

    def draw(self, win):
	pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
	    print "moving left"
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            print "moving right"
            self.x += self.vel

        if keys[pygame.K_UP]:
	    print "moving up"
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
	    print "moving down"
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)
 	self.update()

    def update(self):
	self.rect = (self.x, self.y, self.width, self.height)
	
    def Show_accusation_callback(self):
	global inputUser4
	print 'printing show accusation ', inputUser4
	inputUser4.insert(END, text_variable.get())
	

    def Make_accusation_callback(self):
	#print 'Printing text', text_variable.get()
	self.text_variable = text_variable.get()
	print self.text_variable

        
	
    def print_rule(self):
		top = Tk()
		top.geometry('300x500')

		
		Accusation_label = Label(top, text = "")
		Accusation_label.pack()
		global text_variable
		text_variable = StringVar()
		inputUser = Entry(top, textvariable=text_variable)
		inputUser.pack()
		
		
		
		Make_accusation = Button(top, text = 'Make accusation', bd = '5', command = 	self.Make_accusation_callback)
		Make_accusation.pack(side = 'top')
		

		suggestion_label = Label(top, text = "")
		inputUser_1 = Entry(top)
		suggestion_label.pack()
		inputUser_1.pack()

		Make_suggestion = Button(top, text = 'Make Suggestion', bd = '5', command = top.destroy)
		Make_suggestion.pack(side = 'top')

		Approve_Accusation = Button(top, text = 'Approve Accusation', bd = '5', command = top.destroy)
		Approve_Accusation.pack(side = 'top')
		Disprove_Suggestion = Button(top, text = 'Disprove Accusation', bd = '5', command = top.destroy)
		Disprove_Suggestion.pack(side = 'top')

		Show_Suggestion_label = Label(top, text = "")
		inputUser3 = Entry(top)
		Show_Suggestion_label.pack()
		inputUser3.pack()
		Show_Suggestion = Button(top, text = 'Show Suggestion', bd = '5', command = top.destroy)
		Show_Suggestion.pack(side = 'top')

                global Show_Accusation_label
		Show_Accusation_label = Label(top, text = "")
		global inputUser4
		inputUser4 = Entry(top)
		Show_Accusation_label.pack()
	
		inputUser4.pack()
		Show_Accusation = Button(top, text = 'Show Accusation', bd = '5', command = self.Show_accusation_callback)
		Show_Accusation.pack(side = 'top')

		top.mainloop()

    def user_input(self):
		#self.thread1 = threading.Thread(target = self.print_rule(), args = (1,))
		#self.thread1.start()

		self.print_rule()

		#if self.input == '0':
			#self.suggestion = raw_input("Enter your suggestion: ")
			#self.player_name = raw_input("Enter your player name")
		#if self.input == '1':
			#return True
		#if self.input == '2':
			#return False
		#if self.input == '3':
			#print self.player_name + ' suggests that ' + self.suggestion


