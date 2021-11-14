import socket
import os

def delete(request):
    headers = request.split('\n')
    filename = headers[0].split()[1]

    dir_path = './htdocs'
    file_path = f'{dir_path}/{file}'

    if os.path.exists(file_path):
        os.remove(file_path)
        response = 'HTTP/1.1 200 OK\n\n'
    else:
        response = 'HTTP/1.1 404 NOT FOUND\n\nFile Not Found'

return response
