# ~~~~~~~ Assignment - Factorial ~~~~~~~
try:
    number = int(input("Enter a number: "))

    factorial = 1

    if number < 0:
        print("No factorial for negative numbers!: ")
    elif number == 0:
        print("Factorial of 0 is 1")
    else:
        for index in range(1, number + 1):
            factorial = factorial * index
        print("Factorial of",number,"is",factorial)
except ValueError:
    print("This is an invalid integer")



# ~~~~~~~~ Assignment - Palindrome ~~~~~~~~~~

def word(a):
    return a == a[::-1]

a = input("Please enter a word: ")
a = word(a)

if a:
    print("Palindrome")
else:
    print("Not a Palindrome")



# # ~~~~~~~ Assignment - Prime Number ~~~~~~~~



try:
    number = int(input("Enter a number: "))
    if number > 1:
        for i in range(2,number):
            print(f"number: {number}, i: {i} = {number % i}")
            if (number % i) == 0:
                print(f"{number} is NOT a prime number: ")
                break
        else:
            print(f"{number} is a prime number")
    else:
        print(f"{number} is NOT a prime number: ")

except ValueError:
    print("This is an invalid integer")

# number = 1

# if True:
#     for i in range(2,number):
#         print("I entered the for")
#         if number == 2:
#             print("I entered the castle")
#         else:
#             print("I did not enter the for")
#     print("Nothing happened")
# else:
#     print("I did not enter the if")

# try:    
#     number = int(input("Enter a number: "))

#     if (number % 2) == 0:
#         print("EVEN")
#     else:
#         print("ODD")
# except ValueError:
#     print("This is not an integer")