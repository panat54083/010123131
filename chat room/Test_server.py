import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234
# Initially setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This modifies the socket to allow us to reuse the address
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind and listen
server_socket.bind((IP, PORT))
server_socket.listen()
# begin clients
sockets_list = [server_socket]
clients = {}

print(f'Listening for connections on {IP}:{PORT}...')

def receive_message(client_socket):
    try :
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header): #if clients close a connecttion gracfully
            return False

        message_length = int(message_header.decode("utf-8").strip())
        # return data
        return {'header': message_header, 'data':client_socket.recv(message_length)}
    except:
        #if clients losed connection violently
        return False

while True:

    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    
    for notified_socket in read_sockets:

        # If notified socket is a server socket - new connection, accept it
        if notified_socket == server_socket:
            # th eorder returned object is ip/port set
            client_socket, client_address = server_socket.accept()

            # for clients send his name
            user = receive_message(client_socket)

            # if client disconnected before he sent his name
            if user is False:
                continue

            # Add clients to list
            socket_list.append(client_socket)

            #save name {ip : name}
            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
    
    else: #if existing socket

        message = receive_message(notified_socket) # revice message

        if message is False: #if client disconnected, clean up
            print("Closed connecttiob from: {}".format(clients[notified_socket['data'].decode('utf-8')]))

            # Remove from list for socket.socket()
            sockets_list.remove(notified_socket)

            # Remove from our list of users
            del clients[notified_socket]

            continue

     # Get user by notified socket, so we will know who sent the message
        user = clients[notified_socket]

        print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
        for client_socket in clients:

                # But don't sent it to sender
                if client_socket != notified_socket:

                    # Send user and message (both with their headers)
                    # We are reusing here message header sent by sender, and saved username header send by user when he connected
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    # It's not really necessary to have this, but will handle some socket exceptions just in case
    for notified_socket in exception_sockets:

        # Remove from list for socket.socket()
        sockets_list.remove(notified_socket)

        # Remove from our list of users
        del clients[notified_socket]
    
