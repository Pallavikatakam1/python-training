# Lists and Loops

user_input = input("Enter numbers separated by space: ")
numbers = list(map(int, user_input.split()))

print("Squares:")
for num in numbers:
    print(num**2, end=' ')
print()

print("Max:", max(numbers))
print("Min:", min(numbers))

