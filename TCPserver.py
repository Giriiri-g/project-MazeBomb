import socket

SERVER_IP = "192.168.10.221"
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_IP, SERVER_PORT))

server_socket.listen(1)
print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

try:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from client: {data.decode()}")

        response = input("Enter your response: ")
        client_socket.sendall(response.encode())
finally:
    client_socket.close()
    server_socket.close()
    print("Connection closed")
