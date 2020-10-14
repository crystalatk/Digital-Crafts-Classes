# print('hi')
name = input("Name Please:\n") #It will take the value it receives and use it for the variable
subject = input("Favorite subject\n") #once the first input is given, it will ask for this. 

age = input("How old are you?\n") #\n makes it put the cursor below the question not next to the question...personal preference of Clint's

if int(age) >= 21:        #You need to change the age to an integer because input is a string!
    print("Grab a Beer?")
# if someone puts non-numbers into age, it will error out....

print(f"You said your name is {name}")
