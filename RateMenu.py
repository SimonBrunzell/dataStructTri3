
#
# Initial Menu Options
# Dictionary Option
menu_options1 = {
    1: 'Images',
    2: 'Size',
    3: 'Font',
    4: 'Exit',
}


def print_menu2():
    for key in menu_options1.keys():
        print(key, '--', menu_options1[key])


print_menu2()


#
# sub menus
def images():
    print("You have selected Images")
    print("1 -- Land Animals")
    print("2 -- Sea Creatures")
    print("3 -- Flying Critters")


# tall, grande, vent
def size():
    print("1 -- small")
    print("2 -- Medium")
    print("3 -- LARGE")


def font():
    print("1 -- Times New Roman")
    print("2 -- Arial")
    print("3 -- Comic Sans")


#
# user input
option1 = 0


def run_options1():
    # infinite loop to accept/process user menu choice
    global option1
    while option1 == 0:
        try:
            option1 = int(input('Select your Option 1-4: '))
            if option1 == 1:
                images()
            elif option1 == 2:
                size()
            elif option1 == 3:
                font()
            # Exit menu
            elif option1 == 4:
                print('Preferences Set! exiting...')
                # exits out of the (infinite) while loop
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
                option1 = 0
                run_options1()
        except ValueError:
            print('Invalid input. Please enter an integer input.')
            option1 = 0
            run_options1()


run_options1()


option_A = 0


def run_image_options():
    # infinite loop to accept/process user menu choice
    global option_A
    while option_A == 0:
        try:
            option_A = int(input('Select your Option 1-3: '))
            if option_A == 1:
                print("You selected Land Animals!")
                print("cuties selected exiting...")
            elif option_A == 2:
                print("You selected Sea Creatures!")
                print("cuties selected exiting...")
            elif option_A == 3:
                print("You selected Flying Critters")
                print("cuties selected exiting...")
            else:
                print('Invalid option. Please choose one of these Galleries')
                option_A = 0
                run_image_options()
        except ValueError:
            print('Invalid input. Please enter an integer input.')
            option_A = 0
            run_image_options()


if option1 == 1:
    run_image_options()


option_S = 0


def run_size_options():
    # infinite loop to accept/process user menu choice
    global option_S
    while option_S == 0:
        try:
            option_S = int(input('Select your Option 1-3: '))
            if option_S == 1:
                print("You selected small")
                print("size selected exiting...")
            elif option_S == 2:
                print("You selected Medium")
                print("size selected exiting...")
            elif option_S == 3:
                print("You selected LARGE")
                print("size selected exiting...")
            else:
                print('Invalid option. Please choose one of these Galleries')
                option_S = 0
                run_size_options()
        except ValueError:
            print('Invalid input. Please enter an integer input.')
            option_S = 0
            run_size_options()


if option1 == 2:
    run_size_options()


option_F = 0


def run_font_options():
    # infinite loop to accept/process user menu choice
    global option_F
    while option_F == 0:
        try:
            option_F = int(input('Select your Option 1-3: '))
            if option_F == 1:
                print("Font set to Times New Roman")
                print("font selected exiting...")
            elif option_F == 2:
                print("Font set to Arial")
                print("Font selected exiting...")
            elif option_F == 3:
                print("Font set to Comic Sans")
                print("Font selected exiting...")
            else:
                print('Invalid option. Please choose one of these Galleries')
                option_F = 0
                run_font_options()
        except ValueError:
            print('Invalid input. Please enter an integer input.')
            option_F = 0
            run_font_options()


if option1 == 3:
    run_font_options()
