import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        message = input("Enter your message: ")
        client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

        response, server_address = client_socket.recvfrom(1024)
        print(f"Received from server: {response.decode()}")

        if message.lower() == "exit":
            break
finally:
    client_socket.close()
