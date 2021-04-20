# Program ID: hangman
# Author: Courtney Ng & Jasmine Li
# Period: 7
# Program Description: Using the character split to create hangman game
# This Part we just don't get it


yes = "yes"
no = "no"
ans = input("Do you want to play hangman?")
if ans == yes:
    word = input("Insert a word")
    print("You have 6 tries. ;^)")
    # variable
    guesses = []

    turns = 6

    # check turns
    while turns > 0:

        # counter
        failed = 0


        for char in word:

        # see if the char in player guess
            if char in guesses:
                print(char),

            else:

            # print underscore if not there
                print("_"),

            # and increase fail counter
                failed += 1

        # if failed is equal to zero

        if failed == 0:
            print("good job you win")

            break

        guess = input("guess a character:")

        # set player guess to guesses
        guesses += guess

        # if the guess is not found in the word
        if guess not in word:

         # decrease counter
            turns -= 1

            print("letter not found")

            print ("you have this many turns:")
            print(turns)

        # no more turns
            if turns == 0:
                print("you lost.. ;^( ")
else:
    print("Okay bye.. ;^( ")
