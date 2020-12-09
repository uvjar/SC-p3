import os
import time
import socket
import json

UDP_IP = '10.35.70.38'
UDP_PORT=33100

os.system('clear') 
 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)  
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 

message=""
pckcnt=0
try:
  while True:
    msg_py = "HELLO "+str(pckcnt)
    message=json.dumps(msg_py).encode('utf-8')   

    sock.sendto(message, (UDP_IP,UDP_PORT))
    print(msg_py,UDP_IP,UDP_PORT)
    pckcnt = pckcnt +1    
    time.sleep(5)
 
except (KeyboardInterrupt, SystemExit): 
  print( "\nKilling Thread...")
  print( "Done.\nExiting.")