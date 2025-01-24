import json

DATA_FILE = "tasks.json"

def load_tasks():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
