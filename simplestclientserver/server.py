import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Bind to the port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

while True:
    # Accept a new connection
    client_socket, addr = server_socket.accept()
    print("Connection from {}".format(addr))

    while True:
        # Receive data from the client (1024 maximum bytes)
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print("Received message from client: {}".format(data))

        # Modify the message (e.g., echo it back in uppercase as confirmation)
        modified_data = data.upper()
        
        # Send the modified message back to the client
        client_socket.send(modified_data.encode())

    # Close the connection with the client
    client_socket.close()

# Optionally, you might want to close the server socket if it ever exits the loop
server_socket.close()
