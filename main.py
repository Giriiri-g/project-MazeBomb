##[ MAZE-bOMB ]

import pygame
import sys

Map = """       ╔══════════╗                                                   
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
Player_pos = [10, 9]
Map_pos = 720
# curr Map pos = pos[0]*71 + pos[1] + 1, pos -> player pos
font = pygame.font.SysFont("monospace", 36) # use monospace font always, otherwise the text alignment will be off
playermap = ""
drawplayer(Map_pos)
lines = playermap.split('\n')


clock = pygame.time.Clock()

while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_a:
                    move("a")
                    lines = playermap.split('\n')
                    print(playermap)
                    print("A")
               if event.key == pygame.K_s:
                    move("s")
                    lines = playermap.split('\n')
                    print(playermap)
                    print("S")
               if event.key == pygame.K_w:
                    move("w")
                    lines = playermap.split('\n')
                    print(playermap)
                    print("W")
               if event.key == pygame.K_d:
                    move("d")
                    lines = playermap.split('\n')
                    print(playermap)
                    print("D")

     screen.fill(black)
     # displaying each line in a text surface for efficient manipulation 
     for i, line in enumerate(lines):
          text_surface = font.render(line, True, blue)
          screen.blit(text_surface, (0, i * 40))
     pygame.display.flip()
     clock.tick(60)
