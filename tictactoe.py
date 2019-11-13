# bord
# display bord
# play game
# handle turn
# check win
# check rows
#     check coloums
#     check diagonals
#     check tie
# flip player


print("Global variable")
print("="*20)

game_stile_goingon = True
winner = None
current_player = "X"

bord = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]


def display_bord():
    print(bord[0] + "|" + bord[1] + "|" + bord[2])
    print(bord[3] + "|" + bord[4] + "|" + bord[5])
    print(bord[6] + "|" + bord[7] + "|" + bord[8])


def play_game():
    display_bord()
    while game_stile_goingon:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " win..!")
    elif winner == None:
        print("Game tie... Tray again!!")


def handle_turn(player):

    print("Player " + player + " s' turn.")
    position = input("Choose a position from 0-9:- ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("You choose an invalid position!")
            position = input("Please choose a valide position from 0-9:- ")

        position = int(position) - 1

        if bord[position] == "-":
            valid = True
        else:
            print("You already fill this position. Please choose another one..:)")

    bord[position] = player
    display_bord()


def check_if_game_over():
    check_for_winer()
    check_if_tie()


def check_for_winer():
    global winner
    # check rows
    row_winner = check_rows()
    # check colums
    coloums_winner = check_coloums()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif coloums_winner:
        winner = coloums_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_stile_goingon

    row_1 = bord[0] == bord[1] == bord[2] != "-"
    row_2 = bord[3] == bord[4] == bord[5] != "-"
    row_3 = bord[6] == bord[7] == bord[8] != "-"

    if row_1 or row_2 or row_3:
        game_stile_goingon = False

    if row_1:
        return bord[0]
    elif row_2:
        return bord[1]
    elif row_3:
        return bord[2]


def check_coloums():

    global game_stile_goingon

    coloum_1 = bord[0] == bord[3] == bord[6] != "-"
    coloum_2 = bord[2] == bord[4] == bord[7] != "-"
    coloum_3 = bord[3] == bord[6] == bord[8] != "-"

    if coloum_1 or coloum_2 or coloum_3:
        game_stile_goingon = False

    if coloum_1:
        return bord[0]
    elif coloum_2:
        return bord[2]
    elif coloum_3:
        return bord[3]
    return


def check_diagonals():
    global game_stile_goingon

    diagonal_1 = bord[0] == bord[4] == bord[8] != "-"
    diagonal_2 = bord[2] == bord[4] == bord[6] != "-"

    if diagonal_1 or diagonal_2:
        game_stile_goingon = False

    if diagonal_1:
        return bord[0]
    elif diagonal_2:
        return bord[2]


def check_if_tie():
    global game_stile_goingon

    if "-" not in bord:
        game_stile_goingon = False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


play_game()
