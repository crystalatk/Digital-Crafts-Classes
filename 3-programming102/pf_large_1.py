# 1. Tic-Tac-Toe
# Continue the Tic-Tac-Toe example from the nested for-loop example

# #
print("Welcome to Crystal's Tic Tac Toe Game!\nPlease follow the instructions carefully!")
SIZE = 3
board = [] # Start with an empty List
for y in range(SIZE):
    # Each element in the board will also be a List
    board.append([])        
    for x in range(SIZE):
        # Fill our inner Lists with the coordinates
        board[y].append("[%d][%d]" % (y, x))
print("\nHere is our board!\nPlayer 1 is X and Player 2 is O.\n")
# Print the board as a grid


for row in board:
    for column in row:
        print("%s  " % column, end="")
    print("\n")

player_1 = "  X   "
player_2 = "  O   "

player = 1

error_number_message = "\n*******\nPlease enter a number between 0 and 2.\n*******"
loser_statement = "\n*****Player %s Loses!!! Hahaha!*****"



for i in range(0, 10):
    print(f"\nPlayer {player}'s turn!\n")

    while True:
        try:
            row = int(input(f"\n***Player {player}***\nWhich row would you like to use (This is the first number [row] [column]?\n0, 1, or 2? "))
            if 0 <= row <= 2:
                column = int(input("\nWhich column would you like to mark?\n0, 1, or 2? "))
                if 0 <= column <= 2:
                    if board[row][column] == player_1 or board[row][column] == player_2:
                        print("\n*****\nThat space is already taken. Try again!\n*****")
                    else:
                        break
                else:
                    print(error_number_message)
            else:
               print(error_number_message) 
        except ValueError:
            print(error_number_message)

    if player == 1:
        board[row][column] = player_1
        player = 2
    else:
        board[row][column] = player_2
        player = 1

    print("\n")
    for row in board:
        for column in row:
            print("%s  " % column, end="")
        print("\n")


    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        print(loser_statement % player)
        break
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        print(loser_statement % player)
        break
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        print(loser_statement % player)
        break
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        print(loser_statement % player)
        break
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        print(loser_statement % player)
        break
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        print(loser_statement % player)
        break
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        print(loser_statement % player)
        break
    elif board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        print(loser_statement % player)
        break
    else:
        i += 1

if i >= 9:
    print("\n*****It's a cat! You guys are evenly matched!*****\nPlease play again!\n\n")
else:
    print("\n\tPlease play again!\n\n")




# #repeat
# print(f"\nPlayer 2's turn!\n")


# while True:
#     try:
#         row = int(input("\n***Player 2***\nWhich row would you like to use (This is the first number [row] [column]?\n0, 1, or 2? "))
#         column = int(input("\nWhich column would you like to mark?\n0, 1, or 2? "))
#         break
#     except ValueError or 0 < row > 2 or 0 < column > 2:
#         print("\n*******\nPlease enter a number between 0 and 2.\n*******")

# board[row][column] = player_2[1]

# for row in board:
#     for column in row:
#         print("%s  " % column, end="")
#     print("\n")