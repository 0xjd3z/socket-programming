import socket

SERVER_NAME = "localhost"
SERVER_PORT = 12000
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Input your message: ")
client.sendto(message.encode(), (SERVER_NAME, SERVER_PORT))

modified_message, server_address = client.recvfrom(BUFFER_SIZE)
print(modified_message.decode())
client.close()