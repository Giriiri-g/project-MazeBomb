import pygame

class Map:
    def __init__(self, Asset Map=None):
        if Map is None:
            self.Map =  """       ╔══════════╗                                                   
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
        else:
            self.Map = Map
        self.player_pos = Asset.player_spawn
        self.Map_pos = Asset.map_spawn
        self.rowlen = len(self.Map[0:self.Map.index('\n')]) + 1
        self.playermap = ""
        self.height = 0
        self.width = 0
        self.Map_surf = None
            
    def move(self, d):
        if d=="a":
            calcpos = [self.player_pos[0], self.player_pos[1]-1]
            calcmappos = self.mapindexer(calcpos)
            if self.checkvalid(calcmappos):
                self.player_pos = calcpos
                self.Map_surf = self.drawplayer(calcmappos)
                
        elif d=="s":
            calcpos = [self.player_pos[0]+1, self.player_pos[1]]
            calcmappos = self.mapindexer(calcpos)
            if self.checkvalid(calcmappos):
                self.player_pos = calcpos
                self.Map_surf = self.drawplayer(calcmappos)
        elif d=="w":
            calcpos = [self.player_pos[0]-1, self.player_pos[1]]
            calcmappos = self.mapindexer(calcpos)
            if self.checkvalid(calcmappos):
                self.player_pos = calcpos
                self.Map_surf = self.drawplayer(calcmappos)
        elif d=="d":
            calcpos = [self.player_pos[0], self.player_pos[1]+1]
            calcmappos = self.mapindexer(calcpos)
            if self.checkvalid(calcmappos):
                self.player_pos = calcpos
                self.Map_surf = self.drawplayer(calcmappos)

    def checkvalid(self, mappos):
        if self.Map[mappos] in ['║','═','╗','╝','╚','╔', " "]:
            return False
        return True



    def mapindexer(self, pos):
        return pos[0]*self.rowlen + pos[1] + 1

    def drawplayer(self, mappos):
        self.playermap = Map[:mappos]+"@"+Map[mappos+1:]

    def draw_map(self):
        surf = pygame.Surface((self.height, self.widt))  # Create a surface with the same size as the screen
        surf.fill(Asset.black)  # Fill the surface with black background
        lines = self.playermap.split('\n')
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                color = Asset.grey
                if char in ['║', '═', '╗', '╝', '╚', '╔', '╦', '╣', '╠', '╩']:
                    color = Asset.wall_color
                elif char == "∙":
                    color = Asset.movable_space_color
                elif char == "!":
                    color = Asset.exclamation_color
                elif char == "▒":
                    color = Asset.passage_color
                elif char == "@":
                    color = Asset.player_color

                text_surface = pygame.font.render(char, True, color)
                surf.blit(text_surface, (j * 19, i * 30))

        return surf