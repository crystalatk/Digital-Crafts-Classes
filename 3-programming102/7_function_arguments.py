print("This is the argument", "Look a second!") #for the function print
# len()<--we've done these arguments also!
len([1, 4, 5])#<---more than one argument!

# the arguments are what is between the parenthesis in a function
# separated with commas!

def add_two_numbers(a,b):#<--setting up the parameters
    print(a+b)

add_two_numbers(1, 3)#<--supplying the arguments
add_two_numbers(3, 4)

def me_print(any):
    print(any)

# The parameters that its asking for are treated like variables that have already been defined within the function

me_print(5)
me_print(True)
me_print([3, 4, 5])
me_print({"eky":"Huh?"})

# add_two_numbers(1, "c") <---This will cause a TypeError! You can't add an integer and a string

# You must have the same number of arguments as the parameters allow!

# Order matters
def tell_me_stuff(first_name, age, gender):
    print(f"My name is {first_name}")
    print(f"I am {age} years old.")
    print(f"I am {gender} human")
# first_name = "Crystal"<<<<----This Errors, you can't set the variable and expect it to show up in the function....
# age = 30
# gender = "They"
# tell_me_stuff()
tell_me_stuff("Clint", 38, "Male")
tell_me_stuff("Male", "Clint", 38)

#Giving the wrong type causes an error; or does it?!?!
add_two_numbers("foo", "bar")
# Adding two strings is concatonating....


# It does with divide! 
def divide_two_numbers(a, b):
    print(a/b)

divide_two_numbers("they", "were")
