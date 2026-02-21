print()
print("Task Tracker")
print()
# display options
print(f"1.Add tasks\n2.View tasks\n3.Delete tasks\n4.Update tasks\n5.Completed tasks\n6.Exit\n")
user_choice = int(input("Select from the list labelled above: "))

# call specific function
def main_function():
    if user_choice == 1:
        # call the add tasks function
        add_tasks()
    elif user_choice == 2:
        # call the view tasks function
        pass
    elif user_choice == 3:
        # call the delete tasks function
        pass
    elif user_choice == 4:
        # call the update tasks function
        pass
    elif user_choice == 5:
        # call the completed tasks function
        pass
    elif user_choice == 6:
        # call the exit task
        pass
    else:
        # display a message for the user
        # to select using numbers 
        pass

# Add tasks
def add_tasks():
    print("Name the task")
    task = str(input("Enter the task: "))
    print("Start Time")
    hour = int(input("Enter the hour: "))
    mins = int(input("Enter the minutes: "))

    # confirm the task
    print(f"Task:{task}, Time:{hour:2d}:{mins:2d}")




# run the program as a script or module
if __name__ == "main":
    main_function()
