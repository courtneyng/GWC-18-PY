from random import *
aRandomNumber = randint(1, 10)

guesses = 0

for i in range(3):
#while guesses < 3:
    guesses += 1
    guess = input("Guess a number between 1 and 10 (inclusive): ")
    guess = int(guess)

    if guess == aRandomNumber:
        print("You got the right answer")
        break
    else:
        print("You got the wrong answer")
        if guess > aRandomNumber:
            print("Try to guess lower")
        else:
            print("Try to guess higher")
print("Game Over")
