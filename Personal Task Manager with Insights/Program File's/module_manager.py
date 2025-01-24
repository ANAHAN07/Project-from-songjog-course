import json

DATA_FILE = "tasks.json"

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

    save_tasks()



# This is the main heart of the program. This file manage all the function folders. 
# I took help from Chat Gpt to make the login procedure. I tired to make but so manny errors made me frustrated and i doesn't have enough time to figer out so i just use chat gpt for the login.
# JSON file is a text-based format used to store and exchange structured data between different applications and programming languages.
# No need to download the error_faced.txt file. 