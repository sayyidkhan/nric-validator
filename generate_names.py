import names

def generateNames(myFunction):
    myList = []

    while(len(myList) != 1000):
        myName = myFunction()
        if(myName in myList):
            continue
        else:
            myList.append(myName)

    return myList

def readFromList(myList):
    for item in myList:
        print(item)



myList = generateNames(names.get_last_name)
readFromList(myList)

#https://pypi.org/project/names/