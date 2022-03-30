import random
def printBoard(board):
    print(board[1]+" | "+board[2]+" | "+board[3]+" | ")
    print(board[4]+" | "+board[5]+" | "+board[6]+" | ")
    print(board[7]+" | "+board[8]+" | "+board[9]+" | ")
def checkwin(board):
    if board[1] == board[2] == board[3] and (board[1] != " "):
        return [True,board[1]]
    if board[4] == board[5] == board[6] and (board[4] != " "):
        return [True,board[4]]
    if board[7] == board[8] == board[9] and (board[7] != " "):
        return [True,board[7]]
    if board[1] == board[5] == board[9] and (board[1] != " "):
        return [True,board[1]]
    if board[3] == board[5] == board[7] and (board[3] != " "):
        return [True,board[5]]
    if board[1] == board[4] == board[7] and (board[1] != " "):
        return [True,board[4]]
    if board[2] == board[5] == board[8] and (board[2] != " "):
        return [True,board[5]]
    if board[3] == board[6] == board[9] and (board[3] != " "):
        return [True,board[3]]
    if " " not in board.values():
        return [True,"tie"]
    return [False," "]
def playerMove(board):
    selection = int(input("Where do you want to move? "))
    while board[selection] != " ":
        selection = int(input("Where do you want to move? Select an open space. "))
    board[selection] = "x"

def computerMove(board):
    move = random.randint(1,9)
    while board[move] != " ":
        move = random.randint(1,9)
    board[move] = "o"
def game():
    board = {
        1:" ",
        2:" ",
        3:" ",
        4:" ",
        5:" ",
        6:" ",
        7:" ",
        8:" ",
        9:" "
    }
    move = 1
    while not checkwin(board)[0]:
        if checkwin(board)[1] == "tie":
            break
        if move==1:

            printBoard(board)
            print("Your move: ")
            playerMove(board)
            move = 0
        else:
            computerMove(board)
            move = 1
    if checkwin(board)[1] == "x":
        print("Congratulations! You won!")
    elif checkwin(board)[1] == "tie":
        print("It was a tie! ")
    else:
        print("The computer won. ")
if __name__ == '__main__':
    game()