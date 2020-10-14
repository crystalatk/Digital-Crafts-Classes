# 1. Create a program that will print from 1-10 using a while loop.
print("**1**")

i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Create a program that will print from 10-1 using a while loop.
print("**2**")

i = 10
while i >= 1:
    print(i)
    i -= 1

# 3. Create a program that has a variable named username and another variabled named password with values of your choice.
#     Prompt the user for a username and then a password.
#     If the both match continue on with the program and give a welcome message.
#     If not it prompts the user for the username and password until they get it correct.
#     (bonus) have a limited amount of attempts and if they reach the limit it tells the user and exits the program.
print("**3**")

user_name = ""
password = ""
i = 1


while i <= 10 and (user_name != "Daisy" or password != "flower"):
    print(f"attempt {i}")
    user_name = input("What is your username?\n")
    password = input("What is your password?\n") 
    i += 1 
    if i == 11:
        print("You suck!")
    if user_name == "Daisy" and password == "flower":
        print(f"Welcome, {user_name}! So glad you could make it!")
