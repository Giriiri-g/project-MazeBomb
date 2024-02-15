import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_IP, SERVER_PORT))
print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")

try:
    while True:
        message = input("Enter your message: ")
        client_socket.sendall(message.encode())

        response = client_socket.recv(1024)
        print(f"Received from server: {response.decode()}")

        if message.lower() == "exit":
            break
finally:
    client_socket.close()
    print("Connection closed")
