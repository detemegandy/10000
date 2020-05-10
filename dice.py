import random
class dice():
    def __init__(self,sides=6):
        self.sides = sides
        self.sideUp = random.randint(1,self.sides)
        self.saved = False

    def __repr__(self):
        if self.saved:
            return "(" + str(self.sideUp) + ")"
        return str(self.sideUp)

    def __str__(self):
        return str(self.sideUp)

    def roll(self):
        if self.saved == False:
            self.sideUp = random.randint(1,self.sides)
        return self

    def save(self,side):
        if self.sideUp == side:
            self.saved = True
        
    def rollSaved(self):
        self.sideUp = random.randint(1,self.sides)
        self.saved == False