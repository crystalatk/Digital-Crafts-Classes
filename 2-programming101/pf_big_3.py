# 3. Guess a Number
# You will implement a guess-the-number game where the player has 
# to try guessing a secret number until they gets it right. 
# For now, you will "hard code" the secret number to 5 
# (just set it to five like secret_number = 5). 
# You will prompt the player to enter a number again and again, 
# each time comparing their input to the secret number. 
# To to that, you will need to write a while loop. 
# If they guess correctly, you will print "You win!", otherwise, 
# you will prompt for a number again.

# secret_number = 5
# user_guess = int(input("I am thinking of a number between 1 and 10.\n Guess my number!\nFirst guess: "))

# while user_guess != secret_number:
#     print("Nope! You lose!")
#     user_guess = int(input("Just kidding, try again!\nNew guess: "))
# print("You got it! You get a gold star!")

# step 2: Give High-Low Hint
# Improve your game to provide the player with a high-or-low hint.

# secret_number = 5
# user_guess = int(input("I am thinking of a number between 1 and 10.\n Guess my number!\nFirst guess: "))

# while user_guess != secret_number:
#     if user_guess < secret_number:
#         print("Nope! You lose!")
#         user_guess = int(input(f"Just kidding, {user_guess} is too low!\nNew guess (hint:try something higher!): "))
#     else:
#         print("No Way!")
#         user_guess = int(input(f"{user_guess} is so big! Try going lower.\nNew guess: "))
# print("You got it! You get a gold star!")


# Step 3: Randomly Generated Secret Number
# Instead of hard-coding the secret number to 5 now, 
# you will generate the secret number using a random number generator 
# provided by Python, so that even you, the programmer, 
# cannot know the secret number before hand. 
# To generate a random number between 1 and 10, i
# nclusive, do this:

# import random
# secret_number = random.randint(1, 10)
# print("I am thinking of a number between 1 and 10.")
# user_guess = " "

# while user_guess != secret_number:
#     user_guess = int(input("\n Guess my number: "))
#     if user_guess < secret_number:
#         print(f"Nope! You lose! Just kidding, {user_guess} is too low!")
#     elif user_guess > secret_number:
#         print(f"No Way!{user_guess} is so big! Try going lower.")
#     else:
#         break
# print("\n\nYou got it! You get a gold star!")



# Step 4: Limit Number of Guesses
# Limit the number of guesses the player has to 5. 
# If he cannot guess the number within 5 guesses, he losses.
# 

# print("I am thinking of a number between 1 and 10.")
# import random
# secret_number = random.randint(1, 10)
# n = 0

# while n < 5:
#     n +=1
#     user_guess = int(input(f"\nAttempt {n}: "))
#     if user_guess < secret_number:
#         print(f"Nope! You lose! Just kidding, {user_guess} is too low!")
#     elif user_guess > secret_number:
#         print(f"No Way!{user_guess} is so big! Try going lower.")
#     else:
#         break
# if n == 5:
#     print("Too many tries! You lose!")
# else:
#     print("You got it! You get a gold star!")


# Bonus: Play Again
# At the conclusion of a game, give the player the option of playing again.

import random
print("I am thinking of a number between 1 and 10.")
n = 1
secret_number = random.randint(1, 10)
while n <= 5:
    while True:
        try: 
            user_guess = int(input(f"\nAttempt {n}/5: "))
            break
        except ValueError:
            print("Please pick a number between 1 & 10?")
    n +=1
    if user_guess < secret_number:
        print(f"\nNope! You lose! Just kidding, {user_guess} is too low!")
    elif user_guess > secret_number:
        print(f"\nNo Way! {user_guess} is too big!")
    while n > 5 or user_guess == secret_number:
        if user_guess == secret_number:
            print("\nYou got it! You get a gold star!")  
        elif n > 5:
            print("\nToo many tries! You lose!")    
        new_game = input("\nWould you like to play again?\n(yes or no)???:  ")
        if new_game.upper() == "YES":
            n = 1
            secret_number = random.randint(1, 10)
            print("\nI am thinking of a number between 1 and 10.")
            break
        else:
            print("Thanks for playing!")
            n = 6
            break
    


#to redeclare his variables, he did:
# user_guess, n, secret_numer = None, 0, random.randint(1, 10)