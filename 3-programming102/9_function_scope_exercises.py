#1.  Create a program that has a global varaible 'name' that is assigned a string value.
# Define a function that has an parameter called 'message' and will print out the name coma and then the message supplied in the argument when the function is called.
# call that function 3 times with 3 different messages.
#     #sample output
#     Clint, You are awesome and really tall.

print("***1***")

def coma(message):
    global name
    name = "Clint, "
    print(name + message)

coma("you have a typo!")
coma("how's the vacay?")
coma("enjoy the lifting.")



# 2. Create a program that has a global variable 'name' like the exercise above.
# Have a function that can modify the name variable with a supplied argument.
# call that function changing the name 3 times.

print("***2***")

def easy(name_arg):
    global name
    name = name_arg
    return name

print(easy("Crystal"))
print(easy("Eddie"))
print(easy("PooPoo Head"))

print(name)

