# While Loop + Match (Python 3.10+) + User Input


my_list = []

while True:
    action = input("Enter action (add/remove/print/exit): ").strip().lower()

    match action:
        case "add":
            item = input("Enter item to add: ")
            my_list.append(item)
            print(f"'{item}' added to the list.")
        case "remove":
            item = input("Enter item to remove: ")
            if item in my_list:
                my_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print("Item not in list.")
        case "print":
            print("Current list:", my_list)
        case "exit":
            print("Exiting program.")
            break
        case _:
            print("Invalid command. Please enter add, remove, print, or exit.")

