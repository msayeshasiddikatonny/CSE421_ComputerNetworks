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
             vowels = "aeiouAEIOU"
             count =0
        for i in msg:
            if i in vowels:
                count+=1
        if count==0:
            conn.send("Not enough vowels".encode(FORMAT))
        elif count<3:
            conn.send("Enough vowels I guess".encode(FORMAT))
        else:
            conn.send("Too many vowels".encode(FORMAT))
conn.close()