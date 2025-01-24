from login import login
from load_task import load_tasks
from add_task import add_task
from view_tasks import view_tasks
from update_task import update_task
from delete_task import delete_task
from calculator import calculator
from measurement import measurement
from word_counter import word_counter
from email_saver import email_saver
from utiliti_bill import utility_bills

def remainder(tasks):
    
    if tasks:
        print("\n----- Remainder -----")                                                                    # Output: ----- Remainder -----
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['title']} - Due: {task.get('due_date', 'No due date')}")               # Output: 1. Project_2 | Category: Work | Priority: High | Due: 2025-01-24 | Status: Pending
        print("----------------------------------")                                                     # Output: ----------------------------------
    else:
        print("\nNo tasks or reminders to show.")                                                       # Output: No tasks or reminders to show.


def main_menu(username):
    tasks = load_tasks()

    while True:
        print(f"\nWelcome, {username}! Task Manager and Utility Tools")             # Output: Welcome, ahan_07! Task Manager and Utility Tools
        print("1. Add Task")                                                        # Output: 1. Add Task
        print("2. View Tasks")                                                      # Output: 2. View Tasks
        print("3. Update Task")                                                     # Output: 3. Update Task
        print("4. Delete Task")                                                     # Output: 4. Delete Task
        print("5. Advanced Calculator")                                             # Output: 5. Advanced Calculator
        print("6. Measurement Calculator")                                          # Output: 6. Measurement Calculator
        print("7. Word Counter")                                                    # Output: 7. Word Counter
        print("8. Email Saver")                                                     # Output: 8. Email Saver
        print("9. Utiliti Bills Calculator")                                        # Output: 9. Utiliti Bills Calculator
        print("10. Exit")                                                           # Output: 10. Exit

        choice = input("Enter your choice: ")                                       # Output: Enter your choice: []
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            calculator()
        elif choice == "6":
            measurement()
        elif choice == "7":
            word_counter()
        elif choice == "8":
            email_saver()
        elif choice == "9":
            utility_bills()
        elif choice == "10":
            print("Thank you and Goodbye!!")                                 # Output: Thank you and Goodbye!!
            break
        else:
            print("Invalid choice. Please try again.")                       # Output: Invalid choice. Please try again.

if __name__ == "__main__":
    
    username = login()

    main_menu(username)
