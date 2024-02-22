import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            print("Received:", data.decode())
        except Exception as e:
            print("Error:", e)
            break
    
    # Close the client socket
    client_socket.close()

def main():
    # Define the server address and port
    SERVER_IP = '192.168.239.221'
    SERVER_PORT = 60000
    
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind the socket to the server address and port
        server_socket.bind((SERVER_IP, SERVER_PORT))
        
        # Listen for incoming connections
        server_socket.listen(1)
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

if __name__ == "__main__":
    main()
