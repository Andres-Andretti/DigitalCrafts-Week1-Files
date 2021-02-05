# Activity 4 

friends = []

while True: 
    friend = input("Enter friend's name or type q to exit: ")
    friends.append(friend)
    print(friend)
    if friend == "q":
        break
