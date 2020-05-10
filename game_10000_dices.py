import time
from dice import dice
from player import player


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
    player1 = player()
    while player1.score < 10000:
        turn(player1,dices)
        time.sleep(5)
    print('Reaced 10000 or more! Score: ' + str(player1.score))

def countFace(diceList:list,face):
    returnValue = 0
    for dice in diceList:
        if dice.sideUp == face and not dice.saved:
            returnValue += 1
    return returnValue

def countAllFaces(diceList):
    return (countFace(diceList,1),countFace(diceList,2),countFace(diceList,3),countFace(diceList,4),countFace(diceList,5),countFace(diceList,6))

def pick(x: int,choices: list):
    numDice,score,face = choices[x]
    for i in range(len(choices)-1,-1,-1):
        if choices[i][2]== face:
            choices.pop(i)
    return numDice,score,face,choices
    
def findChoices(diceList):
    print('finding choices')
    one,two,three,four,five,six = countAllFaces(diceList)

    #score straight and 3 pairs
    numberOfFaces = [one,two,three,four,five,six]
    numberOfFaces.sort(reverse = True)
    print(numberOfFaces)
    if numberOfFaces[2] == 2:
        print('three pairs')
        return [[6,1500,0]]
    elif numberOfFaces[5]:
        print('straight')
        return [[6,2000,0]]
    choices = []
    
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
        return [[6,8000,1]]

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
        return [[6,4000,5]]
        
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
        return [[6,1600,2]]
        
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
        return [[6,2400,3]]

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
        return [[6,3200,4]]
        
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
        return [[6,4800,6]]

    #https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/

    return choices

    #search for scoring combinations in dices

    #remove choices less than 1000

def askPick(choices: list):
    bad = True
    if not len(choices) == 1:
        for choice in choices:
            print(' ')
            print('Choice '+ str(choices.index(choice)) + ': ' + str(choice[0]) +' '\
            + str(choice[2]) + '\'s for ' + str(choice[1]) + ' points?\n')
        while bad:
            try:
                answer = int(input('Pick : '))
                bad = False
            except ValueError:
                bad = True
    else:
        print('Pick : 0')
        answer = 0
    return answer
    

def turn(player,diceList:list):
    currentscore = 0
    player.alive = True
    print('turn')
    while player.alive:
        print('currentscore: ' + str(currentscore))
        print(*diceList)
        choices = findChoices(diceList)
        if len(choices) == 0:
            break
        while len(choices):
            choices = findChoices(diceList)
            if choices[0][0]==6:
                currentscore += choices[0][1]
                choices = []
                continue
            playerPick = -1
            while not -1 < playerPick < len(choices):
                playerPick = askPick(choices)
            numDice,score,face,choices = pick(playerPick,choices)
            currentscore += score
            for element in diceList:
                if element.sideUp == face and numDice:
                    numDice -= element.save(face)
            while not playerPick=="y" and not playerPick == "n" and len(choices):
                if player.onTable or currentscore > 999:
                    playerPick = input('Do you want to pick another? (y/n): ')
                else:
                    continue
            if playerPick == "y":
                continue
            elif playerPick == "n":
                break
        freeDice = sum(map(lambda dice: int(not dice.saved),diceList))
        print("freeDice: " + str(freeDice))
        if not freeDice:
            diceList = [dice.rollSaved() for dice in diceList]
        else:
            diceList = [dice.roll() for dice in diceList]
    player.addScore(currentscore)
    print('player score: ' + str(player.score))
    print('turn done')
    diceList = [dice.rollSaved() for dice in diceList]

main()
    
