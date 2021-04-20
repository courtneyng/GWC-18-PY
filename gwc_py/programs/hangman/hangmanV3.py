word = input("Type a word for someone to guess: ")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")

# Some useful variables
guesses = []
maxfails = 7


guess = input("Guess a letter: ")

    # check turns
while maxfails > 0:
    failed = 0 # counter

    for char in word: # see if the char in player guess
        if char in guesses:
            print(char),

        else:
            print("_"), # print underscore if not there
            failed += 1 # increase fail counter

        # if failed is equal to zero
    if failed == 0:
        print("good job you win")
        break

    guess = input("guess a character:")
    guesses += guess # set player guess to guesses

        # if the guess is not found in the word
    if guess not in word:
        maxfails -= 1 # decrease counter

        print("letter not found")
        print ("you have this many turns:")
        print(maxfails)

        # no more turns
        if maxfails == 0:
            print("you lost.. ;^( ")
