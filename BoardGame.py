# import random
import random

def dice():
    # prints a random value from the list
    list1 = [1, 2, 3]
    return random.choice(list1)


def dice2():
    # prints a random value from the list
    list1 = [1, 2, 3]
    return random.choice(list1)

# initialising a board with 9 places
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
game = True

P1 = 0 ; P2 = 0

# Rendering player's positions
def render_board(board):
    print("------------", end="\n")

    # If 'P1' or 'P2' is present -> print P1 or P2
    # If not -> '-' is printed 
    for row in range(1, 3 + 1):
        for col in range(1, 3 + 1):

            if row == 2 and col == 1:
                if type(board[0]) == str:
                    print(board[0], end="  ")
                else:
                    print("-  ", end="  ")

            if row == 3:
                if type(board[col]) == str:
                    print(board[col], end="  ")
                else:
                    print("-  ", end="  ")

            if row == 1:
                if type(board[8-col]) == str:
                    print(board[8-col], end="  ")
                else:
                    print("-  ", end="  ")

            if row == col == 2:
                if type(board[8]) == str:
                    print(board[8], end="  ")
                else:
                    print("-  ", end="  ")
            
            if row == 2 and col == 3:
                if type(board[4]) == str:

                    print(board[4], end="  ")
                else:
                    print("-  ", end="  ")

        print("\n------------", end="")
        print()

def update_board(p1, p2):
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    is_game_over = False

    if p1 == p2: # If P1 and P2 are at same place -> one is brought back to 0 
        print("Player 1 (P1) Killed, Back to Safe Place" + "\n")
        p1 = 0

    # Placing players on the board
    for i in range(0, len(board)):
        if p1 == board[i]:
            board[i] = "P1"
    for i in range(1, len(board)):
        if p2 == board[i]:
            board[i] = "P2"

    # Win conditions
    if str(board[len(board) - 1]) == "P1":
        print("Player 1 Wins!!!")
        is_game_over = True
    if str(board[len(board) - 1]) == "P2":
        print("Player 2 Wins!!!")
        is_game_over = True

    # Updating the board, p1, p2 and whether the game should continue
    return board, p1, p2, is_game_over


while game:

    is_game_over = False

    # Rolling the dice for Player1
    num1 = dice()
    P1 += num1

    # Forcing the player to stay at the same place 
    if P1 > len(board) - 1:
        print("\n" + "P1 Rolled too high, stay where you are, P2s Turn")
        P1 -= num1

    # Rolling the dice for Player2
    num2 = dice()
    P2 += num2

    # Forcing the player to stay at the same place 
    if P2 > len(board) - 1:
        print("\n" + "P2 Rolled too high, stay where you are, P1s Turn")
        P2 -= num2

    test = print("\n" + "Player 1 (P1) Role Dice: " + str(num1) + "\n" + "Player 2 (P2) Role Dice: " + str(num2) + "\n")
    input("Press enter to display positions..  " + "\n")
    info = print(" Player 1 (P1) Pos: " + str(P1), "\n", "Player 2 (P2) Pos: " + str(P2) + "\n")
    input("Press enter to render board..  " + "\n")

    new_list, P1, P2, is_game_over = update_board(P1, P2)

    render_board(new_list)
    print("\n")
    if is_game_over:
        game = False
    if game:
        input("Press enter to roll dice..  ")