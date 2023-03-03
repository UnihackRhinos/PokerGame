import socket
from _thread import *
import pickle
#from Game import some shizzle

server = "118.138.196.207" # replace this with your ipv4 address to test, also replace in network.py
port = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
                    print("data says reset")
                elif data != "get":
                    print("some thing happen :?")
                    
                
                print("Received:", data)
                print("Responding with:", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")

    conn.close()


p=0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, p))
    p+=1
