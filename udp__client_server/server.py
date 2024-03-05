import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("Server listening on {}:{}".format(*server_address))

while True:
    print("Waiting for a message...")
    # Receive message and address from client
    data, client_address = server_socket.recvfrom(4096)

    print("Received message:", data.decode())

    # Echo message back to client
    server_socket.sendto(data, client_address)

