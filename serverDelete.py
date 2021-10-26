import socket
import os

def delete(request):
    dir_path = ''
    envia = ''
    file = ''
    
    arquivos = os.listdir(dir_path)
    
    if len(arquivos) == 0:
        envia +="Pasta vazia."
        
    else:
        os.path.exists(dir_path/file)
        os.remove(dir_path/file)
    
    return 'delete'
