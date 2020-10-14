#1. Create a program that prompts the user for a number and compare that number with random number of your choice.
    # If the number is too high tell the user.
    # If the number is too low tell the user.
    # If the number is correct tell the user.

favorite_number = int(input("What is your favorite number? I wonder if ours are the same...\n"))

if favorite_number == 23:
    print("You have the perfect favorite number! Just like me!")
elif favorite_number < 23:
    print("Wow, that number is too small! Try again to guess mine!")
elif favorite_number >50:
    print("That's way too big! You like big numbers and I cannot lie! hehehe....")
else:
    print("That's too big!")