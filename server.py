import socket

import threading

# this retrieves the ip address of the pc and connects to port 9001
# if we change it to the ipv4(SERVER) address of a chat server, everyone can connect to the chat
PORT = 9001
SERVER = socket.gethostbyname(socket.gethostname())

# Address is stored as a tuple
ADDRESS = (SERVER, PORT)

# encoding and decoding will occur
FORMAT = "utf-8"

# Lists that will contain all the clients connected to the server and their names.
clients, names = [], []

# Fast communication between server and client
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the address of the server to the socket
server.bind(ADDRESS)


# start the connection
def startChat():
    print("server is working on " + SERVER)

    # listening for connections
    server.listen()

    while True:
        # accept connections and returns a new connection to the client
        conn, addr = server.accept()
        conn.send("NAME".encode(FORMAT))

        # 1024 represents the max amount of data that can be received (bytes)
        name = conn.recv(1024).decode(FORMAT)

        # append the name and client to the respective list
        names.append(name)
        clients.append(conn)

        print(f"Name is :{name}")

        # broadcast message
        broadcastMessage(f"{name} has joined the chat! ".encode(FORMAT))

        conn.send('Connection successful!'.encode(FORMAT))

        # Start the handling thread
        thread = threading.Thread(target=handle,
                                  args=(conn, addr))
        thread.start()

        # Number of clients connected to the server
        print(f"active connections {threading.activeCount() - 1}")


# method to handle the incoming messages
def handle(conn, addr):
    print(f"new connection {addr}")
    connected = True

    while connected:
        # receive message
        message = conn.recv(1024)

        # broadcast message
        broadcastMessage(message)

    # close the connection
    conn.close()


# Method of broadcasting messages to each client
def broadcastMessage(message):
    for client in clients:
        client.send(message)


# call the 'startChat()' to begin the communication
startChat()
