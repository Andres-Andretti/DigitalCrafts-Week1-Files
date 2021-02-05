
# Add Task

tasks = []

def add():
    
    while True:
        title = input("\nEnter your task: ")
        priority = input("\nEnter priority 'low, med, high': ")

        task = {"title": title, "priority": priority}

        tasks.append(task)

        choice = input("\nEnter q to quit or any key to continue adding: ")
        if choice == "q":
            break           

# View Task

def view():
    for index in range(0, len(tasks)):
        task = tasks[index]
        print(f"{index + 1} - {task['title']} - {task['priority']}")
     
# Delete Task

def delete():
    while True:
        delete_task = int(input("\nWhich task do you wish to delete?: "))
        if delete_task == "q":
            break
        else:
            del tasks[(int(delete_task)) - 1]
            break


while True:
    menu = input("""Press 1 to add a task
Press 2 to delete a task
Press 3 to view all tasks
Press q to quit: """)

    if menu == "1":
        add()
    elif menu == "2":
        view()
        delete()
    elif menu == "3":
        view()
    elif menu == "q":
        break
    else:
        print("You have entered an invalid value. Please try again ")
