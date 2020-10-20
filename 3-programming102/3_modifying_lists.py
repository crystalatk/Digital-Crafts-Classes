my_pets = ["Daisy", "Molly", "Shadow"]
# Method can run from its instance, can be data types or class

#APPEND:adds single item

my_pets.append("Rainbow") #Adding Rainbow to end of list
print(my_pets)

# There are different Methods you can use.

# concatenation: You can concatenate lists using +
# Does not modify the original lists

my_dogs = ["Daisy", "Molly"]
my_cats = ["Shadow", "Rainbow"]

my_pets = my_dogs + my_cats
my_pets = my_pets + ["George"] # To add a single item, you need brackets. Otherwise, it sill error, because you are tryign to concatenate a string and list....
print( my_pets)
print(my_dogs)

# If you add an empty bracket [], you will not error, but nothing will change...

combined_literal = [1,3,5] + ['A', "b", True]
print(combined_literal)

# EXTEND: adds many items

new_pets = []
new_pets.extend(my_dogs)
print(new_pets)
new_pets.extend(my_cats)
print(new_pets)

# You can do this, too!
# new_pets.extend(["Georgia", "Stein"])
# print(new_pets)


# Replacing Items! You can only do this to replace, not to add.
my_pets[2] = "El Gato Diablo"
print(my_pets)

# # If we want to add two items directly
# my_pets[2:1] = ["El Gato Diablo", "Horseface Cat"]
# print(my_pets)

# Deleting an item from a list
del my_pets[2]
print(my_pets)

# Don't forget! We are looking for falsy statements, so this will never print. An empty bracket is a falsy statement and so is 0.....
reg = []
while len(reg):
    print("did it")