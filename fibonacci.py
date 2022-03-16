
num = input("How many terms of the Fibonacci sequence do you want?: ")


def fibonacci(num):
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


print()
fibonacci(str(num))




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

