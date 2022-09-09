import socket

SERVER_PORT = 12000
SERVER_ADDRESS = "localhost"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((SERVER_ADDRESS, SERVER_PORT))
print("The server is ready to receive")
while True:
    message, client_address = server.recvfrom(2048)
    modified_message = message.decode().upper()
    server.sendto(modified_message.encode(), client_address)