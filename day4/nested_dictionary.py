# Activity 2 - Nested 

first_name = ("Andres")
last_name = ("Corredor")
primary_address = {"street": "123 Main St", "city": "Orlando, FL"}
secondary_address = {"street": "1600 Pennsylvania Ave", "city": "Washington, DC"}

profile = [first_name, last_name, primary_address, secondary_address]
print(profile)


# Activity 3 - Multi-Nested JSON

user = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "sincere@april.biz",
    "address": {
        "street": "xxxx",
        "zipcode":"xxxx",
        "geo": {
            "lat": "-37.4054",
            "long": "81.4523"
        }
    }
    "phone": "1-770-736-8031"
}

# Iterating through the dictionary

# Option 1

for key in user: 
    print(key) <-- # prints out just key
    print(user[key]) <-- #prints out value with [] inside ()

# Option 2

for value in user.values():
    print(value) <-- #prints only value, not key


# Option 3 
for key, value in user.items(): <-- # .items is a function
    print(key)
    print(values)


# Deleting from a dictionary

electric_car = {"make": "Tesla", "model": "Model S"}

del electric_car["model"] <-- # del removes specified item in [] of variable(elec_car)
print(electric_car) 