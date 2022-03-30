import random
def printBoard(board):
    print(board[1]+" | "+board[2]+" | "+board[3]+" | ")
    print(board[4]+" | "+board[5]+" | "+board[6]+" | ")
    print(board[7]+" | "+board[8]+" | "+board[9]+" | ")
def checkwin(board):
    if board[1] == board[2] == board[3]:
        return [True,board[1]]
    if board[4] == board[5] == board[6]:
        return [True,board[4]]
    if board[7] == board[8] == board[9]:
        return [True,board[7]]
    if board[1] == board[5] == board[9]:
        return [True,board[1]]
    if board[3] == board[5] == board[7]:
        return [True,board[5]]
    if board[1] == board[4] == board[7]:
        return [True,board[4]]
    if board[2] == board[5] == board[8]:
        return [True,board[5]]
    if board[3] == board[6] == board[9]:
        return [True,board[3]]
    return [False," "]
def playerMove(board):
    selection = int(input("Where do you want to move"))
    while board[selection] != " ":
        selection = int(input("Where do you want to move"))
    board[selection] = "x"

def computerMove(board):
    move = random.randint(1,10)
    while board[move] != " ":
        move = random.randint(1,10)
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
if __name__ == '__main__':
    game()