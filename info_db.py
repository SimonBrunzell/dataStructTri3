
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
    "Classes": ["A", "B", "C", "D", "E"]
})


# getting the user's name
first = list_of_PII[1].get("FirstName")
last = list_of_PII[1].get("LastName")
full_name = first + " " + last

# asking what their Period 1 class
A = input(full_name + " what is your first class: ")

# trying to input the users response into the sublist
list_of_PII[1]["Classes"][0] = A

print()
print("Your Period 1 is: ")
print(list_of_PII[1].get("Classes")[0])
