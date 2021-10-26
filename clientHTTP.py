from socket import *

serverName = ""
serverPort = 8080

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input('')

clientSocket.send(message.encode())
