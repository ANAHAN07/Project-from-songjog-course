from module_manager import save_tasks

def add_task(tasks):
    
    name = input("Enter the task name: ").strip()                                           # Output:  Enter the task name: Minecraft Hypixel Web  
    category = input("Enter the task category (Work, Study, Personal): ").strip()           # Output:  Enter the task category (Work, Study, Personal): Work
    priority = input("Enter the task priority (High, Medium, Low): ").strip()               # Output:  Enter the task priority (High, Medium, Low): High
    due_date = input("Enter the due date (YYYY-MM-DD): ").strip()                           # Output:  Enter the due date (YYYY-MM-DD): 2025-03-30

    
    task = {
        "name": name,
        "category": category if category else "Uncategorized",
        "priority": priority if priority else "Medium",
        "due_date": due_date if due_date else "No due date",
        "status": "Pending"  
    }

    
    tasks.append(task)
    save_tasks(tasks)
    print("\nTask added successfully!")                 # Output:   Task added successfully!

    add_task()