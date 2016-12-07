from socket import *
from thread import *
import time
import socket

file = open('filename.txt', 'r')

for line in file:
    print line,

p=int(input("Enter Port\n"))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.43.34", p))
#client_socket.send("Hi From client")
print "Connected"
while True:
  person = raw_input('Enter your message: ')
  client_socket.send(str(person))
