import socket
import pickle


#hostname = socket.gethostname()
#IPAddr = socket.gethostbyname(hostname)

class Network:
	def __init__(self, IPAddr, port_num):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = IPAddr		
		self.port = port_num
		self.addr = (self.server, self.port)
		self.p = self.connect()
		self.status = 0

	def getP(self):
		return self.p
		
	def connect(self):
		try:
			self.client.connect(self.addr)
			print "Connected to Server"
			self.status = 1
			return pickle.loads(self.client.recv(2048))
		except:
			#return False
			pass

	def send(self, data):
		try:
			self.client.send(pickle.dumps(data))
			return pickle.loads(self.client.recv(2048))
		except socket.error as e:
			print(e)
