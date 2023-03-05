import socket
from _thread import *
import pickle
from game import Game
from time import sleep

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
    while gameData.connected:
        try:
            data = pickle.loads(conn.recv(1024*8))
            if not data:
                break
            else:
                if data == "reset":
                    # gameData.reset()
                    gameData.betting_round = 0
                    gameData.allin = [0, 0]
                    gameData.deck = gameData.Deck().cards
                    gameData.runout = []
                    gameData.hand = [[], []]
                    gameData.handstarted = False
                    gameData.flopstarted = False
                    gameData.turnstarted = False
                    gameData.riverstarted = False
                    gameData.num_of_actions = [0, 0]
                    gameData.winnerchecked = False
                    #gameData.position = [(gameData.postion[0] + 1) % 2, (gameData.postion[1] + 1) % 2 ]  # who is in position???
                    gameData.pot = 0
                    gameData.hand_over = False
                    # gameData.committed = 0
                    # gameData.owed = [0, 0]
                    #sleep(0.5)
                elif data == "preflop":
                    if not gameData.handstarted:
                        gameData.handstarted = True # changing value in game object
                        gameData.blinds(player)
                        gameData.deal()
                elif data == "halfPotBet":
                    betsize = round(int(gameData.pot)/2)
                    gameData.betting(player,2,betsize)
                elif data == "fullPotBet":
                    betsize = int(gameData.pot)
                    gameData.betting(player,2,betsize)



                elif data == "allIn":
                    betsize = gameData.stack[player]
                    gameData.allin[player] = 1 # changing value in game object
                    gameData.stack[player] = 0 # changing value in game object remove later
                    gameData.betting(player,2,betsize)
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
