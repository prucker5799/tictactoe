import random

field = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
choices_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def show_field():
    print(field[0][0] + " | " + field[0][1] + " | " + field[0][2])
    print(field[1][0] + " | " + field[1][1] + " | " + field[1][2])
    print(field[2][0] + " | " + field[2][1] + " | " + field[2][2])
    print("\n\n")


def turn(token, f):
    if f == 1:
        field[0][0] = token
    elif f == 2:
        field[0][1] = token
    elif f == 3:
        field[0][2] = token
    elif f == 4:
        field[1][0] = token
    elif f == 5:
        field[1][1] = token
    elif f == 6:
        field[1][2] = token
    elif f == 7:
        field[2][0] = token
    elif f == 8:
        field[2][1] = token
    elif f == 9:
        field[2][2] = token

    choices_left.remove(f)


def player_turn():
    print("Choose one of the following numbers to place your Token: " + str(choices_left))
    i = int(input("Enter the number of the field you want to choose: "))
    if i in choices_left:
        turn("X", i)
    else:
        print("\nATTENTION! You chose a number that isn't allowed. Seriously?! I even show them to you every bloody"
              " time you have to choose...\n")
        player_turn()


def bot_turn():
    # Block for 4 outer sides of field
    if field[0][0] == "X" and field[0][2] == "X" and field[0][1] == "_":
        turn("O", 2)
    elif field[0][0] == "X" and field[2][0] == "X" and field[1][0] == "_":
        turn("O", 4)
    elif field[2][0] == "X" and field[2][2] == "X" and field[2][1] == "_":
        turn("O", 8)
    elif field[2][2] == "X" and field[0][2] == "X" and field[1][2] == "_":
        turn("O", 6)
    # Block diagonals
    elif field[0][0] == "X" and field[2][2] == "X" and field[1][1] == "_":
        turn("O", 5)
    elif field[2][0] == "X" and field[0][2] == "X" and field[1][1] == "_":
        turn("O", 5)
    # 1.Turn
    if len(choices_left) == 8:
        # When player sets in any corner
        if field[0][0] == "X" or field[0][2] == "X" or field[2][0] == "X" or field[2][2] == "X":
            turn("O", 5)
        # When player begins in center
        # elif field[1][1] == "X":
        #     turn("O", random.r)


def check_combinations(symbol):
    s = str(symbol)
    b = False
    if field[0][0] == field[0][1] == field[0][2] == s:
        b = True
    elif field[1][0] == field[1][1] == field[1][2] == s:
        b = True
    elif field[2][0] == field[2][1] == field[2][2] == s:
        b = True
    elif field[0][0] == field[1][0] == field[2][0] == s:
        b = True
    elif field[0][1] == field[1][1] == field[2][1] == s:
        b = True
    elif field[0][2] == field[1][2] == field[2][2] == s:
        b = True
    elif field[0][0] == field[0][1] == field[0][2] == s:
        b = True
    elif field[0][2] == field[1][1] == field[2][0] == s:
        b = True
    elif field[0][0] == field[1][1] == field[2][2] == s:
        b = True

    return b


def win():
    r = 0
    if check_combinations("X"):
        r = 1
    elif check_combinations("O"):
        r = 2

    return r


def tic_tac_toe():
    turns = 9
    while True:
        player_turn()
        turns -= 1
        bot_turn()
        turns -= 1
        show_field()
        print(len(choices_left))
        if win() == 1:
            print("Player has won. Who else could have, the bot chooses random numbers...")
            break
        if win() == 2:
            print("Bot has won. You lost against a randomly playing Bot, KEK!")
            break
        if turns == 0:
            print("The game is a tie. Just TIE again next time hahaha ixde lul rofl lulz.")
            break
