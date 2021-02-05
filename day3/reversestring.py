def reverse_string(a):
    return a[::-1]

user_input = input("Please enter a word: ")
user_input = reverse_string(user_input)
print(user_input)