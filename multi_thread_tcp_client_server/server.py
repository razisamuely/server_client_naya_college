import socket
import threading

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            print(f"Connection from {client_address} has been closed.")
            break
        print(f"Received from {client_address}: {data.decode()}")
        client_socket.send(data)
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("The server is listening on port 12345...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
        print(f"Active connections: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
