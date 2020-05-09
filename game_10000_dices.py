from dice import dice


#game object
##game setup
###number of players (default 2)
###create dices
###dices lists
####roll list
####grouped list


def main():
    dices = []
    for i in range(6):
        dice1 = dice()
        dices.append(dice1)
    print(*dices)
    player1 = player()
    player1.turn(dices)

def countFace(diceList,sideUp):
    returnValue = 0
    for dice in diceList:
        if dice.sideUp == sideUp:
            returnValue += 1
    return returnValue

def countAllFaces(diceList):
    return (countFace(diceList,1),countFace(diceList,2),countFace(diceList,3),countFace(diceList,4),countFace(diceList,5),countFace(diceList,6))

def pick(x,choices,freeDice,Rvalue):
    if x == 0:
        return
    Rvalue += choices[x][1]
    freeDice -= choices[x][0]
    choices.pop(x)
    
def showchoices(player,diceList):
    print('showing choices')
    
    Rvalue = 0
    one,two,three,four,five,six = countAllFaces(diceList)

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

    #search for scoring combinations in dices

    #remove choices less than 1000

    #choices bring dice out of play (dice.inplay = False)?

    #put dices into collections

    #use methods on whole collection similar to array operator scalar ?
                    
class player:

    def __init__(self):
        self.score = 0
        self.alive = True
        print('player')
    
    def onTable(self):
        return self.score > 1000

    def turn(self,diceList):
        currentscore = 0
        self.alive = True
        print('turn')
        while self.alive:
            print('currentscore: ' + str(currentscore))
            print(*diceList)
            currentscore += showchoices(self,diceList)
            print("map: " + map(lambda dice: int(not dice.saved),diceList))
            if freeDice == 0:
                diceList = map(lambda dice: dice.rollSaved, diceList)
            else:
                diceList = map(lambda dice: dice.rollUnSaved, diceList)

main()
    
