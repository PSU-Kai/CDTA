import socket
import os

# Set up a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Get the server's host name
host_name = socket.gethostname()

# Get the server's IP address
ip_address = socket.gethostbyname(host_name)
# Bind the socket to a specific address and port
server_address = (ip_address, 4096)  # server address and port number
sock.bind(server_address)

# Listen for incoming connections
sock.listen()

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    connection, client_address = sock.accept()

    try:
        print(f"Connection from {client_address}")
        
        # Receive the file name
        file_name = connection.recv(4096)
        print(f"Received data: {file_name}")  # add this line
        file_name = file_name.decode('utf-8')
        print(f"Decoded file name: {file_name}")  # add this line

        # Send acknowledgement of file name receipt
        connection.sendall(bytes('ack', 'utf-8'))
        print("Sent ack")  # add this line

        # Receive the file data
        file_data = b""
        while True:
            data = connection.recv(4096)
            if not data:
                break
            file_data += data

        # Write the file data to a file
        with open(file_name, 'wb') as f:
            f.write(file_data)

        print(f"Received and wrote file: {file_name}")

        # Send success message
        connection.sendall(bytes('success', 'utf-8'))

    finally:
        # Clean up the connection
        connection.close()
