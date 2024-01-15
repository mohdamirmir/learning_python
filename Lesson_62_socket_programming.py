#Lesson:62 -  socket programming
'''
server has an ip address/domain name
every service has different port number

TCP - connection oriented protocol
UDP - connectionless protocol


'''
import socket

s = socket.socket()
print('socket created')

s.bind(('localhost',9999))

s.listen(3)
print('waiting for connections')

while True:
    c,addr = s.accept()
    name=c.recv(1024).decode()
    print("connected with", addr,name)
    c.send(bytes('welcome to telusco','utf-8'))
    c.close()