# Nesting: Putting code blocks inside of other code blocks or groupings...something inside of something esle.


# wrapping a string / varaible in len() outputs how many characters the string is.
name = input("What is your name? ")
if len(name) > 3:
    print("Your name is long enough.")
    if len(name) > 15:
        print("That is way too long.")
    else:
        print(f"Welcome, {name}.")

print("***Part 2***")


name = input("What is your name? ")

if len(name) > 3:
    if len(name) < 10:
        if len(name) == 4:
            # Even one block lower
            print('Perfect Length!')
        else:
            print("It's an ok length.")
        
        print(f"Welcme, {name}!")
    else:
        print("That's way to long partner")
else:
    print('%s is too few characters' % len(name))

#We could replace len(name) with a variable!

print("***Part 3: Multiple Conditions***")

print("***With And!***") #All statements must be truthy

name = input("what is your name? ")
num = len(name)
## You can have multiple conditions here
if num > 3 and num < 15:
    if num == 4:
        print('Perfect Length!')
    else:
        print("It's an ok length")
        
    print(f"Welcme, {name}!")
else:
    print('%s is not a good number of characters:(' % len(name))

print("***With or***") #EAny of the statements can be truthy

if num > 3 or num < 15: #There will be no false statement because these parameters cross
    print("This is valid.")

if num < 3 or num > 15: #Parameters don't overlap, so you will get a print
    print("Your name is an unusual length!")
