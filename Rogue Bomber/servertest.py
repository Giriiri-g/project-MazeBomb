import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            data = data.decode().split(",")
            data[1] = int(data[1])
            print("Received:", data)
        except Exception as e:
            print("Error:", e)
            break
    client_socket.close()

def main():
    SERVER_IP = '192.168.239.221'
    SERVER_PORT = 60000
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server_socket.bind((SERVER_IP, SERVER_PORT))
        server_socket.listen(3)
        print("Server is listening for connections...")
        
        while True:
            client_socket, client_address = server_socket.accept()
            # print("Connection from:", client_address)
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except Exception as e:
        print("Error:", e)
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
