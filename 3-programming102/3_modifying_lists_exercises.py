# 1. Write a program that has a list of names.
#         Add two new names to that list.
#         Print the results.
print("***1***")

list_of_names = ["Suzie", "Oey", "Emily", "Abby"]
added_names = ["Chloe", "Avery"]
list_of_names.extend(added_names)
print(list_of_names)

# 2. Write a program that has 5 names in a list.
#         Replace the items at index 2 and 4 with "Foo" and "Bar" respectively.
print("***2***")

names_two = ["Gwen", "Nancy", "Blake", "Ella", "Eli"]
print(names_two)

names_two[2] = "Foo"
names_two[4] = "Bar"
print(names_two)


# 3. Write a program that has a list of 5 names.
#         Loop through the array printing the item at index 0 and then removing that item from the array until there are no items in the array.
#         (hint) This will use a while loop.
print("***3***")

names_three = ["Gwen", "Nancy", "Blake", "Ella", "Eli"]
while names_three: #In Javascript, I would want to do len(names_three) because an empty bracket is not falsy in Javascript
    print(names_three[0])
    del(names_three[0])
# print(names_three)

