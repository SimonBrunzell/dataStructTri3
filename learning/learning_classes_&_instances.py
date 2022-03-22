


class Employee:

    # self is a variable that can be swapped out when creating objects
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    # full name() is a method
    def fullname(self):
        return "{} {}" .format(self.first, self.last)


# emp_1 is an instance of the Employee Class
# self is passed on auto, so skip "self"
emp_1 = Employee("Simon", "Brunzell", 18)

# this allows for the replacement of a class variable
emp_1.first = input("do you go by a nickname, if so what is it: ")


# printing the return of a function attached to the class Employee
# both of these commands do the same thing
# but because emp_1 is an instance under the class Employee it doesn't need to be specified
print(emp_1.fullname())
print(Employee.fullname(emp_1))





