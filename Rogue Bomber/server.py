import socket
import threading
from queue import Queue

# Define a global queue to store received inputs
input_queue = Queue()

def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            input_queue.put(data.decode())  # Put received data into the queue
        except Exception as e:
            print("Error:", e)
            break
    
    # Close the client socket
    client_socket.close()

def server_main():
    # Define the server address and port
    SERVER_IP = '192.168.239.221'
    SERVER_PORT = 60000
    
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind the socket to the server address and port
        server_socket.bind((SERVER_IP, SERVER_PORT))
        
        # Listen for incoming connections
        server_socket.listen(3)
        print("Server is listening for connections...")
        
        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print("Connection from:", client_address)
            
            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the server socket
        server_socket.close()

def receive_inputs():
    # Function to retrieve inputs from the queue
    inputs = []
    while not input_queue.empty():
        inputs.append(input_queue.get())
    return inputs


if __name__ == '__main__':
    server_main()