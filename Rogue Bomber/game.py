import pygame
import sys
from event_handler import *
from map import *
from assets import *

def run_game():
    while True:
        for event in pygame.event.get():
            handle_events(event)

        if not menu_active:
            draw_map()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Rogue Bomber")
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    run_game()
