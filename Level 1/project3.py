def remove_task(task_list):
    if not task_list:
        print("Task list is empty!")
        return
    view_tasks(task_list)
    try:
        num = int(input("Enter the number of the task to remove: "))
        if 1 <= num <= len(task_list):
            removed_task = task_list.pop(num - 1)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number")
        


    
def view_tasks(task_list):
    if not task_list:
        print("Task list is empty")
    else:
        print("Tasks: ")
        for i, task in enumerate(task_list, 1):
            print(f"{i}.{task}")

def add_task(task_list):
    while True:
        task = input("Enter the task (or type exit to stop): ".strip())
        if not task:
            print ("You cannot add empty line")
        elif task.lower() == 'exit':
            break
        else:
            task_list.append(task)
            print (f"Task added: {task}")

def main():
    task_list = []

    while True:
        try:
            option = int(input("Menu:\n1. Add task\n2. View Task\n3. Remove task\n4.Exit\nEnter your choice: "))
        except ValueError:
            print("Enter valid option (1-4).")
            continue
        if (option == 1):
            add_task(task_list)
        elif (option == 2):
            view_tasks(task_list)
        elif (option == 3):
            remove_task(task_list)
        elif (option == 4):
            print("Exiting program. Bye!")
            break
        else:
            print("Chose option between 1 and 4")
        print("\n")

if __name__ == "__main__":
    main()