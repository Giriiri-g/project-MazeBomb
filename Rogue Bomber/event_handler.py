import pygame
import sys
from assets import menu_active

def handle_events(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q and menu_active:
            print("Shutting Down")
            pygame.quit()
            sys.exit()
        elif not menu_active:
            handle_movement(event.key)

def handle_movement(key):
    if key == pygame.K_a:
        move("a")
    elif key == pygame.K_s:
        move("s")
    elif key == pygame.K_w:
        move("w")
    elif key == pygame.K_d:
        move("d")
    elif key == pygame.K_ESCAPE:
        menu_active = False
    elif key == pygame.K_SLASH:
        menu_active = True
        screen.fill(black)
        screen.blit(menu, (menu_x, menu_y))
