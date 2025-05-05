import socket

def download_webpage(url):
    # Ensure the URL starts with 'http://'
    if not url.startswith('http://'):
        url = 'http://' + url
    
    # Parse the URL to extract the host and path
    host = url.split('/')[2]
    path = '/' + '/'.join(url.split('/')[3:]) if len(url.split('/')) > 3 else '/'
    
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server on port 80 (HTTP)
        s.connect((host, 80))
        
        # Formulate the HTTP GET request
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        s.sendall(request.encode())
        
        # Receive the response from the server
        response = b''
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data
    
    # Separate headers and body
    header_data, _, body = response.partition(b'\r\n\r\n')
    
    # Decode headers to string
    headers = header_data.decode()
    
    return headers, body.decode(errors='replace')

# Example usage
headers, content = download_webpage('example.com')

print("Headers:")
print(headers)
print("\nContent:")
print(content)
