# Dictionaries

students = {}

while True:
    print("\nChoose an option:")
    print("1. Add/Update Student")
    print("2. Delete Student")
    print("3. View All Students")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        score = int(input("Enter score: "))
        students[name] = score
        print("Student ",name," added/updated.")

    elif choice == '2':
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student ",name," deleted.")
        else:
            print("Student not found.")

    elif choice == '3':
        if students:
            print("\nStudent Scores:")
            for name, score in students.items():
                print("Name: ",name, " Score: ",score)
        else:
            print("No student records available.")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please select 1-4.")
