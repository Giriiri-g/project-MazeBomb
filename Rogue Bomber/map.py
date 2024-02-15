import pygame
from assets import *

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