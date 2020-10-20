[1, 2, 3] #list of integers
["Hi", "My", "Name is"] #list of string
# In python, we can have whatever types inside a list
["Hi", 2, False, 3.5, None]

# We can assign variables to lists

my_list_of_ints = [1,2,3]
print(my_list_of_ints)

# A list can be assigned a variable value
name = "clint"
age = 38
married = True

my_new_list = [name, age, married] #We are assigning the values to the list, but not the variable, so if the variable changes the list does not change.

age = 39 #This won't change the list because we already assigned the variable the value of age above

print(my_new_list)

# Inside a list, we can put a mix, including another list!

# Index: the number representation of the posistion of an item in the list or array
# Lists are ordered, so the order does not change...

my_children = ["Olivia", "Allie", "Mark"]
print(my_children[0]) #Will print Olivia

my_only_son = my_children[2]

print(my_only_son)