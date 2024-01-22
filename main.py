## [ MAZE-bOMB ]

import pygame
import sys

Map = """
##################                            
#                #                            
#    @           #       #####################
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




pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Rogue Bomber")

black = (0, 0, 0)
grey = (169, 169, 169)

font = pygame.font.SysFont("monospace", 36) # use monospace font always, otherwise the text alignment will be off

lines = Map.split('\n')

while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
     screen.fill(black)

     # displaying each line in a text surface for efficient manipulation 
     for i, line in enumerate(lines):
          text_surface = font.render(line, True, grey)
          screen.blit(text_surface, (10, 10 + i * 40))
     pygame.display.flip()
