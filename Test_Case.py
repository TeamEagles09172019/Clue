from network import Network
from clue import Player

class Test_Server_Connection:
    def __init__(self, SERVER_IP, PORT):
    	self.server = SERVER_IP
    	self.port = PORT
    	
    def connection(self):
    	n = Network(self.server, self.port)
    	if n.p is None:
    		print 'connect_to_server: FAILED'
    	else:
    		print 'connect_to_server: PASSED'
    		

class Test_Suggestion:
	def __init__(self, x, y, width, height, color, accusation, suggestion, ipAddr, port):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.rect = (x,y,width,height)
		self.vel = 2
		self.accusation = accusation
		self.suggestion = suggestion
		self.name = 'Derrick'
		self.approve_disprove = ''
		self.ip = ipAddr
		self.port = port
		
	def sugg(self):
		p = Player(self.x, self.y, self.width, self.height, self.color, self.accusation, self.suggestion, self.ip, self.port)
		p.make_accusation_and_suggestion(0,0,'2')
		if p.suggestion != '':
			print 'Making Suggestion: PASSED'
		else:
			print 'Making Suggestion: FAILED'
			
class Test_Accusation(Test_Suggestion):
	def acc(self):
		p = Player(self.x, self.y, self.width, self.height, self.color, self.accusation, self.suggestion, self.ip, self.port)
		p.make_accusation_and_suggestion(0,0,'1') 
		if p.accusation != '':
			print 'Making Accusation: PASSED'
		else:
			print 'Making Accusation: FAILED'
		

        