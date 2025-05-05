import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Send data to the server
message = "Hello, Server!"
client_socket.send(message.encode())

# Receive response from the server
response = client_socket.recv(1024).decode()
print(f"Server response: {response}")

# Close the socket
client_socket.close()
