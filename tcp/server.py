import socket

SERVER_NAME = "localhost"
SERVER_PORT = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_NAME, SERVER_PORT))
server.listen(1)
print("The server is ready to recieve.")

while True:
    #accept() creates a new socket for communicating with client
    conn_socket, addr = server.accept()
    print("accepted connection from", addr)
    message = conn_socket.recv(1024).decode()

    modified_message = message.upper()
    conn_socket.send(modified_message.encode())
    conn_socket.close()


