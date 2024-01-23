##[ MAZE-bOMB ]

import pygame
import sys

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
Map2 = """
══════════════════............................
═................═............................
═....@...........═.......═════════════════════
═................═-------═.!.................═
═................╠.......╠...................═
═................═-------═..............!....═
═...........!....═.......═...................═
═................═.......═════════════════════
══════════════════............................
"""
#Map2='══════════════════                            \n═                ═                            \n═    @           ═       ═════════════════════\n═                ═-------═ !                 ═\n═                ╠       ╠                   ═\n═                ═-------═              !    ═\n═           !    ═       ═                   ═\n═                ═       ═════════════════════\n══════════════════                            \n'


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


pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Rogue Bomber")

black = (0, 0, 0)
blue = (0, 255, 0)
grey = (169,169,169)
Player_pos = [10, 9]
Map_pos = 720
# curr Map pos = pos[0]*71 + pos[1] + 1, pos -> player pos
font = pygame.font.SysFont("monospace", 36) # use monospace font always, otherwise the text alignment will be off
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

clock = pygame.time.Clock()

while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_q:
                    print("Shutting Down")
                    pygame.quit()
                    sys.exit()
               if event.key == pygame.K_a and menu_active == False:
                    move("a")
                    lines = playermap.split('\n')
                    print(playermap)
                    print("A")
               if event.key == pygame.K_s and menu_active == False:
                    move("s")
                    lines = playermap.split('\n')
                    print(playermap)
                    print("S")
               if event.key == pygame.K_w and menu_active == False:
                    move("w")
                    lines = playermap.split('\n')
                    print(playermap)
                    print("W")
               if event.key == pygame.K_d and menu_active == False:
                    move("d")
                    lines = playermap.split('\n')
                    print(playermap)
                    print("D")

               if (event.key == pygame.K_ESCAPE):
                    menu_active = False

               if (event.key == pygame.K_SLASH):
                    
                    menu_active = True
                    screen.fill(black)
                    screen.blit(menu, (menu_x, menu_y))
                    
                    
                    


     
     # displaying each line in a text surface for efficient manipulation 
     if menu_active == False:
          screen.fill(black)
          for i, line in enumerate(lines):
               text_surface = font.render(line, True, blue)
               screen.blit(text_surface, (0, i * 40))
     pygame.display.flip()
     clock.tick(60)
