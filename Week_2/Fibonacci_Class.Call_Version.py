
class Fibonacci:
    def __init__(self, num, n1, n2, count):
        self.num = str(num)
        self.n1 = n1
        self.n2 = n2
        self. count = count


def ask_amount(self):
    # self.num = input("How many terms of the Fibonacci sequence do you want?: ")
    print("you said you wanted " + self.num + " terms?")
    print("here you go")
    return self.num


def fibo_math(self):
    self.num = int(self.num)
    while self.count < self.num:
        print(self.n1)
        nth = self.n1 + self.n2
        self.n1 = self.n2
        self.n2 = nth
        self.count += 1


# original amount of Fibonacci sequences that will be printed
# also assigns values to n1, n2, and count
amount = Fibonacci(2, 0, 1, 0)

# i might have to move this out here not sure tho
amount.num = input("How many terms of the Fibonacci sequence do you want?: ")

ask_amount(amount)

fibo_math(amount)
























# n = input("how many fibo digits do you want: ")
#
#
#     class Fibonacci:
#         # creates object self I think
#         def __init__(self):
#             self.fiboSeq = [0, 1]
#
#     # call allows for a class to behave like a regular Python function
#
#     def __call__(self, n):
#         if n < len(self.fiboSeq):
#             return self.fiboSeq[n]
#         else:
#             # Compute the requested Fibonacci number
#             fib_number = self(n - 1) + self(n - 2)
#             self.fiboSeq.append(fib_number)
#         return self.fiboSeq[n]
#
#
# fibo_of = fibonacci()
# # object instantiation and run __init__ method
# print(fibo_of(5))
# # object running __call__ method
