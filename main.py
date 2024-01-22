## [ MAZE-bOMB ]

import pygame
import sys

Map = """
##################                            
#                #                            
#                #       #####################
#                #-------# !                 #
#                |       |                   #
#                #-------#              !    #
#           !    #       #                   #
#                #       #####################
##################                            
"""
Map2 = """
##################............................
#................#............................
#....@...........#.......#####################
#................#-------#.!.................#
#................|.......|...................#
#................#-------#..............!....#
#...........!....#.......#...................#
#................#.......#####################
##################............................
"""
#Map2='##################                            \n#                #                            \n#    @           #       #####################\n#                #-------# !                 #\n#                |       |                   #\n#                #-------#              !    #\n#           !    #       #                   #\n#                #       #####################\n##################                            \n'


def move(d):
     if d=="a":
          calcpos = [Player_pos[0]-1, Player_pos[1]]
          calcmappos = mapindexer(calcpos)
          if checkvalid(calcmappos):
               Player_pos = calcpos
               
     elif d=="s":
          checkvalid(calcmappos)
          pass
     elif d=="w":
          checkvalid(calcmappos)
          pass
     elif d=="d":
          checkvalid(calcmappos)
          pass

def checkvalid(mappos):
     if Map[mappos] == "#":
          return False
     return True

def mapindexer(pos):
     return pos[0]*47 + pos[1] + 1

def drawplayer(mappos):
     mapstr = Map[:mappos]+"@"+Map[mappos+1:]
     return mapstr

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Rogue Bomber")

black = (0, 0, 0)
grey = (169, 169, 169)
Player_pos = [2, 5]
Map_pos = 100
# curr Map pos = pos[0]*47 + pos[1] + 1, pos -> player pos
font = pygame.font.SysFont("monospace", 36) # use monospace font always, otherwise the text alignment will be off
playermap = drawplayer(Map_pos)
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
               if event.key == pygame.K_s:
                    move("a")
               if event.key == pygame.K_w:
                    move("a")
               if event.key == pygame.K_d:
                    move("a")

     screen.fill(black)
     # displaying each line in a text surface for efficient manipulation 
     for i, line in enumerate(lines):
          text_surface = font.render(line, True, grey)
          screen.blit(text_surface, (10, 10 + i * 40))
     pygame.display.flip()
     clock.tick(60)
