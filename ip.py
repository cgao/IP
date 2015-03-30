import socket
import os
from time import strftime

myIP=socket.gethostbyname(socket.gethostname())
time=strftime("updated at %Y-%m-%d %H:%M:%S")

f=open('myIP.txt','w')
f.write(myIP+'\n')
f.write(time+'\n')
f.close()
