class player:

    def __init__(self, name:str):
        self.score = 0
        self.alive = False
        self.name = name
    
    def __repr__(self):
        if not self.onTable():
            return self.name
        return self.name +'\nscore: ' + str(self.score)

    def onTable(self):
        return self.score > 1000

    def addScore(self,amount):
        if self.score > 1000 and amount > 0:
            self.score += amount
            return 1
        elif amount >= 1000:
            self.score += amount
            return 1
        return 0