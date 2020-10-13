# literal is not a variable
# concatenate is joining two or more items together

first = "look a string"
second = "look another string!" #assigning a new variable.

'single quotes!' #still a string!

# 'I want to cross spaces
# now I am down here
# ' this will cause an error. You can't break lines this way. It will cause an error

third = ''' 
I want to cross spaces


now I am down here
''' #creates a space after

fourth = """This is going to 
be
spaced down"""

print(third)
print(first)
print(fourth)

print("hello"+" "+"world") # to make space, put a space inside the quotes. Either with the words or on its own...

# do Not
# bob = "Yes!"
# bob = 42 + bob
# these are different types. you will error!


message = "Hello, world!"

print(message)

print("second half")

name = "Clint"

# f-string!!!
combine = f"I want to say {message} to {name}" #fstrings need to be variables not items inside objects

print(combine) #could put the combine in here, but not as combine =, just as f"I want to say {message} to {name}"

print(f"I want to say {message} to {name}")

# Interpolation!!
adjective = "Awesome"
new_string = "Hey this is %s, and I like it" % adjective

print(new_string)

print("Oh my gosh, that dog is %s!" %adjective)

# You can concatonate a string with the interpolation...

print("The car is %s " %adjective + "I like it")

print("I want to tell %s %s %s!" % (name, message, new_string)) 

# Special Characters!!!

haiku ="Haikus are easy.\nBut sometimes they don't make sense.\nRefrigerator."
print(haiku)
# /n means new line!
# /t tabs!

tabbed = "Look\tI'm tabbed"
print(tabbed)

# quoted
sarcastic = 'I "really love" talking politics'
print(sarcastic)

# spaces use commas
print("and", "this", "that")