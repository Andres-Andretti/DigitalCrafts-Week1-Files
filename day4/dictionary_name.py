# Activity 1

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

name = {"first_name": first_name, "last_name": last_name}

print("My name is " + name["first_name"] + " " + name["last_name"])

print (f"My name is {name['last_name']}, {name['first_name']}")