import random
class dice():
    def __init__(self,sides):
        self.sideUp = random.randint(1,sides)
    def roll(self, sides):
        self.__init__(sides)

def main():
    dices = []
    for i in range(6):
        dice1 = dice(6)
        print(dice1.sideUp)
        dices.append(dice)
    player1 = player()
    player1.turn()

def pick(x,choices,freeDice,Rvalue):
    if x == 0:
        return
    Rvalue += choices[x][1]
    freeDice -= choices[x][0]
    choices.pop(x)

def roll(number):
    dice = []
    for i in range(0,number):
        dice.append(random.randint(1,6)) 
    return dice
    
def showchoices(player,dice,freeDice):
    print('showing choices')
    
    Rvalue = 0
    get_indexes = lambda dice, xs: [i for (y, i) in zip(xs, range(len(xs))) if dice == y]
    one =   len(get_indexes(1,dice))
    two =   len(get_indexes(2,dice))
    three = len(get_indexes(3,dice))
    four =  len(get_indexes(4,dice))
    five =  len(get_indexes(5,dice))
    six =   len(get_indexes(6,dice))

    #score straight and 3 pairs
    numberOfFaces = [one,two,three,four,five,six]
    numberOfFaces.sort(reverse = True)
    print(numberOfFaces)
    if numberOfFaces[2] == 2:
        print('three pairs')
        freeDice = 0
        return 1500
    elif numberOfFaces[5]:
        print('straight')
        freeDice = 0
        return 2000
    choices = []
    choices.append([0,0,0])
    
    #score 1's
    if one == 1:
        choices.append([1,100,1])
    if one == 2:
        choices.append([1,100,1])
        choices.append([2,200,1])
    if one == 3:
        choices.append([1,100,1])
        choices.append([2,200,1])
        choices.append([3,1000,1])
    if one == 4:
        choices.append([1,100,1])
        choices.append([2,200,1])
        choices.append([3,1000,1])
        choices.append([4,2000,1])
    if one == 5:
        choices.append([1,100,1])
        choices.append([2,200,1])
        choices.append([3,1000,1])
        choices.append([4,2000,1])
        choices.append([5,4000,1])
    if one == 6:
        freeDice = 0
        return 8000

    #score 5's
    if five == 1:
        choices.append([1,50,5])
    if five == 2:
        choices.append([1,50,5])
        choices.append([2,100,5])
    if five == 3:
        choices.append([1,50,5])
        choices.append([2,100,5])
        choices.append([3,500,5])
    if five == 4:
        choices.append([1,50,5])
        choices.append([2,100,5])
        choices.append([3,500,5])
        choices.append([4,1000,5])
    if five == 5:
        choices.append([1,50,5])
        choices.append([2,100,5])
        choices.append([3,500,5])
        choices.append([4,1000,5])
        choices.append([5,2000,5])
    if five == 6:
        freeDice = 0
        return 4000
        
    #score 2's
    if two == 3:
        choices.append([3,200,2])
    if two == 4:
        choices.append([3,200,2])
        choices.append([4,400,2])
    if two == 5:
        choices.append([3,200,2])
        choices.append([4,400,2])
        choices.append([5,800,2])
    if two == 6:
        freeDice = 0
        return 1600
        
    #score 3's
    if three == 3:
        choices.append([3,300,3])
    if three == 4:
        choices.append([3,300,3])
        choices.append([4,600,3])
    if three == 5:
        choices.append([3,300,3])
        choices.append([4,600,3])
        choices.append([5,1200,3])
    if three == 6:
        freeDice = 0
        return 2400

    #score 4's
    if four == 3:
        choices.append([3,400,4])
    if four == 4:
        choices.append([3,400,4])
        choices.append([4,800,4])
    if four == 5:
        choices.append([3,400,4])
        choices.append([4,800,4])
        choices.append([5,1600,4])
    if four == 6:
        freeDice = 0
        return 3200
        
    #score 6's
    if six == 3:
        choices.append([3,600,6])
    if six == 4:
        choices.append([3,600,6])
        choices.append([4,1200,6])
    if six == 5:
        choices.append([3,600,6])
        choices.append([4,1200,6])
        choices.append([5,2400,6])
    if six == 6:
        freeDice = 0
        return 4800

    human = None
    while not human == 0:
    
        #are we dead?
        if len(choices) == 1:
            player.alive = False
            return 0 #score
       
        for choice in choices:
          print(' ')
          if choices.index(choice) == 0:
              if  not Rvalue == 0:
                  print('Choice 0: Stop rolling and save ' + str(Rvalue)) + '?'
          else:
              print('Choice '+ str(choices.index(choice))+': ' + str(choice[0]) +' '\
                + str(choice[2]) + '\'s for ' + str(choice[1]) + ' points?\n')
        
        human = input("choice #")
        pick(human,choices,freeDice,Rvalue)
             
    return Rvalue
    #group dice?

    #search for scoring combinations in dices

    #remove choices less than 1000

    #choices bring dice out of play (dice.inplay = False)?

    #store scoring combinations

    #make dice objects

    #put dices into collections

    #use methods on whole collection similar to array operator scalar ?
                    
class player:
    score = 0
    alive = True
    onTable = score > 1000
    dice = roll(6)
    print('player')
    
    def turn(self):
        currentscore = 0
        freeDice = 6
        self.alive = True
        print('turn')
        while self.alive:
            print('currentscore: ' + str(currentscore))
            print(self.dice)
            currentscore += showchoices(self,self.dice,freeDice)
            if freeDice == 0:
                self.dice = roll(6)
            else:
                self.dice = roll(freeDice)


main()
    
