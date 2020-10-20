# Scope - the place in a program where a declared variable can be accessed


# Global Scope!

x = 10 #<--has global scope and can be recalled throughout this program

def add_to_x(a):
    return x + a

print(add_to_x(12)) #<--x remains 10
print(add_to_x(33))

# Local Scope!

def add_two_numbers(a, b):
    c = a + b #<---local scope! This is inside the function and can only be used within. Outside the function, c doesn't have meaning.
    return c
print(add_two_numbers)
# print(c) <--will error, c is not defined outside of the function

def repeat_stuff():
    x = 10
    def update_x():
        return x + x
    
    while x < 100:
        x = update_x()
        print(x)

#update_x cannot be accessed outside 
repeat_stuff()

## Cannot modify a global inside of a function
x = 10
def change_x_to(newX):
    x = newX
    print(x)
    return x

change_x_to(15) #prints 15..yea! x is 15
print(x) #x is 10? WTH?!?

# How to make a global variable within the function!
# You must declare a global variable before the variable is defined
# def change_x_to(newX):
#     global x #saying 'Hey x if your global stay that way or be a global var if not already created'
#     x = newX
#     print(x)
#     return x

change_x_to(15)
print(x)

# Using as few global variables as possible is ideal
# Global variables should be constants...

# Global variable conditionally set is possible... but not a best practice
number = int(input("Give me a number:\n"))
if number > 10:
    x = number * 10

print(x)#if user entered <9 then it will error






