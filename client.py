import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = socket.gethostbyname(socket.gethostname()), 9001
client_socket.connect((host, port))
name = input("What is your name ? ")

while True:

	message = input(f"{name} > ")
	client_socket.send(f"{name} > {message}".encode("utf-8"))