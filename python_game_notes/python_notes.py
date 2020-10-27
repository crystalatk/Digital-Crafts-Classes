# Make a new folder repository
# make a file for each class.
# I can call the class by:
# from Unit import Character <----the first name is file the second is the class

#  This would be in another file: Unit

class Character:
    def __init__(self, name, position):
    self.name = name
    self.position = position #<--This can be a dictionary {} or a list [], Clint decided to use a list. In a dictionary, he woudl have the x and y stated, i.e. { "x" : 1, "y" : 2}


# This will be a new file: Item

class Item:
    def __init__(self, name, position):
        self.position = position
        self.name = name

#  New file! This is where you import into
# from Item import Item
# from Unit import Character

name = userinput("What do you want your name to be?")
player = Character(name, [5, 5])
menu = ["Move up", "Move down", "Move left", "Move right"]

# def move():
#     if 

while playing:#<---this will keep the game going
    show menu()
    try:
        action = int(input("What is your choice?\n"))
    except ValueError:
        print("You must enter a valid entry.")
        action = None #<---This will get rid of the action, since it was just defined above. Otherwise, it will already be defined as nonsense...
    
    if action:
        if action == 1:
            player.move("up")
        elif action == 2:
            player.move("down")
        elif action == 3:
            player.move("left")
        elif action == 4:
            player.move("right")
    
    print(player.positon)

#  You could make enemies and have if enemy.position == player.position  

# for enemy in enemies:
#     if enemy.position == player.position:
#         print(f"You ran into {enemy.name}: ")
#         print("You attack!")
#         player.attack(enemy)
#         print("Enemy attacks!")
#         enemy.attack(player)
# print(player.health)

        