def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nAll Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} | Category: {task['category']} | Priority: {task['priority']} | Due: {task['due_date']} | Status: {task['status']}")
