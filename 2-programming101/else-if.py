age = input("How old are you?\n")

if int(age) >= 21:
    print("You are old enough")
else:
    print("You are not old enough")

# if and else must start on same block level. be aligned...

print("****Part 2****")

age = int(input("How old are you?\n"))  #age will always be an integer now!

if age == 21:
    print("You are a great age to party.")
elif age >= 21:
    print("You are old enough")
elif age >37:
    print("this will never print!")
else:
    print("You are not old enough")

# once the else if statement is found, it runs the first thing and then doesn't run the rest.
# therefore, the second elif will never run!
