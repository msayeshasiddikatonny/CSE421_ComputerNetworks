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
              msg=int(msg)

        if msg<41:
            x=str(msg*200)+' taka'
            conn.send(x.encode(FORMAT))
        elif msg>40:
            x=8000+(msg-40)*300
            x=str(x)+' taka'
            conn.send(x.encode(FORMAT))

conn.close()