import time
from dice import dice
from player import player

#game object
##game setup
###number of players (default 2)

def main():
    dices = []
    for i in range(6):
        dice1 = dice()
        dices.append(dice1)
    player1 = player('Mona')
    player2 = player('Andreas')
    while player1.score < 10000 and player2.score < 10000:
        turn(player1,dices)
        time.sleep(5)
        turn(player2,dices)
    if player1.score < 10000:
        print('Reaced 10000 or more! Score: ' + str(player1.score))
    elif player2.score < 10000:
        print('Reaced 10000 or more! Score: ' + str(player2.score))
    time.sleep(60)

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
    one,two,three,four,five,six = countAllFaces(diceList)

    #score straight and 3 pairs
    numberOfFaces = [one,two,three,four,five,six]
    numberOfFaces.sort(reverse = True)
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
            print('Choice '+ str(choices.index(choice)) + ': ' + str(choice[0]) +' '\
            + str(choice[2]) + '\'s for ' + str(choice[1]) + ' points?\n')
        while bad:
            try:
                answer = int(input('Pick : '))
                bad = False
            except ValueError:
                bad = True
    else:
        print('Choice 0: ' + str(choices[0][0]) +' '\
            + str(choices[0][2]) + '\'s for ' + str(choices[0][1]) + ' points?\n')
        print('Pick : 0')
        answer = 0
    return answer
    

def turn(player,diceList:list):
    currentscore = 0
    player.alive = True
    print('\n\n###################################################################################\nTurn for')
    print(player)
    while player.alive:
        print('current score: ' + str(currentscore) + '\nDICE:')
        print(*diceList)

        #find Choices from first throw
        choices = findChoices(diceList)

        #no choices means bad luck turn over already
        if len(choices) == 0:
            print('BAD LUCK!\nNothing to save on this throw!\n')
            break

        #while choices available
        while len(choices):
            choices = findChoices(diceList)
            if choices[0][0]==6:
                currentscore += choices[0][1]
                choices = []
                continue
            playerPick = -1
            while not -1 < playerPick < len(choices):
                playerPick = askPick(choices)

            #asking player for choice and removing same dice choice form choices
            numDice,score,face,choices = pick(playerPick,choices)

            #saving the choice score
            currentscore += score

            #setting dice to saved
            for element in diceList:
                if element.sideUp == face and numDice:
                    numDice -= element.save(face)
            
            #if there are more choices ask player to pick another?
            while not playerPick=="y" and not playerPick == "n" and len(choices):
                playerPick = input('Do you want to pick another? (y/n): ')
            if playerPick == "y":
                continue
            elif playerPick == "n":
                break

        #counting number of free dice
        freeDice = sum(map(lambda dice: int(not dice.saved),diceList))

        #no free dice means you HAVE to roll again (rules of the game)
        if not freeDice or freeDice == 6:
            print('Rolling 6 dice again!')
            diceList = [dice.rollSaved() for dice in diceList]

        #else the player can choose to stop and save, if player is on table or currentscore is over 1000
        else:
            rollAgain = None           
            print('player on table: ' + str(player.onTable()))
            print(int(currentscore))
            if player.onTable() or currentscore > 999:
                while not rollAgain=="y" and not rollAgain == "n":
                    rollAgain = input('Do you want to roll remaining ' + str(freeDice) + '? (y/n): ')
            else:
                print(player)
                print('Is not on table yet, and current score is less than 1000, have to roll again.\n')
            print('')
            if not rollAgain == "n":
                print('Rolling ' + str(freeDice) + ' again!')
                diceList = [dice.roll() for dice in diceList]
            else:
                break

    #turn done saving and showing results
    player.addScore(currentscore)
    print('turn done for '+str(player))

    #rolling for next player
    diceList = [dice.rollSaved() for dice in diceList]

main()
    
