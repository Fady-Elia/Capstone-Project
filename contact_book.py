import csv
from datetime import datetime


def create_contact(username, email, phone_numbers, address):
    # Get the current insertion date and time
    insertion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create a contact list with the provided details
    contact = [username, email, phone_numbers, address, insertion_date]
    # Open the file in append mode and write the contact details as a row
    with open(get_filename(), 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(contact)
    print("Contact created successfully!")


def update_contact(username, email, phone_numbers, address):
    # Read all contacts from the file
    contacts = read_contacts()
    updated_contacts = []
    for contact in contacts:
        if contact[0] == username:
            # If the contact's username matches the provided one, update the details and insertion date
            insertion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            updated_contact = [username, email, phone_numbers, address, insertion_date]
            updated_contacts.append(updated_contact)
        else:
            # For other contacts, keep them as they are
            updated_contacts.append(contact)
    # Write the updated contacts back to the file
    write_contacts(updated_contacts)
    print("Contact updated successfully!")


def delete_contact(username):
    # Read all contacts from the file
    contacts = read_contacts()
    # Filter out the contact with the provided username
    updated_contacts = [contact for contact in contacts if contact[0] != username]
    # Write the updated contacts back to the file
    write_contacts(updated_contacts)
    print("Contact deleted successfully!")


def list_contacts(sort_by='insertion_date'):
    # Read all contacts from the file
    contacts = read_contacts()
    if sort_by == 'insertion_date':
        # Sort contacts by insertion date
        contacts.sort(key=lambda x: x[4])
    elif sort_by == 'username':
        # Sort contacts by username
        contacts.sort(key=lambda x: x[0])
    else:
        print("Invalid sort option. Sorting by insertion date.")
        contacts.sort(key=lambda x: x[4])
    # Print the sorted contacts with their details
    for contact in contacts:
        print(f"Username: {contact[0]}, Email: {contact[1]}, Phone Numbers: {contact[2]}, "
              f"Address: {contact[3]}, Insertion Date: {contact[4]}")


def get_filename():
    # Get the current date to generate the file name
    date = datetime.now().strftime("%m%d%Y")
    return f"contactbook_{date}.csv"


def read_contacts():
    # Open the file and read all contacts as a list
    with open(get_filename(), 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
    return contacts


def write_contacts(contacts):
    # Open the file and write the contacts as rows
    with open(get_filename(), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)


def main():
    while True:
        print("\n==== Contact Book ====")
        print("1. Create contact")
        print("2. Update contact")
        print("3. Delete contact")
        print("4. List contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            phone_numbers = input("Enter phone numbers (comma-separated): ").split(',')
            address = input("Enter address: ")
            create_contact(username, email, phone_numbers, address)

        elif choice == '2':
            username = input("Enter username of the contact to update: ")
            email = input("Enter new email: ")
            phone_numbers = input("Enter new phone numbers (comma-separated): ").split(',')
            address = input("Enter new address: ")
            update_contact(username, email, phone_numbers, address)

        elif choice == '3':
            username = input("Enter username of the contact to delete: ")
            delete_contact(username)

        elif choice == '4':
            print("\n==== List Contacts ====")
            print("1. Sort by insertion date")
            print("2. Sort by username")
            sort_choice = input("Enter your choice (1-2): ")
            if sort_choice == '1':
                list_contacts('insertion_date')
            elif sort_choice == '2':
                list_contacts('username')
            else:
                print("Invalid choice. Listing contacts sorted by insertion date.")
                list_contacts('insertion_date')

        elif choice == '5':
            print("Exiting Contact Book...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
