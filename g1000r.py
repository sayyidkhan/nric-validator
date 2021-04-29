from generator import generateNRIC

myList = []

while(len(myList) != 1000):
    nric = generateNRIC()
    if(nric in myList):
        continue
    else:
        myList.append(nric)


def printResult(myList):
    for items in myList:
        print(items)

printResult(myList)

