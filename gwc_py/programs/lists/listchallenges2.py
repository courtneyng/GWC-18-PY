from random import *    

sides = ["Mashed Potatoes", "Broccoli", "French Fries", "Onion Rings", "Grapes"]
main = ["Spaghetti", "Fettuccine", "Linguine", "Tortellini", "Ravioli"]
desserts = ["Gelato", "Tiramisu", "Canoli", "Semifreddo", "Panna Cotta"]
#aList = [0, 1]

aRandomSide = randint(0, len(sides)-1)
aRandomMain = randint(0, len(main)-1)
aRandomDessert = randint(0, len(desserts)-1)
#aRandomIndex = randint(0, len(aList)-1)


print ("Your side dish is:", sides[aRandomSide])
print ("Your main dish is:", main[aRandomMain])
print ("Your dessert is:", desserts[aRandomDessert])
