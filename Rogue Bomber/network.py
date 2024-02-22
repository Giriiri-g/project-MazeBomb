import socket
import threading
from tkinter import *

# Server configuration
SERVER_IP = "172.26.224.1"
SERVER_PORT = 16000

# Function to handle receiving messages from the server
def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                received_message = data.decode()
                print(f"Received from server: {received_message}")
                messages_text.insert(END, received_message + "\n")
                messages_text.see(END)
        except Exception as e:
            print(f"Error receiving message from server: {e}")
            break

# Function to send message to the server
def send_message(client_socket):
    message = input_entry.get()
    try:
        client_socket.sendall(message.encode())
    except Exception as e:
        print(f"Error sending message to server: {e}")
    input_entry.delete(0, END)

# Socket setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
print("Connected to server.")

# Start thread for receiving messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Tkinter setup
root = Tk()
root.title("Client")

messages_text = Text(root, width=50, height=20)
messages_text.pack(pady=20)

input_frame = Frame(root)
input_frame.pack()

input_label = Label(input_frame, text="Enter Message:")
input_label.grid(row=0, column=0)

input_entry = Entry(input_frame, width=30)
input_entry.grid(row=0, column=1)

send_button = Button(input_frame, text="Send", command=lambda: send_message(client_socket))
send_button.grid(row=0, column=2, padx=10)

# Main Tkinter loop
root.mainloop()