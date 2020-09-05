import random
choices_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
field = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


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


def game():
    turns = 9
    while turns > 0:
        turn("X", random.choice(choices_left))
        turn("O", random.choice(choices_left))
