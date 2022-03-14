import time


def print_fishes(position):
    sp = " " * position
    print(sp + " ><((('> ")
    print(sp + "   ><(('> ")
    print(sp + "><(('> ")


def print_chase(position):
    sp = " " * position
    print(sp + " ><((('> " + sp + " ><((('> ")
    print(sp + "   ><(('> " + sp + " ><((('> ")
    print(sp + "><(('> " + sp + " ><((('> ")

def yes_to_chase():
    for position in range(start, distance, step):
        print_chase(position)
        time.sleep(.1)


start = 0
distance = 60
step = 2

for position in range(start, distance, step):
    print_fishes(position)
    time.sleep(.1)


chase_y_n = str(input('Do you wanna see a chase: '))

if chase_y_n == "yes" or 'y':
    yes_to_chase()

elif chase_y_n == "no":
    print('dang alright...')

else:
    print("huh? what did you say...?")

print("that's it folks")


