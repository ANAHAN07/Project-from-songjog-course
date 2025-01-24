from module_manager import save_tasks

def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")                  # Output: No tasks available to delete.
        return
    
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} - Status: {task['status']}")                # Output: 1. Project_2 - Status: Pending
                                                                                      #   2. project_1 - Status: Completed
                                                                                      #   3. Minecraft Hypixel Web - Status: Pending
                                                                                      #   4. jjj - Status: Pending
    
    task_num = int(input("\nEnter the task number to delete: ")) - 1            # Output: Enter the task number to delete: 4
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        save_tasks(tasks)
        print("Task deleted successfully!")             # Output: Task deleted successfully!
    else:
        print("Invalid task number.")                   # Output:  Invalid task number.   

        delete_task()
