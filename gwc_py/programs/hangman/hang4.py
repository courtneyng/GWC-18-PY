from random import *
words = ["gray"]
chosen = randint(0, len(words)-1)
Word = words[chosen]
guesses = 7

for i in range (0, len(Word)):
    dashes = "_" * len(Word)
print(dashes)

guessed = []
while guesses > 0:
    guess = input("Please guess a lowercase letter: ")

    if guess.isnumeric():
        print("That's not a lowercase letter! Try again. ")
        print()

    elif guess.isupper():
        print("That's not a lowercase letter! Try again. ")
        print()

    elif guess in guessed:
        print("You already guessed this letter! Try again. ")
        print()

    elif len(guess) > 1:
        print("That's not a lowercase letter! Try again. ")
        print()

    else:
        guessed.append(guess)
        if guess in Word:
            for x in range(len(Word)):
                if guess == Word[x]:
                    dashes = dashes[:x] + guess + dashes[x+1:]
            print(dashes)
            if dashes == Word:
                print("You won! Thanks for playing!")
                break
            print("You have", guesses, "guesses left.")
            print("You have already guessed:", * guessed)
        else:
            guesses-=1
            print("Wrong! You have", guesses, "guesses left.")
            print("You have already guessed:", * guessed)
            print(dashes)
            continue
if guesses == 0:
    print("You lost! The word was", Word, ".")
