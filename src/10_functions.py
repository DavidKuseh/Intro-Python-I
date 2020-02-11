# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(num):
    if num % 2 == 0:
        return true

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_even_or_odd(num):
    if num % 2 == 0 and num !=0:
        return ("Even!")
    elif (num % 2) == 1:
        return ("Odd")
