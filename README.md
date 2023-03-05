# PokerGame

This project uses pygame, which must be installed to run the game.

To operate this game, both players will need to be connected to the same local network. For the machine that you wish to operate the server, you will need to edit the IP address in both the server.py and network.py files to your IPV4 address (found using ipconfig). Each client will need to change the IP address in their own network.py file. 

You must run server.py first.

Then each client can run client.py to join. (For testing purposes, server.py and two instances of client.py can all be run on the same machine, as they will still communicate over the local network).
