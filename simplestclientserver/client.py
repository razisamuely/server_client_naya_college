import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Connect to the server
client_socket.connect((host, port))

while True:
    # Get input from the user
    message = input("Enter your message ('quit' to exit): ")
    if message == 'quit':
        break

    # Send a message to the server
    client_socket.send(message.encode())

    # Receive the server's response
    modified_message = client_socket.recv(1024).decode()
    print("Received modified message from server: {}".format(modified_message))

# Close the socket
client_socket.close()
