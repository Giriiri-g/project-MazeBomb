from socket import *

serverIP = "172.20.10.3"
serverPort = 18547

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
print(f'Connected to the server at {serverIP}:{serverPort}')

while True:
    message = input("Enter your message: ")
    clientSocket.send(message.encode())

    if message.lower() == "exit":
        break  # Break the loop if the user types "exit"

    reply = clientSocket.recv(20000).decode()
    reply = reply.replace("n", "\n")
    print(f"Received from server: \n{reply}")


clientSocket.close()
print("Connection with the server closed")
