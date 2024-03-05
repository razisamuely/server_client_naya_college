import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ('localhost', 12345)

try:
    while True:
        # Prompt the user for input
        message = input("Enter your message ('quit' to exit): ")
        if message == 'quit':
            break

        # Send message to server
        print("Sending:", message)
        client_socket.sendto(message.encode(), server_address)

        # Receive response from server
        data, _ = client_socket.recvfrom(4096)
        print("Received:", data.decode())

finally:
    # Clean up the connection
    client_socket.close()
