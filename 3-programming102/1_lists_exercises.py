# 1. Create a program that has a list of at least 3 of your 
    # favorited foods in order and assign that list to a 
    # variable named "favorite_foods".

    # print out the value of your favorite food by 
    # accessing by it's index.
    # print out the last item on the list as well.

favorite_foods = ["chocolate", "spinach", "stir-fry"]
print(favorite_foods[0])
print(favorite_foods[-1])

#Good soltuion to print whole list:
# print(favorite_foods[0:])

# 2. Create a program that contains a list of 4 different 
    # "things" around you.

    # Print out the each item on a new line with the number 
    # of it's index in front of the item.
        # 0. Coffee Cup
        # 1. Speaker
        # 2. Monitor
        # 3. Keyboard

thing_around = ["Coffee Cup", "Speaker", "Monitor", "Keyboard"]

print("0. " + thing_around[0])
print("1. " + thing_around[1])
print("2. " + thing_around[2])
print("3. " + thing_around[3])

#Good Solution
index = 0
while index < len(thing_around):
    print("%i. %s" % (index + 1, thing_around[index]))
    index += 1


# 3. Using the code from exercise 2, prompt the user 
# for which item the user thinks is the most interesting. 
# Tell the user to use numbers to pick. (IE 0-3).

    # When the user has entered the value print out the 
    # selection that the user chose with some sort of pithy 
    # message associated with the choice.
    #     "You chose Coffee Cup, You must like coffee!"

thing_around = ["Coffee Cup", "Speaker", "Monitor", "Keyboard"]
print("Items Around Me:")
print("0. " + thing_around[0])
print("1. " + thing_around[1])
print("2. " + thing_around[2])
print("3. " + thing_around[3])

is_in_loop = True
while is_in_loop:
    try:
        user_pick = int(input("Which item do you think is most interesting?\nPlease choose 0, 1, 2, or 3. "))
        if 0 <= user_pick < len(thing_around):
            is_in_loop = False 
        else:
            print("You did not choose a number between 0 & 3")  
    except ValueError:
        print("\nThat will not work\nPlease enter either: 0, 1, 2, or 3")

# user_pick = int(input("Which item do you think is most interesting?\nPlease choose 0, 1, 2, or 3. "))
if user_pick == 0:
    print(f"\nOh my goodness, you chose a {thing_around[user_pick]}?!?\nI hate coffee.")
elif user_pick == 1:
    print(f"\n{thing_around[user_pick]}s are good for listenting to those tunes. Turn it up!")
elif user_pick == 2:
    print(f"\nThank goodness I have a big {thing_around[user_pick]}.\nWhen it comes to {thing_around[user_pick]}s, size does matter.")
else:
    print(f"\nYou chose the {thing_around[user_pick]}.\nDon't look too closely, I hear these things are dirty!\n")
# print(f"Oh my goodness, you chose a {thing_around[user_pick]}?!?\nThat's what I like, too!")

