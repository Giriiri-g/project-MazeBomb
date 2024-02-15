import pygame
import sys
import assets
from homepage import display_homepage
from loginpage2 import display_login_page
from game import run_game

pygame.init()

asset = assets.Asset()
screen = pygame.display.set_mode((asset.width, asset.height))
pygame.display.set_caption("Rogue Bomber")

current_page = "homepage"  # Start with the homepage

clock = pygame.time.Clock()

while True:
    if current_page == "homepage":
        next_page = display_homepage(screen)
    elif current_page == "login":
        next_page = display_login_page(screen)
    elif current_page == "game":
        next_page = run_game(screen, asset)

    # Check if the page should change
    if next_page:
        current_page = next_page

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
