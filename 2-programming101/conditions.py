# what we've done before!
print(1 + 2) #assignment operators

# comparison operators: Always returns a true or false
print(1 == 2) #going to return a true or false
print(2 == 2) #going to be true!

# When we write a true false comparison it is a Boolean

#Using comparision operators
print(1 == 2)   #False
print(1 <  2)   #True
print(1 >  2)   #False
print(1 >= 1)   #True: greater than or equal to
print(1 <= 2)   #True: less than or equal to
print(1 != 1)   #False: not equal to

# Variables with Boolean
print("***variables***")
a = 1
b = 2
print(a == b) # false

# Strings!
print("***strings***")
name = "Clint"

print(name == "George")
print(name != "George")

print(name == "clint") #False because capitals! Must be exact!!!

print(name > "a") #the strings take into account alphabetical and capital
# capitalization and the alphabetized. and then longer name is larger...end of alphabet is larger

# Comparisons: if statements
#  code block is executed if value is true
#   if you don't indent properly, you will get error!
#     using four spaces instead of tab or only use tab. If you switch between you might error. 


print("****comparisons***")

if 1 > 3:
    print("this will not be printed")
if 1 < 3:
    print("this will be printed")
    print("this is the same level")# you can keep going on the same level...

if False:
    print("when is false ever true?") #Never, will never run

if True:
    print("when is true falsey?") #True is always true, so will always run

if None:
    print("None is never printed")

if 0:
    print("0 is a falsey statement.") #Booleans can be 1 and 0, zero is falsey, 0 is truthy

if 3:
    print("3 exists, so it is a truthy statement. Print!")

something_at_all = "Yes it's great!" #if this is an empty string, list, paragraph, its false....

if something_at_all:
    print(something_at_all)

# Falsey expressions: All of these will returne false in Python.
# None
# false
# 0
# ""   --Empty string
# []   ---Not falsey in Javascript empty list
# {}   ---Not falsey in Javascript empty paragraph


