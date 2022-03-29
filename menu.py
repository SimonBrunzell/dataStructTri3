from Week_0.ani import ship
from Week_0.animated_fish import yes_to_chase
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
        "Display":"quit",
        "exec":quit,
        "type":"func"
    }
}

def buildMenu(menu):
    for key,item in menu.items():
        print(f"{key} : {item['Display']}")

def presentMenu(menu):
    buildMenu(menu)
    choice = int(input("Which item do you want? "))
    while choice not in menu:
        choice = int(input("Which item do you want? "))
    if menu[choice]["type"] == "func":
        menu[choice]["exec"]()
if __name__ == '__main__':
    presentMenu(mainmenu)