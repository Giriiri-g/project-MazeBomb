##[ MAZE-bOMB ]
import  random
import pygame
import sys

def run_game(screen):
    global Map, Player_pos, playermap, lines, menu_active, hud_surface, hud_names, hud_values, font2, player_huds, font, bombs, players, og_Map


    players = [[10,9], [11,30], [10, 58], [18, 27]]
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    grey = (169,169,169)
    wall_color = (170, 85, 0)
    movable_space_color = (80, 240, 80)
    exclamation_color = (251, 251, 84)
    passage_color = (167, 167, 167)
    player_color = (0, 0, 255)
    font = pygame.font.SysFont("Courier New", 28)
    font2 = pygame.font.Font("Rogue Bomber/Assets/fonts/ttf - Ac (aspect-corrected)/AcPlus_IBM_BIOS.ttf", 18)
    hud_surface = pygame.Surface((1200, 60))
    hud_surface.fill((169, 169, 169))
    hud_names = ["Giriirig", "PsylectrA", "Puchandi", "cumlord"]
    hud_values = [["♥♥♥♥♥", 0, 1], ["♥♥♥", 0, 2], ["", 3, 0], ["♥♥♥♥", 2, 1]]
    surface_width = 298
    surface_height = 58
    player_huds = [pygame.Surface((surface_width, surface_height)) for _ in range(4)]
    bombs = []

    pygame.init()
    pygame.display.set_caption("Rogue Bomber")

    Map =  """       ╔══════════╗                                                   
       ║∙∙∙∙∙∙∙∙∙∙║                               ╔══════════════════╗
       ║∙∙∙∙∙∙∙∙∙∙║                               ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
       ╚══════╦═══╝                            ▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
              ▒                         ▒▒▒▒▒▒▒▒  ╚╦═════════════════╝
              ▒                         ▒          ▒                  
        ▒▒▒▒▒▒▒                    ▒▒▒▒▒▒          ▒▒▒▒▒▒             
╔═══════╩══════════╗               ▒              ╔═════╩════════════╗
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒            ▒              ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║  ▒  ╔═════════╩═╗            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║  ▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙║            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒▒▒▒▒▒▒▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙∙∙∙∙∙∙∙∙║            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
╚═══════╦══════════╝     ╚═════════╦═╝            ╚══════════════════╝
        ▒                   ▒▒▒▒▒▒▒▒                                  
        ▒▒▒▒▒▒▒▒▒▒▒       ╔═╩═╗                                       
       ╔══════════╩═╗    ▒╣∙∙∙║                          ╔════╗       
       ║∙∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒▒▒║∙∙∙║                          ║∙∙∙∙║       
       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙║                          ║∙∙∙∙║       
       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙║  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╣∙∙∙∙║       
       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙╠▒▒▒                       ║∙∙∙∙║       
       ╚════════════╝     ╚═══╝                          ╚════╝       
"""
    og_Map =  """       ╔══════════╗                                                   
       ║∙∙∙∙∙∙∙∙∙∙║                               ╔══════════════════╗
       ║∙∙∙∙∙∙∙∙∙∙║                               ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
       ╚══════╦═══╝                            ▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
              ▒                         ▒▒▒▒▒▒▒▒  ╚╦═════════════════╝
              ▒                         ▒          ▒                  
        ▒▒▒▒▒▒▒                    ▒▒▒▒▒▒          ▒▒▒▒▒▒             
╔═══════╩══════════╗               ▒              ╔═════╩════════════╗
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒            ▒              ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║  ▒  ╔═════════╩═╗            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║  ▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙║            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒▒▒▒▒▒▒▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙∙∙∙∙∙∙∙∙║            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
╚═══════╦══════════╝     ╚═════════╦═╝            ╚══════════════════╝
        ▒                   ▒▒▒▒▒▒▒▒                                  
        ▒▒▒▒▒▒▒▒▒▒▒       ╔═╩═╗                                       
       ╔══════════╩═╗    ▒╣∙∙∙║                          ╔════╗       
       ║∙∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒▒▒║∙∙∙║                          ║∙∙∙∙║       
       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙║                          ║∙∙∙∙║       
       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙║  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╣∙∙∙∙║       
       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙╠▒▒▒                       ║∙∙∙∙║       
       ╚════════════╝     ╚═══╝                          ╚════╝       
"""

    def move(d, player):
        global lines, Map, hud_values, players
        new_pos = players[player][:]  # Create a copy of the player's position
        if d == "a":
            new_pos[1] -= 1
        elif d == "s":
            new_pos[0] += 1
        elif d == "w":
            new_pos[0] -= 1
        elif d == "d":
            new_pos[1] += 1

        new_map_pos = mapindexer(new_pos)
        if checkvalid(new_map_pos):
            if Map[new_map_pos] == '!':
                Map = Map[:new_map_pos] + '∙' + Map[new_map_pos + 1:]
                if hud_values[player][1] < 3:
                    hud_values[player][1]+=1
            players[player] = new_pos
            drawplayer()

    def checkvalid(mappos):
        global Map
        if Map[mappos] in ['║','═','╗','╝','╚','╔', " "]:
            return False
        return True

    def mapindexer(pos):
        return pos[0]*71 + pos[1] + 1

    def drawplayer():
        global playermap, Map, players, lines
        mappos = [mapindexer(i) for i in players]
        playermap = list(Map)
        playermap[mappos[0]] = "@"
        playermap[mappos[1]] = "#"
        playermap[mappos[2]] = "$"
        playermap[mappos[3]] = "&"
        playermap = ''.join(playermap)
        lines = playermap.split('\n')
        

    def draw_map():
        screen.fill(black)
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                color = black  # Default color for characters not explicitly defined
                if char in ['║','═','╗','╝','╚','╔','╦','╣','╠','╩']:
                    color = wall_color
                elif char == "∙":
                    color = movable_space_color
                elif char in ["!", "☼"]:
                    color = exclamation_color
                elif char == "▒":
                    color = passage_color
                elif char in ["@", "#", "$", "&"]:
                    color = player_color

                text_surface = font.render(char, True, color)
                offset = (j * 15 + 75, i * 28 + 120)
                screen.blit(text_surface, offset)

    def draw_hud():
        global players
        hud_surface.fill(grey)
        x_positions = [1, 301, 601, 901]
        y_position = 1
        screen.blit(hud_surface, (0, 0))
        for i, (name, values) in enumerate(zip(hud_names, hud_values)):
            if len(values[0]) == 0:
                players[i] = [2, 27]
                font_color = red
            else:
                font_color = white
            player_huds[i].fill((0, 0, 0))
            name_text = font2.render(name, True, font_color)
            player_huds[i].blit(name_text, (10, 5))
            hearts_text = font2.render(values[0], True, font_color)
            player_huds[i].blit(hearts_text, (200, 6))
            val1_text = font2.render("☼x"+str(values[1]), True, font_color)
            player_huds[i].blit(val1_text, (10, 30))
            val2_text = font2.render("ɸx"+str(values[2]), True, font_color)
            player_huds[i].blit(val2_text, (val1_text.get_width() + 200, 30))
            screen.blit(player_huds[i], (x_positions[i], y_position))


    def place_bomb(player):
         global Map, bombs, players, playermap
         bombs.append([players[player], 120])
         Map = Map[:mapindexer(players[player])] + '☼' + Map[mapindexer(players[player])+1:]
         drawplayer()
         hud_values[player][1] -= 1

    def explode(index):
        global Map, bombs, players, og_Map
        bomb = bombs[index]
        Map = Map[:mapindexer(bomb[0])] + og_Map[mapindexer(bomb[0])] + Map[mapindexer(bomb[0])+1:]
        bombs.pop(index)
        x,y = bomb[0][0], bomb[0][1]
        radius = [[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
        for ind, player in enumerate(players):
            if player in radius:
                hud_values[ind][0] = hud_values[ind][0][:-1]
        drawplayer()
        draw_map()
        draw_hud()

    # Player_pos = [10, 9]
    player = 0
    # Map_pos = 720
    # curr Map pos = pos[0]*71 + pos[1] + 1, pos -> player pos
    playermap = ""
    drawplayer()
    draw_hud()
    lines = playermap.split('\n')
    menu_active = False

    # menu surface

    desc = """Welcome to Rogue Bomber!
    A    : Move West
    S    : Move South
    W    : Move North
    D    : Move East
    Q    : Quit
    /    : Display Help
    ESC  : Exit Help Menu
    !    : Bomb
    ▒    : Passage
    ║    : A vertical wall
    ═    : A horizontal wall
    ╠    : Doorway"""

    menu_lines = desc.split('\n')
    menu_height = len(menu_lines) * font.get_height()
    menu = pygame.Surface((font.size(max(menu_lines, key=len))[0], menu_height), pygame.SRCALPHA)
    menu.fill((0, 0, 0, 0))

    for i, line in enumerate(menu_lines):
        text_surface = font.render(line, True, grey)
        menu.blit(text_surface, (0, i * font.get_height()))

    menu_x = (screen.get_width() - menu.get_width()) // 2
    menu_y = (screen.get_height() - menu.get_height()) // 2

    # Main Loop

    clock = pygame.time.Clock()
    fps = 60
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and menu_active == True:
                        print("Shutting Down")
                        pygame.quit()
                        sys.exit()
                if event.key == pygame.K_a and menu_active == False:
                        move("a", player)
                if event.key == pygame.K_s and menu_active == False:
                        move("s", player)
                if event.key == pygame.K_w and menu_active == False:
                        move("w", player)
                if event.key == pygame.K_d and menu_active == False:
                        move("d", player)
                if event.key == pygame.K_b and menu_active == False:
                        if hud_values[0][1]>0:
                            place_bomb(player)

                if (event.key == pygame.K_ESCAPE):
                        menu_active = False

                if (event.key == pygame.K_SLASH):
                        
                        menu_active = True
                        screen.fill(black)
                        screen.blit(menu, (menu_x, menu_y))
                        
                        

        for ind, i in enumerate(bombs):
             i[1] -= 1
             if i[1] == 0:
                  explode(ind)
                        
        if Map.count('!') <= 8 and random.random() < 0.005:
            movable_indices = [i for i, char in enumerate(Map) if char == '∙']
            if movable_indices:
                random_index = random.choice(movable_indices)
                Map = Map[:random_index] + '!' + Map[random_index + 1:]

        

        if menu_active == False:
            drawplayer()

            draw_map()
            draw_hud()
        pygame.display.flip()
        clock.tick(60)


import assets
pygame.init()
asset = assets.Asset()
screen = pygame.display.set_mode((asset.width, asset.height))
pygame.display.set_caption("Rogue Bomber")
run_game(screen)