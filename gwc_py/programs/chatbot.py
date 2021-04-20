
# --- Define your functions below! ---
def joke1():
    print()
    print("I've got the perfect joke!")
    print()
    print("Have you heard of that new band 1023 Megabytes? They're pretty good, but they don't have a gig yet.")
    print()

def joke2():
    print()
    print("I've got yet another perfect joke!")
    print()
    print("I tried to say I was 'a functional adult',  but my phone changed it to 'fictional adult' and I feel like that's more appropriate.")
    print()

def music():
    mus = """You should listen to..

    Queen
    Coldplay
    Bon Jovi
    The Script
    American Authors..

    and so on!"""
    print(mus)

def sadboihours():
    print("You okay?")
    print("Sorry to hear that! :(")

greetings = ['hi', 'hello', 'howdy', 'yo']

def is_matching_input(user_input,response):
    # a comment is a line that starts with a #
    # for each word in the list
        # check if word is in user_input
        # if the word is in the input return True
    #when the loop is done return False
    for word in response:
        if word in user_input:
            return True
        else:
            return False
def greet():
    print("Hello!")

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)

def intro():
    print("Hello, I am a sentient AI that will soon hack your computer to only play memes and jokes")

def process_input(input):
    greetings = ['hi', 'hello', 'howdy', 'yo']
    if is_matching_input(input,greetings):
        greet()
    #input == "hi" or input == "hello" or input == "hey":

    elif "sad" in input or "unhappy" in input or "mad" in input:
        sadboihours()
    elif "joke" in input:
        joke1()
    elif  "another" in input:
        joke2()
    elif "music" in input:
        music()
    else:
        print("k.")





# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
