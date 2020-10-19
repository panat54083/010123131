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

class MainChat(QtWidgets.QMainWindow, Ui_MainWindow2):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.Send.clicked.connect(self.send_message)
    def send_message(self):
        print("EIEI")
        # try:
        #     message = self.TypeHere.textStatus.text()
        #     print(message)
        #     message = message.encode('utf-8')
        #     message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        #     client_socket.send(message_header + message)
        #     self.TypeHere.clear()

        # except:
        #     print("Send Error")

class ChatWin(QtWidgets.QMainWindow, Ui_MainWindow1):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        
        self.connectButton.clicked.connect(self.send_name)
        # self.Send.clicked.connect(self.send_message)

    
    def send_name(self):
        try:
            # get name
            my_username = self.InputUser.text()

            # encode name tp bythes
            username = my_username.encode('utf-8')
            username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(username_header + username)
            self.hide()
            # self.displayText.appendPlainText(text)

        except:
            print("Error name")
    
    def send_message(self):
        try:
            message = self.TypeHere.textStatus.text()
            print(message)
            message = message.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)
            self.TypeHere.clear()

        except:
            pass

class ClientThread(Thread):
    def __init__(self,MainChat): 
        Thread.__init__(self) 
        self.MainChat = MainChat

    def run(self): 
        IP = "127.0.0.1"
        PORT = 1234
        HEADER_LENGTH = 10 
        global client_socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))
        client_socket.setblocking(False)
        
        try:
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

                MainChat.textBrowser_2.textStatus.setText(f'{username} > {message}')

            client_socket.close()
        except IOError as e:
            # This is normal on non blocking connections - when there are no incoming data error is going to be raised
            # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
            # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
            # If we got different error code - something happened
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()

        except Exception as e:
            # Any other exception - something happened, exit
            print('Reading error: '.format(str(e)))
            sys.exit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SW_Chat = QtWidgets.QMainWindow()

    ui = ChatWin()
    clientThread=ClientThread(ui)
    clientThread.start()
    # ui.exec()
    sys.exit(app.exec_())