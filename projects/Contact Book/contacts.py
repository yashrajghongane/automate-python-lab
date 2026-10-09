 #Contact Temp Storege in JSON
from pathlib import Path
import json

SCRIPT_DIR = Path(__file__).parent
CONTACT_file = SCRIPT_DIR / "Contact.json"

users_list = []
next_id = 1

def save_contacts():
        with open(CONTACT_file,mode="w" , encoding='utf-8') as file:
            json.dump(users_list,file,indent=4)
        print("Contact saved!")

def load_contacts():
    global users_list
    try:
        with open(CONTACT_file,mode="r" , encoding='utf-8') as file:
            users_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users_list = []


def main():
    load_contacts()
    print("Welcome to the Contact Book!")
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Clear All Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            clear_list()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def ask_name():
        name = input("Enter The your Name : ")
        return name

def ask_number():
    while True:
        number = input("Enter the your Number : ")
        if number.isdigit() and len(number) == 10:
            return number
        else:
            print("Invalid Number, Enter Valid Number.")

def ask_email():
    while True:
        email = input("Enter the your Email : ")
        if "@" in email and "." in email:
            return email
        else:
            print("Invalid Email Enter The correct Email")

def add_contact():
    global next_id
    # then current id 
    current_id = next_id
    next_id += 1
    try:
        name = ask_name()
        number = ask_number()
        email = ask_email()
    except ValueError as e:
        print(e)

    add_dict = {
        "id":current_id,
        "name": name,
        "number":number,
        "email":email
    }
    users_list.append(add_dict)
    print("Contact added..")
    save_contacts()

def view_contacts():
    if users_list:
        for user in users_list:
            print(f" ID : {user['id']} , Name : {user['name']} , Number : {user['number']} , Email : {user['email']}")
    else:
        print("There is Not any Contacts Are avaible")

def clear_list():
    """Clears all contacts from the global list."""
    global users_list, next_id
    users_list = []  
    next_id = 1
    print("All contacts have been cleared!")
    save_contacts()

def delete_contact():
    while True:
        try:
            id_del = int(input("Enter ID to Delete : "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid numerical ID.")

    for user in users_list:
        if user['id'] == id_del:
            users_list.remove(user)
            print(f"User with ID {id_del} has been removed.")
            break
    else:
        print(f"No user found with ID {id_del}")
    save_contacts()
main()