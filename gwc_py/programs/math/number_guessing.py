# Program ID: number_guessing
# Author: Courtney Ng
# Period: 7
# Program Description: Modifying the word guessing.

number = 2
answer = int(input("I am thinking of a number 1-10. What is it?"))




# while word != answer:
#     print ("That is incorrect.")
#     answer = input ("Please try again.")

while number != answer:
    if answer > number:
        print ("That was too high.")
        answer = int(input ("Try again."))
    else:
        if answer < number:
            print ("That was too low ")
            answer = int(input ("Try again."))



print ("Congrats! You have guessed the correct number!")