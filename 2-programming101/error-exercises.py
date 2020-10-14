# 1. Create a program that asks the user for a number and then prints from that number to 0.
#       Handle the error if the user enters something other than a number.
print("**Problem 1**")
try:
    my_number = int(input("Please give a number.\n"))
except ValueError:
    print("I said a number!")



# 2. Create a program that ask a user for two numbers and then returns the sum (add), product(multiply), and quotient (division) of the two numbers.
#       Catch all errors possible from the user and explicitly tell the user what caused the error.

print("**Problem 2**")
try:
    number_1 = int(input("Give me a number!\n"))
    number_2 = int(input("I know I just asked, but another number, please?\n"))
    sum = number_1 + number_2
    print(f"The sum is {sum}")
    product = number_1 * number_2
    print(f"The product is {product}")
    quotient = number_1 / number_2
    print(f"The quotient is {quotient}")
except ValueError:
    print("I said a number! You need to give me a number! No letters or symbols.")
except ZeroDivisionError:
    print("You can't divide by zero! One of your numbers was zero! No quotient for you!")
