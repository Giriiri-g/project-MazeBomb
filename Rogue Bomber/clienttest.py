import socket
import pygame

player_id = 1

def send_key_to_server(key):
    SERVER_IP = '192.168.25.221'
    SERVER_PORT = 60000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        client_socket.send(key.encode())
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Client")
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    send_key_to_server(f"a,{player_id}")
                if event.key == pygame.K_s:
                    send_key_to_server(f"s,{player_id}")
                if event.key == pygame.K_w:
                    send_key_to_server(f"w,{player_id}")
                if event.key == pygame.K_d:
                    send_key_to_server(f"d,{player_id}")
                if event.key == pygame.K_b:
                    send_key_to_server(f"b,{player_id}")
                
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()