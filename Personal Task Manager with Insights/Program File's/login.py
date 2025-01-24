import json

LOGIN_FILE = "users.json"

def load_users():
    
    try:
        with open(LOGIN_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  
    
    load_users()

def save_users(users):
    
    with open(LOGIN_FILE, "w") as file:
        json.dump(users, file, indent=4)

    save_users()

def login():
    
    users = load_users()
    
    print("Welcome to Task Manager and Utility Tools!")            # Output: Welcome to Task Manager and Utility Tools!              
    print("Please log in or register to continue.\n")              # Output: Please log in or register to continue.          

    while True:
        print("1. Login")                                           # Output: 1. Login                          
        print("2. Register")                                        # Output: 2. Register                         
        print("3. Exit")                                            # Output: 3. Exit                         
        choice = input("Enter your choice: ").strip()               # Output: Enter your choice: 2                       

        if choice == "1":  
            username = input("Enter your username: ").strip()       # Output: Enter your username: ahan_07                         
            password = input("Enter your password: ").strip()        # Output: Enter your password: 1234                        

            if username in users and users[username] == password:
                print(f"\nLogin successful! Welcome, {username}!")          # Output: Login successful! Welcome, ahan_07!                 
                return username
            else:
                print("Invalid username or password. Please try again.\n")       # Output: Invalid username or password. Please try again.            

        elif choice == "2":  
            username = input("Enter a new username: ").strip()                          # Output: Enter a new username: ahan_07            
            if username in users:
                print("Username already exists. Please choose a different username.\n")       # Output: Username already exists. Please choose a different username.1       
            else:
                password = input("Enter a new password: ").strip()                         # Output: Enter a new password: 1234      
                users[username] = password
                save_users(users)
                print("Registration successful! You can now log in.\n")                  # Output: Registration successful! You can now log in.

        elif choice == "3":  
            print("Exiting... Goodbye!")                                         # Output: Exiting... Goodbye!
            exit()

        else:
            print("Invalid choice. Please try again.\n")                    # Output: Invalid choice. Please try again.

        login()