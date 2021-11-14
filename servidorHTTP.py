import socket
import os

def get(request):
    headers = request.split('\n')
    filename = headers[0].split()[1]

    if filename == '/':
        filename = 'projeto.html'

    if '=' in filename:
        index = filename.index("=") + 1
        filename = filename[index:]

    try:
        fin = open('htdocs/' + filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.1 200 OK\n\n' + content

    except (FileNotFoundError, OSError):
        response = 'HTTP/1.1 404 NOT FOUND\n\nFile Not Found'

    return response

def post(request):
    requestlist = request.split('\r\n')

    header = requestlist[0].split(' ')
    file = header[1][1:]

    content = requestlist[5]

    try:
        with open(f'./htdocs/%s'%file, 'a') as f:
            f.write(content)
        response = 'OK'

    except FileNotFoundError:
        with open(f'./htdocs/%s'%file, 'w') as f:
            f.write(content)
            response = 'NOK'

    return response

def put(request):
    requestlist = request.split('\r\n')

    header = requestlist[0].split(' ')
    file = header[1][1:]

    content = requestlist[5]

    try:
        with open(f'./htdocs/{file}') as f: 
            actual_content = f.read()

        if content == actual_content:
            response = f'\nHTTP/1.1 204 No Content\nContent-Location: /{file}\n'
        else:
            with open(f'./htdocs/{file}', 'w') as f:
                f.write(content) 
                response = f'\nHTTP/1.1 200 OK\nContent-Location: /{file}\n'
    except (FileNotFoundError, OSError):
        with open(f'./htdocs/{file}', 'w') as f:
            f.write(content)

        response = f'\nHTTP/1.1 201 Created\nContent-Location: /{file}\n'
    except (IndexError, UnicodeDecodeError):
        response = f'\nHTTP/1.1 400 Bad Request\n'

    return response

def delete(request):
    headers = request.split('\n')
    file = headers[0].split()[1]

    dir_path = './htdocs'
    file_path = f'{dir_path}/{file}'

    if os.path.exists(file_path):
        os.remove(file_path)
        response = '\nHTTP/1.1 200 OK\n\n'
    else:
        response = '\nHTTP/1.1 404 NOT FOUND\n\nFile Not Found'

    return response

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
    request = ''

    for _ in range(6):
        request += client_connection.recv(1024).decode()
        method = request.split("\n")[0].split(" ")[0]

        if method in ['GET', 'DELETE']:
            break

    if method == 'GET':
        response = get(request)
    elif method == 'POST':
        response = post(request)
    elif method == 'PUT':
        response = put(request)
    else:
        response = delete(request)

    client_connection.sendall(response.encode())
    client_connection.close()