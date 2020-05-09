class player:

    def __init__(self):
        self.score = 0
        self.alive = True
        print('player')
    
    def onTable(self):
        return self.score > 1000

    def addScore(self,amount):
        self.score += amount