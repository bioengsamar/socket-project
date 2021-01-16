from PyQt5 import QtWidgets
from  PyQt5.uic  import  loadUi
import sys
from chatbot import Ui_main
import socket

PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow . __init__ ( self )
        loadUi ( "home.ui" , self )
        self.window= QtWidgets.QMainWindow()
        self.u= Ui_main()
        self.u.setupUi(self.window)
        self.u.pushButton.clicked.connect(self.send_message)
        
    def open(self):
        self.window.show()
        msg ="hey server"
        self.send(msg)
        
    def send(self, msg):
        message = msg.encode(FORMAT)
        client.send(message)
        self.u.lineEdit_2.setText(client.recv(2048).decode(FORMAT))
        
    def send_message(self):
        more=self.u.lineEdit.text()
        self.send(more)
        print(more)
        if more == 'good bye':
            self.window.close()
            self.show()
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()