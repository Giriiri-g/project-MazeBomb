import pygame

class Asset:
    def __init__(self):
        pygame.init()
        self.menu_active = False
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (169, 169, 169)
        self.wall_color = (170, 85, 0)
        self.movable_space_color = (80, 240, 80)
        self.exclamation_color = (251, 251, 84)
        self.passage_color = (167, 167, 167)
        self.player_color = (0, 0, 255)
        self.menu_active = False
        self.player_spawn = [10, 9]
        self.map_spawn = 720
        self.font = pygame.font.Font("Rogue Bomber/Assets/fonts/ttf - Ac (aspect-corrected)/AcPlus_IBM_BIOS.ttf", 60)
        self.font2 = pygame.font.Font("Rogue Bomber/Assets/fonts/ttf - Px (pixel outline)/PxPlus_IBM_BIOS.ttf", 40)
        self.font3 = pygame.font.Font("Rogue Bomber/Assets/fonts/ttf - Ac (aspect-corrected)/AcPlus_IBM_BIOS.ttf", 30)
        self.bombs = []
        self.height = 750
        self.width = 1200
        self.homepage_bg = "C:\\ps\\Project MazeBomb\\project-MazeBomb\\Rogue Bomber\\Assets\\Bomber.png"
        self.text_color = (255, 255, 255)
        self.background_color = (5, 22, 26)
        self.text_input_box_color = (0, 0, 0)
        self.text_input_bg_color = (255, 255, 255)
