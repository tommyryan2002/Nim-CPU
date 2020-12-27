from collections import OrderedDict
rowsasDict = {"row1": [], "row2": [], "row3": []}
rowsasList = [7, 5, 3]
nimSum = []
ralTemp = []
playerTurn = True
gameOver = False
import random
turnCount = 0

#counts the multpiples in each row to find the nim sum
def findnimSum(list):
    x = 1
    for i in list:
        oneCount = 0
        twoCount = 0
        fourCount = 0
        num = i
        if num >= 4:
            fourCount += 1
            num -= 4
            if num >= 2:
                twoCount +=1
                num -= 2
                if num >= 1:
                    num -= 1
                    oneCount += 1
            elif num >= 1:
                num -= 1
                oneCount += 1
        elif num >= 2:
            num -= 2
            twoCount += 1
            if num >= 1:
                num -= 1
                oneCount += 1
        elif num >= 1:
            num -= 1
            oneCount += 1
            
        rowsasDict["row" + str(x)] = [fourCount, twoCount, oneCount]
        x += 1
        
    global nimsumFour
    global nimsumTwo
    global nimSum
    global nimsumOne
    #finds the total nimsum from the count of the multiples
    nimsumFour = ((rowsasDict["row1"][0]) + (rowsasDict["row2"][0]) + (rowsasDict["row3"][0]))
    nimsumTwo = ((rowsasDict["row1"][1]) + (rowsasDict["row2"][1]) + (rowsasDict["row3"][1]))
    nimsumOne = ((rowsasDict["row1"][2]) + (rowsasDict["row2"][2]) + (rowsasDict["row3"][2]))
    nimSum = [nimsumFour % 2, nimsumTwo % 2, nimsumOne % 2]



def findoptimalMove():
    global rowsasList
    findnimSum(rowsasList)
    complete = False
    rowCycle = 0
    #checks if there is a row of [0, 0, n]
    if (rowsasList[0] == 0 and rowsasList[1] == 0 and rowsasList[2] > 1) or (rowsasList[0] == 0 and rowsasList[1] > 1 and rowsasList[2] == 0) or (rowsasList[0] > 1 and rowsasList[1] == 0 and rowsasList[2] == 0):
        for i in rowsasList:
            if i > 1:
                rowsasList[rowCycle] = rowsasList[rowCycle] - (i - 1)
                break
            rowCycle += 1
        return
    #checks if there is a row of [0, 1, n > 0] or any combo.
    if (rowsasList[0] == 0 and rowsasList[1] == 1 and rowsasList[2] > 0) or (rowsasList[0] == 1 and rowsasList[1] == 0 and rowsasList[2] > 0) or (rowsasList[0] == 0 and rowsasList[1] > 0 and rowsasList[2] == 1) or (rowsasList[0] == 1 and rowsasList[1] > 0 and rowsasList[2] == 0) or (rowsasList[0] > 0 and rowsasList[1] == 0 and rowsasList[2] == 1) or (rowsasList[0] > 0 and rowsasList[1] == 1 and rowsasList[2] == 0):
        for i in rowsasList:
            if i > 1:
                rowsasList[rowCycle] = rowsasList[rowCycle] - i
                break
            rowCycle += 1
        return
    #checks if there is a row of [1, n, 1]
    if (rowsasList[0] > 1 and rowsasList[1] == 1 and rowsasList[2] == 1) or (rowsasList[0] == 1 and rowsasList[1] > 1 and rowsasList[2] == 1) or (rowsasList[0] == 1 and rowsasList[1] == 1 and rowsasList[2] > 1):
        for i in rowsasList:
            if i > 1:
                rowsasList[rowCycle] = rowsasList[rowCycle] - (i - 1)
                break
            rowCycle += 1
        return
    if rowsasList == [1, 1, 1]:
        nogoodMove()
        return
    #checks if nimSum already == 0
    if nimSum == [0, 0, 0]:
        nogoodMove()
        return
    #If not an edge case this moves towards nimSum = 0
    for i in rowsasList:
        ralTemp = rowsasList.copy()
        x = ralTemp[rowCycle]
        for j in range(0, i):
            #print("looped:" + str(j))
            findnimSum(ralTemp)
            ralTemp[rowCycle] = ralTemp[rowCycle] - 1
            findnimSum(ralTemp)
            if nimSum == [0, 0, 0] and sum(ralTemp) >= 3 :
                rowsasList = ralTemp
                #print(rowsasList)
                #print("testers")
                complete = True
                break
            else:
                #print(ralTemp)
                pass
        rowCycle += 1    
        if complete:
            break
        
def nogoodMove():
    #[0, n, n]
    if (rowsasList[0] == 0 and rowsasList[1] > 0 and rowsasList[2] > 0):
        if rowsasList[1] > rowsasList[2]:
            rowasList[1] -= 1
        else:
            rowsasList[2] -= 1
    #[n, 0, n]
    elif (rowsasList[0] > 0 and rowsasList[1] == 0 and rowsasList[2] > 0):
        if rowsasList[0] > rowsasList[2]:
            rowasList[0] -= 1
        else:
            rowsasList[2] -= 1
    #[n, n, 0]
    elif (rowsasList[0] > 0 and rowsasList[1] > 0 and rowsasList[2] ==0):
        if rowsasList[0] > rowsasList[1]:
            rowasList[0] -= 1
        else:
            rowsasList[1] -= 1
    else:
        x = random.randint(0,2)
        rowsasList[x] -= random.randint(1, (rowsasList[x]))
    
print("Welcome to 7 5 3!")
print("To play: On your turn you may take as many tokens as you like from any one row ")
print("Make your opponent take the very last token from all the rows to win!")  
print("Have fun and Good Luck!")
#for i in range(0,3):
    #num = int(input("enter amount in rows: "))
    #rowsasList.append(num)

while gameOver != True:
    while True:
        if turnCount == 0:
            goFirst = input("Do you want to go first [Y/N]: ")
            if goFirst == "Y" or goFirst == "y":
                playerTurn = True
                break
            if goFirst == "N" or goFirst == "n":
                playerTurn = False
                break
            else:
                print("Invalid Input, try again!")
        else: break
    if sum(rowsasList) <= 1 and playerTurn != True:
        gameOver = True
        print("You Win! Well played...")
        break
    if sum(rowsasList) <= 1 and playerTurn:
        gameOver = True
        print("GG I win")
        break
    elif playerTurn != True:
        print("my turn!")
        findoptimalMove()
        #print(" ", rowsasList)
        playerTurn = True
    
    elif playerTurn:
        print("current rows: ")
        print(" ",rowsasList)
        while True:
            try:
                rowTake = int(input("Which row do you want to take from [1, 2, or 3]: "))
                numTake = int(input("How many do you wish to take: "))
                break
            except:
                print("Invalid Input, try again!")
        if numTake > rowsasList[rowTake -1] or (numTake < 1):
            print("You can't do that! Try again.")
        else:
            rowsasList[(rowTake - 1)] -= numTake
            print("current rows: ")
            print(" ",rowsasList)
            playerTurn = False
        turnCount += 1
    

