
# Assignment 1 - Calculator

first_number = float(input("Please enter first number: "))
user_operand = input("Please enter an operand (+, -, *, /): ")
second_number = float(input("Please enter second number: "))

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

if user_operand == "+":
   print (add(first_number, second_number))
elif user_operand == "-":
    print(subtract(first_number, second_number))
elif user_operand == "*":
    print(multiply(first_number, second_number))
elif user_operand == "/":
    print (divide(first_number, second_number))


# Assignment 2 - Even/Odd

number = int(input("Enter a value: "))

if number % 2 == 0:
    print("EVEN")
else:
    print("ODD")


# Assignment 3 - FizzBuzz

number = int(input("Enter a value: "))

if number %3 and number %5 == 0:
    print("Fizz Buzz")
elif number %3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("neither Fizz nor Buzz")
