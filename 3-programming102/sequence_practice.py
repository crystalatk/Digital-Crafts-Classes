# My solution: I was confused about the task, I was trying to add a single user item to an existing list
# todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
# try:
#     new_item = input("Please enter a new to do item:\n")
# except TypeError:
#     quit()

# todos = todos + ["binge watch a show", "go to sleep"] + [new_item]
# count = 1
# for todo in todos:
#     print("%d: %s" % (count, todo))
#     count += 1

# Real Solution:

# todos = []

# # Prompt the user the first time
# new_todo = input("What do you need to do? ")
# while len(new_todo) > 0:
#     todos.append(new_todo)

#     # Print the current list of to-do items
#     print("To do:")
#     print("====================")
#     count = 1
#     for todo in todos:
#         print("%d: %s" % (count, todo))
#         count += 1

#     # Prompt the user again
#     print("\n")
#     new_todo = input("What do you need to do? ")

# print("Have a nice day!")

# Part 2 prompting a user if they would like to print, add item, or replace item

todos = []
user_needs = input("Would you like to print your list, add an item to your list, or replace an item from your list?\nPlease say: print, add, or replace: ")
while user_needs.upper() == 
if user_needs.upper() == "PRINT":
    print("To do:")
    print("====================")
    count = 1
    for todo in todos:
        print("%d: %s" % (count, todo))
        count += 1

elif user_needs.upper() == "ADD":
    # Prompt the user the first time
    new_todo = input("What do you need to add to your to do list? ")
    todos.append(new_todo)

    # Print the current list of to-do items
    print("To do:")
    print("====================")
    count = 1
    for todo in todos:
        print("%d: %s" % (count, todo))
        count += 1

    # Prompt the user again
    print("\n")
    new_todo = input("What do you need to do? ")

elif user_needs.upper() == "REPLACE":
    remove_todo = input("What number item would you like to replace?")
    replace_todo = input("What would you like instead? ")
    start = remove_todo + 1
    todos[start:remove_todo] = [replace_todo]
        

print("Have a nice day!")