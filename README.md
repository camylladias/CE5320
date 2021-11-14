# Projeto Servidor HTTP/1.1 - Disciplina CE5320 (FEI)

Neste projeto foi implementado um servidor HTTP/1.1 capaz de interpretar alguns comandos do protocolo HTTP recebidos por meio de solicitações de navegadores/clientes,
e responder de forma apropriada a essas requisições. 

Comandos implementados: GET, PUT, POST e DELETE.



#

### Integrantes:
| Alunos |  RA  |
| ------------------- | ------------------- |
| Milena Teixeira |   RA 222190118 |
| Camylla Dias    |  RA 222170052 |
| Yasmin Gomes     | RA 222190126 |
| Marcella Costa   | RA 221190234 |
| Matheus Queiroz  | RA 222190167 |

---
## GET
[ ... ]

## PUT
[ ... ]

## POST
[ ... ]

## DELETE 
*S.O utilizado em teste: Ubuntu 18.04 LTS*
 
 ### Entre na pasta do projeto
 ```
 cd ProjetoHttp-CE5320
 ```
 ![cd-projeto](https://user-images.githubusercontent.com/37374749/141695133-441a2ba3-ef9a-4dee-8f00-6c945e6e6061.PNG)
 
 ### Inicie o servidor
 ```
 python3 servidorHTTP.py
 ```
 ![servidorhttp-py](https://user-images.githubusercontent.com/37374749/141694960-a7e27ca2-af48-4621-a78e-d40a8fc9baea.PNG)
 
 ### Abra outro terminal e inicie a conexão
 ```
 telnet localhost 8080
 ```
 ![telnet](https://user-images.githubusercontent.com/37374749/141695163-42129e30-d6dc-46d6-8be6-ab82ec3abb4a.PNG)

 ### Comando DELETE
 ```
 DELETE /testessss.html 
 ```
 ![delete](https://user-images.githubusercontent.com/37374749/141695166-ca3b89ad-c2e2-492c-8351-ee78e80cf330.PNG)
 
  ### Comando DELETE (teste quando arquivo não existe)
 ```
 DELETE /testessss.html 
 ```
 ![delete-teste-404](https://user-images.githubusercontent.com/37374749/141695462-21889a93-eb37-472c-b8de-3ca4192a4223.PNG)

