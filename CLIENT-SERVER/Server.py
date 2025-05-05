# server.py
import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on port 12345...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to: {client_address}")

# Receive data from the client
data = client_socket.recv(1024).decode()
print(f"Received from client: {data}")

# Send a response back to the client
response = "Hello, Client!"
client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
