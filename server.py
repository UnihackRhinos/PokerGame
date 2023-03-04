import socket
from _thread import *
import pickle
from game import Game

server = "118.138.23.2" # replace this with your ipv4 address to test, also replace in network.py
port = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gameData = Game() # create an instance of game called gameData, which contains all gamedata



try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

def threaded_client(conn, player):
    conn.send(pickle.dumps(player))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(1024*8))
            if not data:
                break
            else:
                if data == "reset":
                    pass ####NEED TO INITIALISE ALL VALUES
                elif data == "halfPotBet":
                    betsize = round(int(gameData.pot)/2)
                    gameData.betting(player,2,betsize)
                elif data == "fullPotBet":
                    betsize = int(gameData.pot)
                    gameData.betting(player,2,betsize)
                elif data == "allIn":
                    betsize = gameData.stack[player]
                    gameData.allin[player] = 1 # changing value in game object
                    gameData.betting(player,2,betsize)
                elif data == "check":
                    gameData.betting(player,1)
                elif data == "fold":
                    gameData.betting(player,3)
                elif data != "pull_request":
                    pass
    
            
            conn.sendall(pickle.dumps(gameData))
        except:
            break

    print("Lost connection")

    conn.close()


p=0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, p))
    if p == 1:
        gameData.connected = True
    p+=1

