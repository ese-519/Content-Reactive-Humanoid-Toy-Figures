import socket 
import time  
import thread
import threading
from thread import *

port=int(input("Enter port\n"))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", port))
server_socket.listen(5)

def service_servos(data):
	if "right" in data:
		if "angle" in data:
			command = data.split()    
    	        	import rhservo
    			rhservo.angle(command[3])
        	if "center" in data: 
    			import rhservo
    			servo.center()
    		if "stop" in data: 
    			import rhservo
    			servo.stop()

	if "left" in data:
		if "angle" in data: 
			command = data.split()  
    			import lhservo
    			lhservo.angle(command[3]) 
    		if "center" in data: 
    			import lhservo 
    			servo.center()
    		if "stop" in data: 
    			import lhservo
    			servo.stop()

while 1:
	print "Drivers Running....."
	client_socket, address = server_socket.accept()
	while 1:
	  data = client_socket.recv(512)
	  if(data != "") :  
	    print "Received @ Driver :" , data
	    if "servo" in data: 
		start_new_thread(service_servos,(data,))
    		#service_servos(data)
