from socket import *

serverIP = "172.20.10.3"
serverPort = 18547

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)
print(f'The server is ready to receive messages at {serverIP}:{serverPort}')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection established with {addr}")
     
    while True:
        message = connectionSocket.recv(20000).decode()
        if not message:
            break  # Break the inner loop if no message received
        print(f"Received from client: {message}")

        reply = input("Enter your reply: ")
        connectionSocket.send(reply.encode())

    connectionSocket.close()
    print(f"Connection with {addr} closed")
