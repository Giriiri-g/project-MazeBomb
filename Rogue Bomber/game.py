##[ MAZE-bOMB ]

import pygame
import sys

def run_game(screen):
    global Map, Player_pos, playermap, lines, menu_active, hud_surface, hud_names, hud_values, font2, player_huds, font

    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 255, 0)
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
    hud_values = [["♥♥♥♥♥", 1, 1], ["♥♥♥", 0, 2], ["", 3, 0], ["♥♥♥♥", 2, 1]]
    surface_width = 298
    surface_height = 58
    player_huds = [pygame.Surface((surface_width, surface_height)) for _ in range(4)]

    pygame.init()
    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Rogue Bomber")

    Map =  """       ╔══════════╗                                                   
       ║∙∙∙∙∙∙∙∙∙∙║                               ╔══════════════════╗
       ║∙∙∙∙∙∙∙∙∙∙║                               ║∙∙∙∙∙∙∙∙!∙∙∙∙∙∙∙∙∙║
       ╚══════╦═══╝                            ▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙∙∙!∙∙∙∙║
              ▒                         ▒▒▒▒▒▒▒▒  ╚╦═════════════════╝
              ▒                         ▒          ▒                  
        ▒▒▒▒▒▒▒                    ▒▒▒▒▒▒          ▒▒▒▒▒▒             
╔═══════╩══════════╗               ▒              ╔═════╩════════════╗
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒            ▒              ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║  ▒  ╔═════════╩═╗            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║  ▒▒▒╣∙∙∙∙∙∙∙∙∙!∙║            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒▒▒▒▒▒▒▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙∙!∙∙∙∙∙║
║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙∙!∙∙∙∙∙∙║            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║
╚═══════╦══════════╝     ╚═════════╦═╝            ╚══════════════════╝
        ▒                   ▒▒▒▒▒▒▒▒                                  
        ▒▒▒▒▒▒▒▒▒▒▒       ╔═╩═╗                                       
       ╔══════════╩═╗    ▒╣∙∙∙║                          ╔════╗       
       ║∙∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒▒▒║∙∙∙║                          ║∙∙∙∙║       
       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙║                          ║∙!∙∙║       
       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙║  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╣∙∙∙∙║       
       ║∙∙∙∙∙!∙∙∙∙∙∙║     ║∙∙∙╠▒▒▒                       ║∙∙∙∙║       
       ╚════════════╝     ╚═══╝                          ╚════╝       
"""


    def move(d):
        global Player_pos
        if d=="a":
            calcpos = [Player_pos[0], Player_pos[1]-1]
            calcmappos = mapindexer(calcpos)
            if checkvalid(calcmappos):
                Player_pos = calcpos
                drawplayer(calcmappos)
                
        elif d=="s":
            calcpos = [Player_pos[0]+1, Player_pos[1]]
            calcmappos = mapindexer(calcpos)
            if checkvalid(calcmappos):
                Player_pos = calcpos
                drawplayer(calcmappos)
        elif d=="w":
            calcpos = [Player_pos[0]-1, Player_pos[1]]
            calcmappos = mapindexer(calcpos)
            if checkvalid(calcmappos):
                Player_pos = calcpos
                drawplayer(calcmappos)
        elif d=="d":
            calcpos = [Player_pos[0], Player_pos[1]+1]
            calcmappos = mapindexer(calcpos)
            if checkvalid(calcmappos):
                Player_pos = calcpos
                drawplayer(calcmappos)

    def checkvalid(mappos):
        if Map[mappos] in ['║','═','╗','╝','╚','╔', " "]:
            return False
        return True

    def mapindexer(pos):
        return pos[0]*71 + pos[1] + 1

    def drawplayer(mappos):
        global playermap
        playermap = Map[:mappos]+"@"+Map[mappos+1:]

    def draw_map():
        screen.fill(black)
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                color = black  # Default color for characters not explicitly defined
                if char in ['║','═','╗','╝','╚','╔','╦','╣','╠','╩']:
                        color = wall_color
                elif char == "∙":
                        color = movable_space_color
                elif char == "!":
                        color = exclamation_color
                elif char == "▒":
                        color = passage_color
                elif char == "@":
                        color = player_color

                text_surface = font.render(char, True, color)
                offset = (j * 15 + 75, i * 28 + 120)
                screen.blit(text_surface, offset)
                # text_rect = text_surface.get_rect()
                # text_rect.topleft = offset
                # screen.blit(text_surface, text_rect)
                # pygame.draw.rect(screen, (255, 255, 255), text_rect, 1)

    def draw_hud():
        hud_surface.fill(grey)
        x_positions = [1, 301, 601, 901]
        y_position = 1
        screen.blit(hud_surface, (0, 0))
        for i, (name, values) in enumerate(zip(hud_names, hud_values)):
            player_huds[i].fill((0, 0, 0))
            name_text = font2.render(name, True, white)
            player_huds[i].blit(name_text, (10, 5))
            hearts_text = font2.render(values[0], True, white)
            player_huds[i].blit(hearts_text, (200, 6))
            val1_text = font2.render("☼x"+str(values[1]), True, white)
            player_huds[i].blit(val1_text, (10, 30))
            val2_text = font2.render("ɸx"+str(values[2]), True, white)
            player_huds[i].blit(val2_text, (val1_text.get_width() + 200, 30))
            screen.blit(player_huds[i], (x_positions[i], y_position))




    Player_pos = [10, 9]
    Map_pos = 720
    # curr Map pos = pos[0]*71 + pos[1] + 1, pos -> player pos
    playermap = ""
    drawplayer(Map_pos)
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
    menu.fill((0, 0, 0, 0))  # Make the surface transparent

    for i, line in enumerate(menu_lines):
        text_surface = font.render(line, True, grey)
        menu.blit(text_surface, (0, i * font.get_height()))

    menu_x = (screen.get_width() - menu.get_width()) // 2
    menu_y = (screen.get_height() - menu.get_height()) // 2

    # Main Loop

    clock = pygame.time.Clock()

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
                        move("a")
                        lines = playermap.split('\n')
                if event.key == pygame.K_s and menu_active == False:
                        move("s")
                        lines = playermap.split('\n')
                if event.key == pygame.K_w and menu_active == False:
                        move("w")
                        lines = playermap.split('\n')
                if event.key == pygame.K_d and menu_active == False:
                        move("d")
                        lines = playermap.split('\n')

                if (event.key == pygame.K_ESCAPE):
                        menu_active = False

                if (event.key == pygame.K_SLASH):
                        
                        menu_active = True
                        screen.fill(black)
                        screen.blit(menu, (menu_x, menu_y))
                        
                        
                        


        
        # displaying each line in a text surface for efficient manipulation 
        if menu_active == False:
            draw_map()
            draw_hud()
        pygame.display.flip()
        clock.tick(60)


# import assets
# pygame.init()
# asset = assets.Asset()
# screen = pygame.display.set_mode((asset.width, asset.height))
# pygame.display.set_caption("Rogue Bomber")
# run_game(screen)