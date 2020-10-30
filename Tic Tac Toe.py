positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
# A list of the things in each position
won = False
# This turns to true when I want to end the loop
def print_board():
    print(f" {positions[0]} | {positions[1]} | {positions[2]} ")
    print("-----------")
    print(f" {positions[3]} | {positions[4]} | {positions[5]} ")
    print("-----------")
    print(f" {positions[6]} | {positions[7]} | {positions[8]} ")
    # Prints the board that changes based on player actions

def player_move(side):
    move = input('Pick the position you want. (Type "Top Left", "Middle Middle", "Bottom Right", etc.) ')
    # Asks which position they want to change
    if move.lower().strip() == "top left":
        if positions[0] == " ":
            # Checks if the position is empty
            positions[0] = side
            # If it is, it replaces the position with the symbol whose turn it is
        else:
            print("Sorry, that position is already filed. Try again!")
            player_move(side)
            # If it is already filled, it tells the player that it is already filled
            # and runs the function again so they can retry
    elif move.lower().strip() == "top middle":
        if positions[1] == " ":
            positions[1] = side
        else:
            print("Sorry, that position is already filed. Try again!")
            player_move(side)
    elif move.lower().strip() == "top right":
        if positions[2] == " ":
            positions[2] = side
        else:
            print("Sorry, that position is already filed. Try again!")
            player_move(side)
    elif move.lower().strip() == "middle left":
        if positions[3] == " ":
            positions[3] = side
        else:
            print("Sorry, that position is already filed. Try again!")
            player_move(side)
    elif move.lower().strip() == "middle middle":
        if positions[4] == " ":
            positions[4] = side
        else:
            print("Sorry, that position is already filed. Try again!")
            player_move(side)
    elif move.lower().strip() == "middle right":
        if positions[5] == " ":
            positions[5] = side
        else:
            print("Sorry, that position is already filed. Try again!")
            player_move(side)
    elif move.lower().strip() == "bottom left":
        if positions[6] == " ":
            positions[6] = side
        else:
            print("Sorry, that position is already filed. Try again!")
            player_move(side)
    elif move.lower().strip() == "bottom middle":
        if positions[7] == " ":
            positions[7] = side
        else:
            print("Sorry, that position is already filed. Try again!")
            player_move(side)
    elif move.lower().strip() == "bottom right":
        if positions[8] == " ":
            positions[8] = side
        else:
            print("Sorry, that position is already filed. Try again!")
            player_move(side)
    else:
        print("You didn't pick one of the available choices! Try again!")
        player_move(side)
        # If they did not type one of the available choices, the function runs again

def victory():
    global won
    # This makes it so the function affects the global variable won instead of
    # creating a local variable that is also called won
    if positions[0] == positions[1] and positions[1] == positions[2] and positions[0] != " ":
        print(f"{positions[0]} has won!")
        won = True
    elif positions[3] == positions[4] and positions[4] == positions[5] and positions[3] != " ":
        print(f"{positions[3]} has won!")
        won = True
    elif positions[6] == positions[7] and positions[7] == positions[8] and positions[6] != " ":
        print(f"{positions[6]} has won!")
        won = True
    elif positions[0] == positions[3] and positions[3] == positions[6] and positions[0] != " ":
        print(f"{positions[0]} has won!")
        won = True
    elif positions[1] == positions[4] and positions[4] == positions[7] and positions[1] != " ":
        print(f"{positions[1]} has won!")
        won = True
    elif positions[2] == positions[5] and positions[5] == positions[8] and positions[2] != " ":
        print(f"{positions[2]} has won!")
        won = True
    elif positions[0] == positions[4] and positions[4] == positions[8] and positions[0] != " ":
        print(f"{positions[0]} has won!")
        won = True
    elif positions[2] == positions[4] and positions[4] == positions[6] and positions[2] != " ":
        print(f"{positions[2]} has won!")
        won = True
    # This checks if any of the ways to win has been fulfilled.
    # If it has, then the loop ends
    else:
        pass

def draw():
    global won
    # This makes it so the function affects the global variable won
    if " " not in positions:
        print("The game has come to a draw!")
        won = True
    # If there are no empty spaces, the loop ends

while not won:
    # This while loop runs the game
    print_board()
    # Prints the board
    player_move("X")
    # X's turn
    victory()
    # Checks if it won
    draw()
    # Checks if it draws
    if won:
        continue
        # This ends the loop if X has won or if there is a draw
    print_board()
    # Prints the board
    player_move("O")
    # O's turn
    victory()
    # Checks if it won
    draw()
    # Checks if it draws
    if won:
        continue
        # This ends the loop if O has won or if there is a draw
else:
    print_board()
    # This prints the final board when the loop stops
