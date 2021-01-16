import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "good bye"
thisdict = {
  "hi": "hi",
  "hello": "hey samar",
  "what is your name": "telemedicine",
  "hey server": "hey client"
}


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        #msg_length = conn.recv(HEADER).decode(FORMAT)
        #if msg_length:
            #msg_length = int(msg_length)
        
        msg = conn.recv(1024).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            conn.send("okay bye bye".encode(FORMAT))
            connected = False
            #break 
        
        print(f"[{addr}] {msg}")

        #if msg == 'what is your name':
            #conn.send("telemedicine".encode(FORMAT))
        #elif msg =='hi' or msg == 'Hi'or  msg == 'HI':
            #conn.send("hello samar".encode(FORMAT))
        #else:
        #if msg == 'Hey server':
            #conn.send("hey client".encode(FORMAT))
        if msg in thisdict:
            conn.send(thisdict.get(msg).encode(FORMAT))
        else:
            conn.send("not available".encode(FORMAT))
        

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()