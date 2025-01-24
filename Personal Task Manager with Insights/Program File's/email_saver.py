import json

EMAIL_FILE = "emails.json"

def email_saver():
    
    emails = load_emails()
    
    email = input("Enter an email to save: ")                   # Output: Enter an email to save: ahanclientservice@gmail.com
    if "@" in email and "." in email:  
        emails.append(email)
        with open(EMAIL_FILE, "w") as file:
            json.dump(emails, file, indent=4)
        print("Email saved successfully!")                          # Output: Email saved successfully!
    else:
        print("Invalid email address. Please try again.")           # Output: Invalid email address. Please try again.

    email_saver()

def load_emails():
    
    try:
        file = open(EMAIL_FILE, "r")
        emails = json.load(file)
        file.close()
        return emails
    except:
        
        return []
    
    load_emails()
