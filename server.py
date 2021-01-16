import socket 
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "good bye"
questuions = {
  "hello": "Hey Samar, I can help you if you're feeling unwell",
  "i have a headache": "I see. Would you mind answering a few questions about your head?",
  "sure": "okay let's start",
  "hi": "Hi again, Samar"
}


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        
        msg = conn.recv(1024).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            conn.send("okay bye bye".encode(FORMAT))
            connected = False
            
        
        print(f"[{addr}] {msg}")

        if msg in questuions:
            conn.send(questuions.get(msg).encode(FORMAT))
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