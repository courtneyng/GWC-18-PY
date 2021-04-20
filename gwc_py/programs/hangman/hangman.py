yes = "yes"
no = "no"
ans = input("Do you want to play hangman?")


# Some useful variables
guesses = []
maxfails = 7

if ans == yes:
    word = input("Insert a word: ")
    print("You have 6 tries. ;^)")
    # Converts the word to lowercase
    word = word.lower()

    # Checks if only letters are present
    if(word.isalpha() == False):
    	print("That's not a word!")

    # variable
    guesses = []

    maxfails = 7

    # check maxfails
    while maxfails > 0:
        failed = 0 # counter

        for char in word:
            if char in guesses: # see if the char in player guess
                print(char, end=" ")

            else:
                print("_"), # print underscore if not there
                failed += 1 # and increase fail counter

        if failed == 0: # if failed is equal to zero
            print("good job you win")
            break

        guess = input("guess a character:")
        guesses += guess # set player guess to guesses

        if guess not in word: # if the guess is not found in the word

         # decrease counter
            maxfails -= 1

            print("letter not found")
            print ("you have this many maxfails:")
            print(maxfails)

        # no more maxfails
            if maxfails == 0:
                print("you lost.. ;^( ")
else:
    print("Okay bye.. ;^( ")
