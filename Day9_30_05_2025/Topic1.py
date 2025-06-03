# Variables and Data types

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in feet): "))
is_student_input = input("Are you a student? (yes/no): ").strip().lower()
is_student = is_student_input == "yes"

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))




