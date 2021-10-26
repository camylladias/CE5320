import socket

def handle_request(request):

    headers = request.split('\n')
    filename = headers[0].split()[1]
    if filename == '/':
        filename = '/projeto.html'

    try:
        fin = open('htdocs' + filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' + content

    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'



    return response


SERVER_HOST = "localhost"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(1)


print("Servidor em execução...")
print("Escutando por conexões na porta %s" % SERVER_PORT)


while True:
    # Aguarda conexão do cliente
    client_connection, client_address = server_socket.accept()

    # Função GET
    request = client_connection.recv(1024).decode()
    print(request)

    # Return an HTTP response
    response = handle_request(request)
    client_connection.sendall(response.encode())

    # Fecha conexão com o cliente
    client_connection.close()

    #fecha o servidor socket
    server_socket.close()


