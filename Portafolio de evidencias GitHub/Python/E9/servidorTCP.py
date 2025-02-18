import argparse
import socket
from cryptography.fernet import Fernet
#Datos de conexion
TCP_IP = '127.0.0.1'
TCP_PORT = 5005 #se puede poner otro
BUFFER_SIZE = 2048
#Creación de objeto socket para abrir coneción

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    #parametro socket_family necesita ser indicado aun enviando la ip y el puerto a socket_tcp
    socket_tcp.bind((TCP_IP, TCP_PORT))
    socket_tcp.listen(1)
    #aqui, addr no va abajo de
    (Connec, addr) = socket_tcp.accept()
    print('Dirección con la que se hace conexión:', addr)
    while True:
        print('Conexión establecida uwu')
        msj_cifr = Connec.recv(BUFFER_SIZE)
        Connec.send(b"Adios :O")
        break
    Connec.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
(conn, addr) = s.accept()
print ('Direccion de conexion:', addr)
while True:
    msj_cifrado = conn.recv(BUFFER_SIZE)
    conn.send(b"o.O")
    break
conn.close()

file = open('clave.key', 'rb')
clave = file.read()
file.close()
cipher_suite = Fernet(clave)
Msj_Bytes = cipher_suite.decrypt(msj_cifrado,None)
msj = Msj_Bytes.decode()
print("El mensaje recibido fue el siguiente:",msj)
