import socket
from _thread import *
import pickle
from game import Game

server = "118.138.91.21" # replace this with your ipv4 address to test, also replace in network.py
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
                    gameData.reset()
                elif data == "preflop":
                    if not gameData.handstarted:
                        gameData.handstarted = True # changing value in game object
                        gameData.blinds(player)
                        gameData.deal()
                        print("Hand dealt")
                        print(gameData.hand)
                elif data == "halfPotBet":
                    betsize = round(int(gameData.pot)/2)
                    gameData.betting(player,2,betsize)
                elif data == "fullPotBet":
                    betsize = int(gameData.pot)
                    print(betsize)
                    gameData.betting(player,2,betsize)
                    print(gameData.num_of_actions)



                elif data == "allIn":
                    betsize = gameData.stack[player]
                    gameData.allin[player] = 1 # changing value in game object
                    gameData.stack[player] = 0 # changing value in game object remove later
                    gameData.betting(player,2,betsize)
                    print("gone all in (coolface)")
                elif data == "check":
                    gameData.betting(player,1)
                elif data == "fold":
                    gameData.betting(player,3)
                elif data == "flop":
                    if not gameData.flopstarted:
                        gameData.flop()
                
                elif data == "turn":
                    if not gameData.turnstarted:
                        gameData.turn()
                        
                elif data == "river":
                    if not gameData.riverstarted:
                        gameData.river()


                elif data == "winner":
                    if not gameData.winnerchecked:
                        gameData.FindWinner(gameData.BestHand(gameData.hand[0],gameData.runout),gameData.BestHand(gameData.hand[1],gameData.runout))
                
                
                elif data != "pull_request":
                    pass
    
            conn.sendall(pickle.dumps(gameData))
        except:
            print("something went wrong")
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
