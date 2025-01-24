def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")                # Output: No tasks available.
        return
    print("\nAll Tasks:")                       # Output: All Tasks: 
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} | Category: {task['category']} | Priority: {task['priority']} | Due: {task['due_date']} | Status: {task['status']}")      # Output: 1. Project_2 | Category: Work | Priority: High | Due: 2025-01-24 | Status: Pending
                                                                                                                                                                    #   2. project_1 | Category: study | Priority: Low | Due: 2025-01-15 | Status: Pending
                                                                                                                                                                    #   3. Minecraft Hypixel Web | Category: Work | Priority: High | Due: 2025-03-30 | Status: Pending

    view_tasks()
