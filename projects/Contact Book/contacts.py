 #Contact Temp Storege in List Of Dict
users_list = []

def main():
    print("Welcome to the Contact Book!")
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Clear All Contact")
        #print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            clear_list()
        #elif choice == '4':
            #delete_contact()
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
        global email
        email = input("Enter the your Email : ")
        if "@" in email and "." in email:
            return email
        else:
            print("Invalid Email Enter The correct Email")

def add_contact():
    # check_current id's in user list
    id_count = len(users_list)
    # then current id 
    current_id = id_count + 1
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

def view_contacts():
    if users_list:
        for user in users_list:
            print(f"Name : {user['name']} , Number : {user['number']} , Email : {user['email']}")
    else:
        print("There is Not any Contacts Are avaible")

def clear_list():
    """Clears all contacts from the global list."""
    global users_list  
    users_list = []  
    print("All contacts have been cleared!")


main()