
list_of_PII = []
# leaves list empty for now

list_of_PII.append({
    "FirstName": "Simon",
    "LastName": "Brunzell",
    "Birthday": "January 24th 2004",
    "Residence": "San Diego",
    "Email": "simon@gmail.com",
    "Classes": ["Symphonic Band", "AP Statistics", "Ethnic Lit", "Data Structures"]
})

list_of_PII.append({
    "FirstName": "Sebastian",
    "LastName": "Brunzell",
    "DOB": "March 7th 2006",
    "Residence": "San Diego",
    "Email": "Sebastian@gmail.com",
    "Classes": ["Class_1", "Class_2", "Class_3", "Class_4", "Class_5", ]
})


# getting the user's name
first = list_of_PII[1].get("FirstName")
last = list_of_PII[1].get("LastName")
full_name = first + " " + last

print(full_name + " is this your class list?")


# prints list backwards
# def class_loop():
#     n = len(list_of_PII[1]["Classes"]) - 1
#     while n > -1:
#         print(list_of_PII[1]["Classes"][n])
#         n = n - 1
# class_loop()


# prints all of Sebastian's original classes
def class_loop_while():
    n = 0
    while n < 5:
        print(list_of_PII[1]["Classes"][n])
        n = n + 1


class_loop_while()


# # prints all of sebastian's classes as the list
# print(list_of_PII[1]["Classes"])

# asks for a correction of Sebastian's Period 1 Class
print()
A = input("sorry somethings wrong... what's your first class: ")

# imputing period 1 into class sublist
list_of_PII[1]["Classes"][0] = A

print()
print(" oh... this is your class list")
print()
# using a for loop to display revamped schedule
for classes in list_of_PII[1]["Classes"]:
    print(classes)

print()
print("are you sure your second class is right")
B = input("what is your 2nd period class?: ")
print()

list_of_PII[1]["Classes"][1] = B


def recursive_loop(c):
    if c < len(list_of_PII[1]["Classes"]):
        print(list_of_PII[1]["Classes"][c])
        recursive_loop(c + 1)
    return


recursive_loop(0)

print()
print("Ooh there we go... this looks right now")


# n = 0
# while n < 5:
#     print(list_of_PII[1]["Classes"][n])
#     n = n + 1




