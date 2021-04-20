guessedList = []

# Executioner
word = input("Enter a word")
charList = list(word) # makes each letter own element
length = len(word)
yes = "yes"
no = "no"

ans = input("Do you want to play hangman?")
while ans == yes:
    for char in word:
        guessedList.append("_")
    guess = input("Insert a letter")
    guessedList.append(guess)


for x in range(0, len(word)):
            if word[x] == guess:
                guessedList[x] = guess
                print(guessedList)
