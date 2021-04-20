# Program ID: math_functions
# Author: Courtney Ng
# Period: 7
# Program Description: create math functions

a = abs(int(input("Pick a number for the absolute value")))
print ("The number you chose for the absolute was =", a)
r = round(int(input("Pick a number to round")))
print ("The number you chose to round was", r)
x = int(input("Insert the first number for the modulo function"))
y = int(input("Insert the second number for the modulo function"))
print ("It will be x divided by y and then you will get the modulo function")
modulo = x % y
w = int(input("Insert the first number for the integer division"))
z = int(input("Insert the second number for the integer division"))
print ("It will be w divided by z and then you will get the integer division")
int_div = w // z
print (a, r, modulo, int_div)