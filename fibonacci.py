

amount = input("How many terms of the Fibonacci sequence do you want?: ")


def fibonacci(num):
    num = str(num)
    print("You said you wanted " + num + " terms? Here you go: ")
    print()
    num = int(num)
    n1, n2 = 0, 1
    count = 0
    while count < num:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


def ask():
    amount = input("Now how many do you want?: ")
    return amount


def tester(n):
    n = int(n)
    if n < 0:
        print("Sorry, cannot print a negative amount of numbers in the sequence")
        ask()
        tester(amount)
    elif n == 1:
        print("come on that's boring ")
        ask()
        tester(amount)
    elif n == 2:
        print("that's a bit better but c'mon ")
        ask()
        tester(amount)
    else:
        fibonacci(n)


tester(amount)


# print()
# fibonacci(str(amount))




# def tester():
#     num = int(input("Enter a number for factorial: "))
#     # check if the number is negative
#     if num < 0:
#         print("Sorry, factorial does not exist for negative numbers")
#     else:
#         print("The factorial of", num, "is", fibonacci(str(num)))
#
#
# tester()
