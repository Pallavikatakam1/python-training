# Basic contact book

contacts = {}

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Exit")
    choice = input("Choose: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
    elif choice == '2':
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == '3':
        name = input("Enter name to search: ")
        print("Name:", contacts.get(name, "Not Found"))
    elif choice == '4':
        break
    else:
        print("Invalid option.")
