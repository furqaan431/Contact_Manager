import os
import csv

# File where contacts will be stored
CONTACTS_FILE = "contacts.txt"

# Function to load contacts from the file
def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, phone = line.strip().split(',')
                contacts.append({"name": name, "phone": phone})
    return contacts


# Function to save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")


# Function to validate phone numbers (only digits and length of 10)
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


# Function to check if a contact exists (to prevent duplicates)
def contact_exists(name):
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return True
    return False


# Function to add a new contact with validation and duplicate checking
def add_contact(name, phone):
    if not is_valid_phone(phone):
        print("Invalid phone number! Please enter a 10-digit number.")
        return
    if contact_exists(name):
        print(f"Contact {name} already exists.")
        return
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")


# Function to view all contacts, sorted alphabetically by name
def view_contacts():
    contacts = load_contacts()
    if contacts:
        contacts.sort(key=lambda x: x["name"].lower())  # Sort alphabetically by name
        print("\n--- Contact List ---")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts found!")


# Function to search for a contact by part of the name or phone number
def search_contact(query):
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if query.lower() in contact["name"].lower() or query in contact["phone"]:
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}")
            found = True
    if not found:
        print("No matching contacts found!")


# Function to delete a contact by name
def delete_contact(name):
    contacts = load_contacts()
    new_contacts = [contact for contact in contacts if contact["name"].lower() != name.lower()]
    if len(contacts) == len(new_contacts):
        print("Contact not found!")
    else:
        save_contacts(new_contacts)
        print(f"Contact {name} deleted successfully!")


# Function to edit an existing contact's phone number
def edit_contact(name):
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            new_phone = input(f"Enter new phone number for {name}: ")
            if is_valid_phone(new_phone):
                contact["phone"] = new_phone
                save_contacts(contacts)
                print(f"Contact {name} updated successfully!")
            else:
                print("Invalid phone number.")
            return
    print("Contact not found!")


# Function to export contacts to a CSV file
def export_contacts_to_csv():
    contacts = load_contacts()
    with open('contacts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone"])
        for contact in contacts:
            writer.writerow([contact['name'], contact['phone']])
    print("Contacts exported to 'contacts.csv'.")


# Function to import contacts from a CSV file
def import_contacts_from_csv():
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        contacts = []
        for row in reader:
            contacts.append({"name": row[0], "phone": row[1]})
        save_contacts(contacts)
    print("Contacts imported from 'contacts.csv'.")


# Function to backup contacts to a file
def backup_contacts():
    contacts = load_contacts()
    with open('contacts_backup.txt', 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")
    print("Contacts backed up to 'contacts_backup.txt'.")


# Function to restore contacts from a backup file
def restore_contacts():
    if os.path.exists('contacts_backup.txt'):
        with open('contacts_backup.txt', 'r') as file:
            contacts = []
            for line in file:
                name, phone = line.strip().split(',')
                contacts.append({"name": name, "phone": phone})
        save_contacts(contacts)
        print("Contacts restored from backup.")
    else:
        print("No backup file found.")


# Main function to display the menu and handle user input
def main():
    while True:
        print("\n--- Contact Management ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Edit Contact")
        print("6. Export Contacts to CSV")
        print("7. Import Contacts from CSV")
        print("8. Backup Contacts")
        print("9. Restore Contacts")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            search_contact(query)
        elif choice == "4":
            name = input("Enter the name to delete: ")
            delete_contact(name)
        elif choice == "5":
            name = input("Enter the name to edit: ")
            edit_contact(name)
        elif choice == "6":
            export_contacts_to_csv()
        elif choice == "7":
            import_contacts_from_csv()
        elif choice == "8":
            backup_contacts()
        elif choice == "9":
            restore_contacts()
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the app
if __name__ == "__main__":
    main()
