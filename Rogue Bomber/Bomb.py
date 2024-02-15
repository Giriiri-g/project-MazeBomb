class bomb:
    def __init__(self, poss):
        self.poss = poss
        self.ttk = 2 # time to kill in seconds
        self.players = None
    
    def tick(self):
        self.ttk -= 1
        if self.ttk == 0:
            return True
        return False
    
    def getpos(self):
        return self.poss
    
    def getplayers(self):
        pass

    def damage(self):
        if self.players is not None:
            for p in self.players:
                p.damage(3)

        
        
        
        
# Compare this snippet from main.py:

    
