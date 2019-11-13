import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.185"
	
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
	#self.accusation = self.connect()
	#self.suggestion = self.connect()


    def getP(self):
        return self.p

    def get_accusation(self):
	return self.accusation

    def get_suggestion(self):
	return self.suggestion

    def connect(self):
        try:
            self.client.connect(self.addr)
	    print "Connected to Server"
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
