from PyQt5 import QtWidgets
from  PyQt5.uic  import  loadUi
import sys
from chatbot import Ui_main
import socket


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow . __init__ ( self )
        loadUi ( "home.ui" , self )
        self.window= QtWidgets.QMainWindow()
        self.u= Ui_main()
        self.u.setupUi(self.window)
        self.u.textBrowser.append('<font color="#FF0000">Server: Hello! How can I help you!</font>')
        self.HOST = "192.168.56.1"
        self.PORT = 5050
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))
        self.u.pushButton.clicked.connect(self.buttonEvent)
        
    def open(self):
        self.window.show()
        
        
    def buttonEvent(self):
        text = self.u.textEdit.toPlainText()
        self.u.textEdit.clear()
        self.u.textBrowser.append('User: '+text)       
        self.client.send(text.encode())

        # Server message
        serverMessage = str(self.client.recv(1024), encoding='utf-8')
        self.u.textBrowser.append('<font color="#FF0000">Server: '+serverMessage+'</font>')
        if text == 'good bye':
            self.window.close()
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()