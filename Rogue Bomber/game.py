import pygame
import sys
from map import Map
Player_pos = [10, 9]
Map_pos = 720

def run_game(screen, asset, map_instance):
    Map = """       ╔══════════╗                                                   
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
            print(calcpos, calcmappos)
            if checkvalid(calcmappos):
                Player_pos = calcpos
                print("move valid")
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
                screen.blit(text_surface, (j * 19, i * 30))




    black = (0, 0, 0)
    blue = (0, 255, 0)
    grey = (169,169,169)
    wall_color = (170, 85, 0)
    movable_space_color = (80, 240, 80)
    exclamation_color = (251, 251, 84)
    passage_color = (167, 167, 167)
    player_color = (0, 0, 255)


    
    # curr Map pos = pos[0]*71 + pos[1] + 1, pos -> player pos
    font = pygame.font.SysFont("Courier New", 32) # use monospace font always, otherwise the text alignment will be off
    playermap = ""
    drawplayer(Map_pos)
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
                        print("A")
                if event.key == pygame.K_s and menu_active == False:
                        move("s")
                        lines = playermap.split('\n')
                        print("S")
                if event.key == pygame.K_w and menu_active == False:
                        move("w")
                        lines = playermap.split('\n')
                        print("W")
                if event.key == pygame.K_d and menu_active == False:
                        move("d")
                        lines = playermap.split('\n')
                        print("D")

                if (event.key == pygame.K_ESCAPE):
                        menu_active = False

                if (event.key == pygame.K_SLASH):
                        
                        menu_active = True
                        screen.fill(black)
                        screen.blit(menu, (menu_x, menu_y))
                        
        if menu_active == False:
            draw_map()
        pygame.display.flip()
        clock.tick(60)
