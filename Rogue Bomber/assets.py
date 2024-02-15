class Asset:
    def __init__(self):
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