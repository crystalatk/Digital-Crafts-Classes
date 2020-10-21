# Instantiation - In programming terms this is creating an self contained 'instance' of a class that can be used in the program.
# attributes - Are values in a class that can be accessed using the accessed using the attribute name. Much like key in a dictionary

#****Defining and Instantiating Classes****

# class Person:
#     pass #this just makes an empty anything

# # def my_func():
# #     pass

# # for i in range(3):
# #     pass

# clint = Person()
# anna = Person()

# print(clint)

# class Person:
#     def __init__(self): #self is the standard parameter inside of a class
#         print('You have initilized the person class')

# #__init__ is special and called automatically, otherwise it's just a function

# clint = Person() 
# anna = Person()

# print(clint)


# class Person:
#     def __init__(self):
#         #using self allows us to modify the class
#         # name attribute
#         self.name = "Clint"
#         # age attribute
#         self.age = 38

# clint = Person()
# print(clint.name)

# *****Using Self************
#   class Person:
#       def __init__(self, name, age):
#           self.name = name
#           self.age = age

#   clint = Person("Clint", 38)
#   anna = Person("Anna", 37)

#   print(clint.name, clint.age)
#   print(anna.name, anna.age)

#   print(f"Wow, {clint.name}, you are {clint.age} years old")

# ***********Default Values*********

class Person:
    # adding a default value for height
    def __init__(self, name, age, height="normal"):
        self.name = name
        self.age = age
        self.height = height

clint = Person("Clint", 38, "short")
anna = Person("Anna", 37)

print(clint.name, clint.age, clint.height)
print(anna.name, anna.age, anna.height)
