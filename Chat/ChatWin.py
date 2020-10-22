from PyQt5 import QtWidgets

from SW import Ui_MainWindow1
from SW2 import Ui_MainWindow2

import socket
import select
import errno
from threading import Thread 


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234
client_socket = None
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

class ChatWin(QtWidgets.QMainWindow, Ui_MainWindow1):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.connectButton.clicked.connect(self.send_name)

    def send_name(self):
        
        try:
            # get name
            my_username = self.InputUser.text()

            # encode name tp bythes
            username = my_username.encode('utf-8')
            username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(username_header + username)
            # opne secound part
            self.hide()
            ui2.show()
            #  set name at scound part
            ui2.Usernamedisplay.setText(my_username)

        except:
            print("Error at sendding name part")

class MainChat(QtWidgets.QMainWindow, Ui_MainWindow2):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.Send.clicked.connect(self.send_message)
    def send_message(self):
        
        # show message on display
        username = self.Usernamedisplay.toPlainText()
        message = self.TypeHere.toPlainText()
        self.showText.append(username + ": "+ message)
        # send message to socket
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
        
        self.TypeHere.clear()


class ClientThread(Thread):
    
    def __init__(self,Chatwin): 
        Thread.__init__(self) 
        self.chat = ChatWin
        self.main = MainChat
        # self.main.hide()
    def run(self): 
        IP = "127.0.0.1"
        PORT = 1234
        HEADER_LENGTH = 10 
        global client_socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))
        client_socket.setblocking(1)
        
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            
            # Receive and decode username
            username = client_socket.recv(username_length).decode('utf-8')
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            # send message
            text = f'{username} : {message}'
            print(text)
            ui2.showText.append(text)

        client_socket.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SW_Chat = QtWidgets.QMainWindow()

    ui2 = MainChat()
    ui2.close()
    ui = ChatWin()

    clientThread = ClientThread(ui2)
    clientThread.start()
    
    sys.exit(app.exec_())
