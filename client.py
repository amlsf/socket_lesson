import socket
import sys
import select 

# This is syntax to tell what type of socket connection, AF_INET: internet, SOCK_STREAM: streaming connection
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Establishes connection between application to connect to server listening on port 555 on local machine "local host" 
my_socket.connect(("localhost", 5555))

running = True
while running:
    # user_input = sys.stdin.readline()
    inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [], [])

    for s in inputready:
        if type(s) == type(my_socket):
            msg = s.recv(1024)
            print msg
        else:
            msg = s.readline()
            if msg == 'quit':
                print "Disconnected from server!"
                running = False
            # This writes user_input to my_socket handle (like a file)
            my_socket.sendall(msg)

        

# user_input = sys.stdin.readline()
# # This writes user_input to my_socket handle (like a file)
# my_socket.sendall(user_input)



# # TODO Receive 1024 bytes from the socket (connected to the server??) and displays
# # how write read parallels?
# # NOTE: two entities (client.py, chatserver.py) talking to each other via a socket that listens on a specific port on server (phone is socket , phone number is port)
# data = my_socket.recv(1024)
# print "received:\n%s" % data

# # This reads from the keyboard (like a file)
# user_input = sys.stdin.readline()
# # This writes user_input to my_socket handle (like a file)
# my_socket.sendall(user_input)

# #Receive 1024 bytes from server through the socket and displays them
# # NOTE: the way chat server py file written to send back what we send
# data = my_socket.recv(1024)
# print "received:\n%s" % data

my_socket.close()