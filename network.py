#importing socket library
import socket
#opening nad creating a socket inyour computer
mysoc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#trying to connect to web server where 80 is port number and it decide which part of web server to access largely 80 is for web pages  
mysoc.connect(('data.pr4e.org',80))
#writing command to get data (get request)
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#sending command
mysoc.send(cmd)
#printing data (recieved data)
while True :
    data=mysoc.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysoc.close()

