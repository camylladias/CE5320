import socket
import datetime


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverPort = 8080

serverSocket.bind(('', serverPort))
serverSocket.listen(True)

print('Servidor inicializado.')

while True:
    try:
        connectionSocket, addr = serverSocket.accept()

        print('\nCliente {} conectado ao servidor.'.format(addr))

        req = connectionSocket.recv(1024).decode()

        print('\nDo cliente: {}'.format(req))

        if 'oi' in req.lower().split():
            res = "Olá!\n\nDigite algo."
        else:
            res = 'Tchau!'
        
        connectionSocket.send(res.encode())

        req = connectionSocket.recv(1024).decode()

        print('\nDo cliente: {}'.format(req))

        if req != ' ':
            arquivo = open('{}.txt'.format(addr), 'w')
            arquivo.write(req)
            arquivo.close()
            res = ('FEITO \n Digite continuar para realizar mais postagens ou sair para finalizar.')
        else:
            res = 'Tchau!'
        
        connectionSocket.send(res.encode())


        connectionSocket.close()
    except Exception:
        connectionSocket.close()
