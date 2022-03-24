
# The Assignment:
# Write Factorial function using classes, providing implementation of call.

import math
#
# print("the factorial of 23 is: ")
# print(math.factorial(23))


class Factorial:
    def __init__(self, terms):
        self.terms = int(terms)

    def print_fact(self):
        fact = math.factorial(self.terms)
        return fact


response = (input("What do you want the Factorial of? : "))
n = Factorial(response)
Factorial.terms = n


print(Factorial.print_fact(Factorial.terms))





