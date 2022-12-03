import socket

# fast communication between server and client on the same machine
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this retrieves the ip address of the pc and creates a port 9001
host, port = socket.gethostbyname(socket.gethostname()), 9001
# connects the client to the server
client_socket.connect((host, port))
name = input("What is your name ? ")
client_connected = True

while client_connected:

	message = input(f"{name} > ")
	client_socket.send(f"{name} > {message}".encode("utf-8"))