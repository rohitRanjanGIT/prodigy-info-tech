import pandas as pd
import os

def createContactCSV():
    if not os.path.exists('contacts.csv'):
        df = pd.DataFrame(columns=['Name', 'Phone', 'Email'])
        df.to_csv('contacts.csv', index=False)
        
def contact_menu():
    print("\nContact Menu")
    print("1. Display all contacts")
    print("2. Add a contact")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Reset contacts")
    print("7. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")

def action(choice):
    df = pd.read_csv('contacts.csv')

    def display_contacts():
        if len(df) <= 0:
            print("No entries found")
        elif len(df.columns) == 3 and all(col in ['Name', 'Phone', 'Email'] for col in df.columns):
            print("No entries found")
        else:
            print(df)


    def add_contact(name, phone, email):
        new_contact = pd.DataFrame({'Name': [name], 'Phone': [phone], 'Email': [email]})
        df_updated = pd.concat([df, new_contact], ignore_index=True)
        df_updated.to_csv('contacts.csv', index=False)
    
    def search_contact(data):
        print("Searching for:", data)
        if data.isdigit():
            print("Searching by Phone")
            result = df[df['Phone'] == data]
        elif '@' in data:
            print("Searching by Email")
            result = df[df['Email'] == data]
        else:
            print("Searching by Name")
            result = df[df['Name'].str.contains(data, case=False, na=False)]
        
        if result.empty:
            print("Contact not found")
        else:
            print("Contact found:")
            print(result)
        return result


    def update_contact(data):
        res = search_contact(data)
        if res.empty:
            return
        print("Field to be updated->\nN: name\nP: phone\nE: email")
        update = input("Enter Field: ").strip().upper()
        if update == 'N':
            new_name = input("Enter new name: ")
            df.loc[res.index, 'Name'] = new_name
        elif update == 'P':
            new_phone = str(input("Enter new phone: "))
            df.loc[res.index, 'Phone'] = new_phone
        elif update == 'E':
            new_email = input("Enter new email: ")
            df.loc[res.index, 'Email'] = new_email
        df.to_csv('contacts.csv', index=False)

    def delete_contact(data):
        res = search_contact(data)
        if not res.empty:
            df.drop(res.index, inplace=True)
            df.to_csv('contacts.csv', index=False)
    
    def reset_contacts():
        df_reset = pd.DataFrame(columns=['Name', 'Phone', 'Email'])
        df_reset.to_csv('contacts.csv', index=False)

    if choice == 1:
        display_contacts()
    elif choice == 2:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        add_contact(name, phone, email)
    elif choice == 3:
        data = input("Enter name, number, or email: ")
        search_contact(data)
    elif choice == 4:
        data = input("Enter name, number, or email: ")
        update_contact(data)
    elif choice == 5:
        data = input("Enter name, number, or email: ")
        delete_contact(data)
    elif choice == 6:
        option = input("Confirm Reset Contacts? (y/n): ")
        if option.lower() == 'y':
            reset_contacts()
        else:
            print("Reset cancelled")

createContactCSV()
choice = contact_menu()

while choice != 7:
    action(choice)
    choice = contact_menu()
print("Exiting Contact Manager...")
