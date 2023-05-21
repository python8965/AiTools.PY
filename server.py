from socket import *

PORT = 22333

serverSock = socket(AF_INET, SOCK_STREAM)

serverSock.bind(('', PORT))
serverSock.listen(1)
connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속이 확인되었습니다.')

while True:
    data = connectionSock.recv(1024)