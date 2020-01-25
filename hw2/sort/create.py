import random

#Create a random list of ints
def createRandomIntList(numInts,xMin=0,xMax=100):
    listOfInts=[]

    for i in range(numInts):
        listOfInts.append(random.randint(xMin,xMax))

    return listOfInts

