from Tkinter import *
import threading


class Dashboard:
	def __init__(self):
		self.suggestion = ''
		self.player_name = ''

	def print_rule(self):
		top = Tk()
		top.geometry('100x100')
	



		suggestion_label = Label(top, text = "")
		inputUser = Entry(top)
		suggestion_label.pack()
		inputUser.pack()
		btn = Button(top, text = 'Make Suggestion', bd = '5', command = top.destroy)
		btn.pack(side = 'top')

		btn = Button(top, text = 'Approve Suggestion', bd = '5', command = top.destroy)
		btn.pack(side = 'top')
		btn = Button(top, text = 'Disprove Suggestion', bd = '5', command = top.destroy)
		btn.pack(side = 'top')
		btn = Button(top, text = 'Show Suggestion', bd = '5', command = top.destroy)
		btn.pack(side = 'top')

		top.mainloop()

	

	def user_input(self):
		self.thread1 = threading.Thread(target = self.print_rule(), args = (1,))
		self.thread1.start()

		#self.print_rule()

		#if self.input == '0':
			#self.suggestion = raw_input("Enter your suggestion: ")
			#self.player_name = raw_input("Enter your player name")
		#if self.input == '1':
			#return True
		#if self.input == '2':
			#return False
		#if self.input == '3':
			#print self.player_name + ' suggests that ' + self.suggestion


#D = Dashboard()
#D.user_input()


