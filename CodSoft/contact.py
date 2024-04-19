contacts = []

def add_contact(name, phone_number, email, address):
    contacts.append({"Name": name, "Phone Number": phone_number, "Email": email, "Address": address})
    print("Contact added successfully.")

def view_contact_list():
    if contacts:
        print("Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['Name']}, Phone Number: {contact['Phone Number']}")
    else:
        print("No contacts found.")

def search_contact(query):
    results = [contact for contact in contacts if query.lower() in contact["Name"].lower() or query in contact["Phone Number"]]
    if results:
        print("Search results:")
        for contact in results:
            print(f"Name: {contact['Name']}, Phone Number: {contact['Phone Number']}")
    else:
        print("No matching contacts found.")

def update_contact(index, new_contact):
    if 0 <= index < len(contacts):
        contacts[index] = new_contact
        print("Contact updated successfully.")
    else:
        print("Invalid contact index.")

def delete_contact(index):
    if 0 <= index < len(contacts):
        del contacts[index]
        print("Contact deleted successfully.")
    else:
        print("Invalid contact index.")

def main():
    while True:
        print("\n1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone_number, email, address)
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            search_contact(query)
        elif choice == "4":
            index = int(input("Enter index of contact to update: ")) - 1
            if 0 <= index < len(contacts):
                name = input("Enter name: ")
                phone_number = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                new_contact = {"Name": name, "Phone Number": phone_number, "Email": email, "Address": address}
                update_contact(index, new_contact)
            else:
                print("Invalid contact index.")
        elif choice == "5":
            index = int(input("Enter index of contact to delete: ")) - 1
            delete_contact(index)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
