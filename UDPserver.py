import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((SERVER_IP, SERVER_PORT))
print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received from client: {data.decode()}")

    response = input("Enter your response: ")
    server_socket.sendto(response.encode(), client_address)
