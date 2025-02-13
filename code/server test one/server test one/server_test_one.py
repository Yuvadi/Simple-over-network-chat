import socket
from _thread import *

host = '192.168.104.202' 
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

def clientthread(conn, addr):

    name = conn.recv(1024).decode()

    print(f"Connected: {addr[0]} ({name})")

    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break
            
        print(f"[{addr[0]}:{addr[1]}] {name}: {msg}")
        conn.send("Msg received".encode())

    conn.close()

while True:
    conn, addr = server.accept()
    start_new_thread(clientthread,(conn,addr))

server.close()