import socket

SERVER_NAME = "localhost"
SERVER_PORT = 1234
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((SERVER_NAME, SERVER_PORT))
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.listen(1)
    print("The server is ready to recieve.")

    while True:
        #accept() creates a new socket for communicating with client
        conn_socket, addr = server.accept()
        print("accepted connection from", addr)
        message = conn_socket.recv(BUFFER_SIZE).decode()

        modified_message = message.upper()
        conn_socket.send(modified_message.encode())
        conn_socket.close()


