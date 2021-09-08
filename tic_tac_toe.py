
import random

def user_ch():
    choice = "nope"

    while choice.isdigit() == 0 or int(choice) not in range(1,10):
        choice = input("Enter the position of your next move (1-9): ")

        if choice.isdigit() == 0:
            print("A positive number you plonker!")

        elif int(choice) not in range(1,10):
            print("Betwixt 1 and 9, c'mon mate...")

    print('\n' * 30)
    return int(choice)

def disp_board(board):
    print('\n' * 30)

    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])

def user_mark():
    mark = ""

    while not (mark == "X" or mark == "O"):
        mark = (input("Player 1, please choose your marker, X or O: ")).upper()

    if mark == "X":
        return ("X","O")

    elif mark == "O":
        return ("O", "X")

def place(board, user_pos, mark):

    if board[user_pos] == "-":
        board[user_pos] = mark
        placed = True
    else:
        return "You can't step on other people's toes like that."
        placed == False

def win(board, mark):
    return(

    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark))

def play_again():
    again = input("Would you like to carry on playing? Y or N. ").lower()

    while not again  == "n" or not again  == "y":
        if again == "y":
            return True
        elif again == "n":
            return False
        else:
            again = input("Need a Y or N. You wanna play? ").lower()

def space(board, user_pos):
    if board[user_pos] == "-":
        return True

def draw(board):
    filled = 0
    for i in range(1,10):
        if space(board, i):
            return False

        else:
            filled += 1
    if filled == 9:
        return True

def first_player():

    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"

print ("Let's see if the ol' TicTacToe works...")

game_on = True

while game_on == True:

    my_board = ["-"]*10
    p1mark, p2mark = user_mark()
    turn = first_player()

    print (turn + "will go first.")

    play = input("You wanna play??? Y or N.").lower()

    if play == "y":
        game_on = True
    elif play == "n":
        game_on = False
    else:
        play = input("Need a Y or N. You wanna play? ").lower()

    while game_on == True:

        if turn == "Player 1":
            print("Player 1's turn. ")
            disp_board(my_board)

            user_pos = user_ch()


            place(my_board, user_pos, p1mark)

            disp_board(my_board)

            if win(my_board, p1mark) == 1:
                disp_board(my_board)
                print("Player 1 has won!")
                game_on = False

            elif draw(my_board)==1:
                disp_board(my_board)
                print("A draw, how boring...")
                game_on = False

            else:
                turn = "Player 2"

        else:
            print("Player 2's turn. ")
            disp_board(my_board)
            user_pos = user_ch()

            place(my_board, user_pos, p2mark)

            disp_board(my_board)

            if win(my_board, p2mark) == 1:
                disp_board(my_board)
                print("Player 2 has won!")
                game_on = False

            elif draw(my_board)==1:

                print("A draw, how boring...")
                game_on = False

            else:
                turn = "Player 1"

        if not play_again():
            game_on = False
            break
