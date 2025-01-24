import json

TASK_FILE = "tasks.json"

def load_tasks():
    
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except:
        return []

    load_tasks()  

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

    save_tasks()
