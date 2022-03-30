from Week_0.ani import ship
from Week_0.animated_fish import yes_to_chase
import os
import time
from crossover.tictactoe import game
mainmenu = {
    1: {
        "Display": "Ship",
        "exec": ship,
        "type":"func"
    },
    2: {
        "Display":"Chase",
        "exec":yes_to_chase,
        "type":"func"
    },
    3: {
        "Display":"tictactoe",
        "exec":game,
        "type":"func"
    },
    4: {
        "Display":"quit",
        "exec":quit,
        "type":"func"
    }
}

def buildMenu(menu):
    for key,item in menu.items():
        print(f"{key} : {item['Display']}")
def printmenubar(n,display=None):
    os.system("clear")
    print("\033[34m="*n)
    if display:
        print("="," "*int((n-5-len(display))/2),f"{display}"," "*int((n-5-len(display))/2),"=")
    else:
        print("="," "*(n-4),"=")
    print("="*n,"\033[0m")

def presentMenu(menu):
    for x in range(49):
        printmenubar(x)
        time.sleep(0.01)
    printmenubar(50,"Python Main Menu")
    buildMenu(menu)
    choice = int(input("Which item do you want? "))
    while choice not in menu:
        choice = int(input("Which item do you want? "))
    if menu[choice]["type"] == "func":
        menu[choice]["exec"]()
if __name__ == '__main__':
    presentMenu(mainmenu)