# Dictionaries + List  comprehension + if - else


salaries = {}
try:
    number = int(input("How many employees? "))
    for _ in range(number):
        name = input("Enter employee name: ")
        salary = int(input(f"Enter salary for {name}: "))
        salaries[name] = salary

    labels = {name: ('High' if salary > 100000 else 'Low') for name, salary in salaries.items()}

    print("\nSalary Labels:")
    print(labels)
except ValueError:
    print("Invalid input. Please enter numeric values for salaries.")
