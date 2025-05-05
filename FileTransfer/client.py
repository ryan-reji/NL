import socket
import os

def send_file(file_path, host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    try:
        # Extract the file name from the path
        file_name = os.path.basename(file_path)
        print(f"Sending file: {file_name}")
        
        # Send the length of the file name
        file_name_length = len(file_name)
        client_socket.send(file_name_length.to_bytes(4, byteorder='big'))
        
        # Send the file name
        client_socket.send(file_name.encode('utf-8'))
        
        # Open the file in read-binary mode
        with open(file_path, 'rb') as file:
            while True:
                # Read the file in chunks and send it
                data = file.read(4096)  # Increased buffer size
                if not data:
                    break
                client_socket.send(data)
        
        print(f"File {file_name} sent successfully.")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == "__main__":
    file_path = input("Enter the file path to send: ")
    send_file(file_path)
