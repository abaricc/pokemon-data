from pokemonDef import Monster
import pokemonFunctions as pf
import sys
import random

#First, read all the pokemon types and put them in a dictionary, pairs are (name, listOfTypes).
dictionaryOfNamesAndTypes=pf.readPokemonTypesFromFileDictionary("listOfPokemon1.txt")
#print(dictionaryOfNamesAndTypes)

# Then, read all pokemon from a file and put them on a list (the types are not correctly updated)
pokeList=pf.readPokemonListFromFile("listOfPokemon2.txt")
#print("\n \n "+str(pokeList))
#print("length of the list "+str(len(pokeList))+" "+str(pokeList))

#TASK A,
# Put all pokemon in a dictionary, the key will be the name of the pokemon
# and the value will be the　tuple containing the pokemon, its characteristics and its list of types
pokedex={}
for monster in pokeList:
    pokedex[monster.name]=monster

#print(pokedex)

# Task B, using the two dictionaries that you now have, pokedex and dictionaryOfNamesAndTypes,
# modifiy the entries in pokedex to include types
pokeTypes={}
for key,value in pokedex.items():
    currentList=dictionaryOfNamesAndTypes[key]
    for type in currentList:
        value.variety.append(type)

#print("\n\n\n\n"+str(pokedex))

#now we can make monsters fight by doing:
#pf.battle(pokedex["Bulbasaur"],pokedex['Charmander'])
#or also
#pf.battle(pokeList[8],pokeList[137])

#random battle
fighter1=pokeList[random.randint(0,len(pokeList)-1)]
fighter2=pokeList[random.randint(0,len(pokeList)-1)]

winner=pf.battle(fighter1,fighter2,False,False)
if winner==0: print(" The pokemon that won the battle was: "+fighter1.name)
elif winner==1: print(" The pokemon that won the battle was: "+fighter2.name)
else: print("The battle ended in a draw! ")
