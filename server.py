import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = socket.gethostbyname(socket.gethostname()), 9001
server.bind((host, port))
server.listen(4)
client_connected = True
socket_objs = [server]

print("Welcome to your chat!!")

while client_connected:

	list_read, write_access_list, exception = select.select(socket_objs, [], socket_objs)

	for socket_obj in list_read:

		if socket_obj is server:
			client, address = server.accept()
			print(f"the client socket object: {client} - address: {address}")
			socket_objs.append(client)

		else:
			data_received = socket_obj.recv(128).decode("utf-8")
			if data_received:
				print(data_received)
			else:
				socket_objs.remove(socket_obj)
				print("1 participant is disconnected")
				print(f"{len(socket_objs) - 1} remaining participants")