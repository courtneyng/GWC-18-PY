#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = [0, 1]
names = ["Ben", "Paul", "Jonas", "Elias", "Leon", "Finn", "Noah", "Louis", "Lucas", "Felix", "Luca", "Maximilian", "Henry", "Max", "Oscar", "Emi", "Anton"]

#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)

aRandomName = randint(0, len(names)-1)
# print (aList[aRandomIndex])
print (names[aRandomName])
