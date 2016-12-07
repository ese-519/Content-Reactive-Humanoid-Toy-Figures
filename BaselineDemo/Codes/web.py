from socket import *
from thread import *
import time
import socket
 
p=int(input("Enter Port\n"))
port=p+1

dc={}
ct=0

def sendToAll(data):
   for i, sock in dc.items():
      add=dc[i]
      add.send(str(data)+"\n")
   return  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", p))
#client_socket.send("Hi From server")
print "Connected"

def service_connections(conn) :
    data = conn.recv(512)
    dataToSend=""
    if(data!=""):
    	print "RECIEVED @ web:" , data
        if "RHandUP" in data:
    		  dataToSend="servo right angle 180"
        if "RHandMID" in data:
    		  dataToSend="servo right angle 90"
	if "RHandDOWN" in data:
    		  dataToSend="servo right angle 0"
	if "LHandUP" in data:
    		 dataToSend="servo left angle 180"
	if "LHandMID" in data:
    		  dataToSend="servo left angle 90"
	if "LHandDOWN" in data:
    		  dataToSend="servo left angle 0"
	if "VideoChange" in data:
    		  dataToSend="/home/sarath/Desktop/ESE519/1_3.mp4"
        client_socket.send(dataToSend)
        conn.send(str(dataToSend)+"\n")
	sendToAll(dataToSend)

def clientthread(conn):
     while True:
          service_connections(conn) 

while 1:
    host = ''  
    print "Server(Web) waiting on port ", port

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5) 
    
    while True:
      conn, addr = sock.accept()
      #conn.send(str("Hello2\n"))
      start_new_thread(clientthread,(conn,))
      dc[ct]=conn
      ct=ct+1
      #if(data!=""):
     	#print "RECIEVED at web:" , data
        #client_socket.send(data)
 
conn.close()
sock.close()
