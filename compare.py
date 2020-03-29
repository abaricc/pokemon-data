from pokemonDef import Monster
import pokemonFunctions as pf
import sys
import random
import operator


def fillPokedex(pokedex, dictionaryOfNamesAndTypes, pokeList):
    for monster in pokeList:
        pokedex[monster.name]=monster
    for key,value in pokedex.items():
        currentList=dictionaryOfNamesAndTypes[key]
        for type in currentList:
            value.variety.append(type)

def countScores(pokeScore):
    for number1 in range(1, pokeListSize//2):
        fighter1=pokeList[number1]
        for number2 in range(pokeListSize//2, pokeListSize):
            fighter2 = pokeList[number2]
            for i in range(5):
                if fighter1!=fighter2:
                    winner=pf.battle(fighter1,fighter2,True,False)
                    if winner==0:
                        pokeScore[fighter1.name] += 2
                    elif winner==1:
                        pokeScore[fighter2.name] += 2
                    #else:
                        #pokeScore[fighter1.name] += 1
                        #pokeScore[fighter2.name] += 1
    pokeScore = sorted(pokeScore.items(), key=operator.itemgetter(1))
    for i in range(1,12):
        print(pokeScore[pokeListSize-i])

def countScores2(topLimit):
    pokeScore = {}
    for poke in range(pokeListSize):
        pokeScore[poke]=0
    for number1 in range(1, pokeListSize//2):
        fighter1=pokeList[number1]
        for number2 in range(pokeListSize//2, pokeListSize):
            fighter2 = pokeList[number2]
            for i in range(3):
                if fighter1!=fighter2:
                    winner=pf.battle(fighter1,fighter2,True,False)
                    if winner==0:
                        pokeScore[number1] += 1
                    elif winner==1:
                        pokeScore[number2] += 1
    pokeScore = sorted(pokeScore.items(), key=operator.itemgetter(1))
    topList = []
    for i in range(1,topLimit+1):
        topList.append(pokeScore[pokeListSize-i])
    return topList

def fillWins(pokeWins):
    for number1 in range(1, pokeListSize//2):
        fighter1=pokeList[number1]
        for number2 in range(pokeListSize//2, pokeListSize):
            fighter2 = pokeList[number2]
            if fighter1!=fighter2:
                winner=pf.battle(fighter1,fighter2,True,False)
                if winner==0:
                    pokeWins[number1][number2]=True
                elif winner==1:
                    pokeWins[number2][number1]=True

def countWins(pokeWins, pokeNumber):
    size=0
    for number2 in range(pokeListSize):
        if pokeWins[pokeNumber][number2]==True:
            size=size+1
    return size

def countUnion(pokeWins, team):
    size=0
    for number in range(pokeListSize):
        if pokeWins[team[0]][number]==True: size=size+1
        elif pokeWins[team[1]][number]==True: size=size+1
        elif pokeWins[team[2]][number]==True: size=size+1
        elif pokeWins[team[3]][number]==True: size=size+1
        elif pokeWins[team[4]][number]==True: size=size+1
        elif pokeWins[team[5]][number]==True: size=size+1
    return size

if __name__=="__main__":
    dictionaryOfNamesAndTypes=pf.readPokemonTypesFromFileDictionary("listOfPokemon1.txt")
    pokeList=pf.readPokemonListFromFile("listOfPokemon2.txt")
    pokeListSize = len(pokeList)
    pokedex = {}
    fillPokedex(pokedex, dictionaryOfNamesAndTypes, pokeList)

    #>>> Finnt strongest Pokemon
    ##pokeScore = {}
    ##print("Top pokemons: ")
    ##for monster in pokeList:
    ##    pokeScore[monster.name]=0
    ##countScores(pokeScore)

    #>> Find strongest team
    pokeWins = []
    for number1 in range(pokeListSize):
        pokeWins.append([])
        for number2 in range(pokeListSize):
            pokeWins[number1].append(False)
    fillWins(pokeWins)
    #print(pokeWins)

    topSize = 35
    topList = countScores2(topSize)
    topListSize = len(topList)
    print("Top pokemons: ")
    print(topList)
    print()
    print("Number of top pokemons used in teams: "+str(topListSize))
    print()

    # Create teams
    teams = []
    for n1 in range(0, topListSize-1):
        for n2 in range(n1+1,topListSize):
            for n3 in range(n2+1,topListSize):
                for n4 in range(n3+1,topListSize):
                    for n5 in range(n4+1,topListSize):
                        for n6 in range(n5+1,topListSize):
                            teams.append([topList[n1][0],topList[n2][0],topList[n3][0],topList[n4][0],topList[n5][0],topList[n6][0]])
    #print(teams)

    # Count union for each team
    unions = []
    for i in range(len(teams)):
        unions.append([countUnion(pokeWins, teams[i]), teams[i]])

    #print("Unions:")
    #for i in range(len(unions)):
    #    print(unions[i][0])

    # Find max union
    max=unions[0][0]
    for i in range(len(unions)):
        if unions[i][0]>max: max = unions[i][0]
    print("Max union: "+str(max))
    print()

    #Print team with the max union
    print("Top pokemon team:")
    for i in range(len(unions)):
        if unions[i][0]==max:
            for pokeNumber in range(6):
                print(pokeList[unions[i][1][pokeNumber]].name)
            break
