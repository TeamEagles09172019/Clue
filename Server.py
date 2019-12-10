import socket
from thread import *
from clue import Player
from Dashboard import Dashboard
import pickle
from Deck import Deck

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
server = IPAddr
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(2)
print("Waiting for a connection, Server Started")

offset = (30 + 1)
 

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                #print("Received: Threaded_client(conn, player) ", data)
                #print("Sending : Threaded_client(conn, player)", reply)
			
		
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

NoP = 2
D = Deck()
DC = D.DistributeCards(NoP)
#for i in range(NoP):
#    print('Player ' + str(i) + ' cards: ', ', '.join(DC[i]))
    
players = [Player(103,103,30,30,(255,0,0),'No accusation', 'No suggestion','0.0.0.0',5555, 'Study',DC[0]), Player(9 * offset,3 * offset,31,31, (0,0,255), 'No accusation', 'No suggestion','0.0.0.0',5556,'Ballroom',DC[1])] #objects

currentPlayer = 0
while True:
    conn, addr = s.accept()

    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
