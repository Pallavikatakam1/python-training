# Tuples + Dictionaries + If-Else


number= int(input("Enter number of students: "))

students = []
for i in range(number):
    name = input(f"Enter name of student {i + 1}: ")
    score = int(input(f"Enter score of {name}: "))
    students.append((name, score))

threshold = int(input("Enter threshold score: "))

score_dict = {name: score for name, score in students}

for name, score in score_dict.items():
    if score > threshold:
        print(f"{name} scored above {threshold}")
