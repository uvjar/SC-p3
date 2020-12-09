import socket
import time
import os
import json

UDP_BCAST_PORT=33100
bufsize = 8192 

sockr = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sockr.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sockr.bind(('',UDP_BCAST_PORT))


def dsrc_receiver():
    global sockr
    try:
        print ('start service ...')
        while True :
            message, from_  = sockr.recvfrom(bufsize)
            if(message == ''):
                print ('pipe broken')
                sockr.close()
                return
            else :
                print(message)	

    except Exception as err:
        print('exception in comm::receiver()'  , err)
                
if __name__ == "__main__" :
    os.system('clear') 
    dsrc_receiver()
