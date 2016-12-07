from socket import *
from thread import *
import time
import socket
 
p=int(input("Enter Port\n"))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", p))
#client_socket.send("Hi From client")
print "Connected"
while True:
  person = raw_input('Enter your message: ')
  client_socket.send(str(person)+"\n")
