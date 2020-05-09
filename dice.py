import random
class dice():
    def __init__(self,sides=6):
        self.sides = sides
        self.sideUp = random.randint(1,self.sides)
        self.saved = False
        
    def __repr__(self):
        return "(sides: " + str(self.sides) + ", sideUp: " + str(self.sideUp) + ", saved: " + str(self.saved)+")"

    def __str__(self):
        return str(self.sideUp)

    def roll(self):
        if self.saved == False:
            self.sideUp = random.randint(1,self.sides)

    def save(self,side):
        if self.sideUp == side:
            self.saved = True
            return 1
        return 0
        
    def rollSaved(self):
        self.sideUp = random.randint(1,self.sides)
        self.saved == False