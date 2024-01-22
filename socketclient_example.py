from socket import *

serverIP = "192.168.161.221"
serverPort = 15632

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
print(f'Connected to the server at {serverIP}:{serverPort}')

while True:
    message = input("Enter your message: ")
    clientSocket.send(message.encode())

    if message.lower() == "exit":
        break  # Break the loop if the user types "exit"

    reply = clientSocket.recv(1024).decode()
    print(f"Received from server: {reply}")

clientSocket.close()
print("Connection with the server closed")
