from module_manager import save_tasks

def update_task(tasks):
    if not tasks:
        print("No tasks available to update.")                      # Output:   No tasks available to update.
        return
    
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} - Status: {task['status']}")                    # Output: 1. Project_2 - Status: Pending 
                                                                                         #    2. project_1 - Status: Pending
                                                                                         #    3. Minecraft Hypixel Web - Status: Pending
    
    task_num = int(input("\nEnter the task number to update: ")) - 1                        # Output:  Enter the task number to update: 2
    if 0 <= task_num < len(tasks):
        tasks[task_num]["status"] = input("Enter new status (Pending/Completed): ")             # Output: Enter new status (Pending/Completed): Completed
        save_tasks(tasks)
        print("Task updated successfully!")             # Output:  Task updated successfully!
    else:
        print("Invalid task number.")                   # Output:  Invalid task number.

    update_task()
