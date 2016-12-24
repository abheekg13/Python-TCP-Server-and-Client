#Author: Abheek Gulati
#For: NJIT class CS 656

import socket

TCP_IP = '127.0.1.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024
MESSAGE = "Hello World!"

print "Sending data: ", MESSAGE

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data: ", data
