import socket
import os

def get(request):
    print(request)

def post(request):
    print(request)

def put(request):
    file = request.split(' ')[1]
    
    if '/' in file:
        file = file[1:]

    isFile = os.path.isfile('./htdocs/%s' %(file))

    if (isFile):
        return 'updated'
    else:
        return 'not existing file'

def delete(request):
    return 'delete'


SERVER_HOST = ""
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(1)

print("Servidor em execucao...")
print("Escutando por conexoes na porta %s" % SERVER_PORT)

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()

    if request:
        headers = request.split("\n")
        method = headers[0].split(" ")[0]

        if method == 'GET':
            response = get(request)
        elif method == 'POST':
            response = post(request)
        elif method == 'PUT':
            response = put(request)
            print(response)
        else:
            response = delete(request)

        #client_connection.sendall(response.encode())

        #client_connection.close()
    else:
        client_connection.close()