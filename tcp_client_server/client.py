import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send data
    message = "Hello, server!"
    print("Sending:", message)
    client_socket.sendall(message.encode())

    # Receive response
    received_data = b""
    while True:
        data = client_socket.recv(16)
        if not data:
            print("Server closed the connection")
            break
        received_data += data

    print("Received:", received_data.decode())

finally:
    # Clean up the connection
    client_socket.close()

