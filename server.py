import socket
import select

# # fast communication between server and client on the same machine
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this retrieves the ip address of the pc and creates a port 9001
host, port = socket.gethostbyname(socket.gethostname()), 9001
# Associate the IP address and the port number
server.bind((host, port))
# Listen for incoming connections, up to maximum 4 external connections
server.listen(4)
client_connected = True
# le socket_objs est definit sur le serveur
socket_objs = [server]

print("Welcome to your chat!!")

# Loop when the client is connected
while client_connected:
	# is used to manage multiple sources in a single process/thread
	list_read, write_access_list, exception = select.select(socket_objs, [], socket_objs)

	for socket_obj in list_read:

		if socket_obj is server:
			# accept connections from outside
			client, address = server.accept()
			print(f"the client socket object: {client} - address: {address}")
			# add client to socket_objs list
			socket_objs.append(client)

		else:
			# maximum number of bytes allowed (128)
			data_received = socket_obj.recv(128).decode("utf-8")
			if data_received:
				print(data_received)
			# disconnecting participants does not work
			elif data_received:
				# deletes socket_obj and displays socket_objs
				socket_objs.remove(socket_obj)
				print("1 participant is disconnected")
				print(f"{len(socket_objs) - 1} remaining participants")