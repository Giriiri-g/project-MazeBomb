import pygame
import sys
from menu import *

def handle_events(event, Asset):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q and Asset.menu_active:
            print("Shutting Down")
            pygame.quit()
            sys.exit()
        elif not Asset.menu_active:
            handle_movement(event.key)

def handle_movement(key, Asset, map, screen):
    if key == pygame.K_a:
        map.move("a")
    elif key == pygame.K_s:
        map.move("s")
    elif key == pygame.K_w:
        map.move("w")
    elif key == pygame.K_d:
        map.move("d")
    elif key == pygame.K_ESCAPE:
        menu_active = False
    elif key == pygame.K_SLASH:
        menu_active = True
        screen.fill((0, 0, 0))
        screen.blit(menu, (menu_x, menu_y))
