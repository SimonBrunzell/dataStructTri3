
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    # self is a variable that can be swapped out when creating objects
    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay

        Employee.num_of_emps += 1

    # full name() is a method
    def fullname(self):
        return "{} {}" .format(self.first, self.last)

    # function utilizing a class variable raise_amount
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    # a function to alter a class variable raise_amount
    @classmethod
    def set_raise_ant(cls, amount):
        cls.raise_amount = amount

    # allows for a string to be broken up by a common seperator and than assigned variables
    @classmethod
    def from_string(cls, emp_str):
        first, last, age, pay = emp_str.split('-')
        return cls(first, last, age, pay)


#       changing the class variable to 1.05
Employee.set_raise_ant(1.05)
print(Employee.raise_amount)


#       emp_1 is an instance of the Employee Class
#       self is passed on auto, so skip "self"
emp_1 = Employee("Simon", "Brunzell", 18, 1000000)

#       this allows for the replacement of a class instance variable
emp_1.first = input("do you go by a nickname, if so what is it: ")


#       printing the return of a function attached to the class Employee
#       both of these commands do the same thing
#       but because emp_1 is an instance under the class Employee it doesn't need to be specified
print(emp_1.fullname())
print(Employee.fullname(emp_1))

#       prints initial pay than sends emp_1 through the function apply_raise()
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#       this allows for the access of all information associated with emp_1
print(emp_1.__dict__)

#       will print number of instance due to the function of assigning values to instances inluding a counter
#       Employee.num_of_emps += 1
print(Employee.num_of_emps)


# passes through emp_str_2 through Employee function from_string()
emp_str_2 = 'John-Doe-18-70000'
emp_2 = Employee.from_string(emp_str_2)

# checking to make sure that the employee was created properly
print(emp_2.__dict__)
print(emp_2.fullname())
