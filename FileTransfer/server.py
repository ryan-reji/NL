import socket
import os

def start_server(host='127.0.0.1', port=12345, output_dir='received_files'):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    while True:
        try:
            print("Waiting for a connection...")
            connection, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            
            # Receive the length of the file name
            file_name_length = int.from_bytes(connection.recv(4), byteorder='big')
            print(f"File name length: {file_name_length}")
            
            # Receive the file name
            file_name = connection.recv(file_name_length).decode('utf-8').strip()
            print(f"Receiving file: {file_name}")
            
            # Create the full path for the output file
            output_file_path = os.path.join(output_dir, file_name)
            
            # Open the file in write-binary mode
            with open(output_file_path, 'wb') as file:
                while True:
                    # Receive data from the client
                    data = connection.recv(4096)  # Increased buffer size
                    if not data:
                        break
                    # Write data to the file
                    file.write(data)
            
            print(f"File {file_name} received and saved to {output_file_path}.")
        
        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            # Clean up the connection
            if 'connection' in locals():
                connection.close()
                print("Connection closed.")

if __name__ == "__main__":
    start_server()
