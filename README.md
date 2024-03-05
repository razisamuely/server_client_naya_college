# Python Client-Server Examples

This repository contains several examples of client-server implementations using Python's socket module. Each example demonstrates different aspects of network programming, including TCP and UDP protocols, and handling multiple clients with threading.


<p align="center">
  <img src="https://github.com/razisamuely/server_client_naya_college/blob/main/artifacts/server_client_gif.gif?raw=true" width="200" />
</p>


`
├── LICENSE
├── multi_thread_tcp_client_server
│   ├── client.py
│   └── server.py
├── simplest_tcp_client_server
│   ├── client.py
│   └── server.py
├── tcp_client_server
│   ├── client.py
│   └── server.py
└── udp_client_server
    ├── client.py
    └── server.py`

###  Simplest TCP Client-Server (simplest_tcp_client_server)
A basic example of a TCP client and server where the client sends a message, and the server echoes it back.

How to Run:
- Server: `python simplest_tcp_client_server/server.py`
- Client: `python simplest_tcp_client_server/client.py`



### TCP Client-Server (tcp_client_server)
A TCP client and server example with a bit more complexity, demonstrating sending and receiving larger amounts of data.

How to Run:
- Server: `python tcp_client_server/server.py`
- Client: `python tcp_client_server/client.py`


### UDP Client-Server (udp_client_server)
Illustrates the use of UDP protocol for sending and receiving messages between client and server.

How to Run:
- Server: python udp_client_server/server.py
- Client: python udp_client_server/client.py


### Multi-Threaded TCP Client-Server (multi_thread_tcp_client_server)
Demonstrates handling multiple clients simultaneously using threads in a TCP server.

How to Run:
- Server: python `multi_thread_tcp_client_server/server.py`
- Client: python `multi_thread_tcp_client_server/client.py` (Can be run in multiple terminals)

### How to Use
Clone this repository.
Navigate to the desired example directory.
Run the server script in one terminal window.
Run the client script in another terminal window.
