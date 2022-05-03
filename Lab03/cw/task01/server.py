import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT  = 'utf-8'
DISCONNECT_MESSAGE ='END'

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print("Server is listening to you")
conn, addr = server.accept()
connected = True
while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length=int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            conn.send("good bye".encode(FORMAT))
        else:
            print(msg)
            conn.send("Message Received".encode(FORMAT))

conn.close()

