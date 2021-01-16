import socket


PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))



send("hey server")
while True:
    more=input('Do you want to continue(y/n): ')
    if more.lower() =='y':
        payload= input('enter question: ')
        send(payload)
    else:
        send(DISCONNECT_MESSAGE)
        break
