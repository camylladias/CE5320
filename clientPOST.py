import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverPort = 8080

clientSocket.connect(('localhost', serverPort))
print('Conectado ao servidor na porta {}.'.format(serverPort))
print("\nDiga 'oi' para continuar conectado.")

while True:
    req = input()

    clientSocket.send(req.encode())

    res = clientSocket.recv(1024).decode()
    print('\nDo servidor: {}'.format(res))

    if 'oi' not in req.lower().split():
        break
    else:
        req = input()
        
        if req != ' ':
            clientSocket.send(req.encode())

            res = clientSocket.recv(1024).decode()
            print('\nDo servidor: {}'.format(res))

            break
        else: break

clientSocket.close()
