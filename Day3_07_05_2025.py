# Arithmatic Operator
#Area of the Rectangle
print("To find area of  rectangle")
length = int(input("enter the length of the rectangle: "))
breadth = int(input("enter the breadth of the rectangle: "))
area = length*breadth
print("The area of the rectangle is: ",area)


#Average of three numbers entered by the user
print("\nTo find average of 3 numbers")
number1 = int(input("Enter the First number: "))
number2 = int(input("Enter the Second number: "))
number3 = int(input("Enter the Third number: "))
average = int(number1 + number2 + number3) / 3
print("The average is: ", average)


#Comparision operator
#  Compare two numbers
print("\nTo compare two numbers which is greatest")
number4 = int(input("Enter first number to compare: "))
number5 = int(input("Enter second number to compare: "))
if(number4 > number5):
    print("The greatest number is: ", number4)
elif (number4 == number5):
    print("Both numbers are equal")
else:
    print("The greatest number is: ", number5)


#Checking the person is eligible to vote or not
print("\n Checking for eligibility of vote")
number6 = int(input("Enter your year of birth: "))
age = 2025-number6
if(age >= 18):
    print("Your age is",age,". You are eligible to vote")
elif(age < 0):
    print("Invalid age")
else:
    print("Your age is",age,"You are not eligible to vote")

# Another way
print("\n Checking for eligibility of vote")
number7 = int(input("Enter your present age: "))
if(number7 >= 18):
    print("You are eligible  to vote")
elif(number7 < 0):
    print("Invalid")
else:
    print("You are not eligible to vote")

#Logical Operators
# Range
print("\n To find given number is in range between 10 to 50")
number8 = int(input("Enter the number to verify the range: "))
if(number8 > 10 and number8 < 50):
    print("The number is in the range")
else:
    print("The number is not in the range")

#Valid User or not
print("\nTo check the username and password")
username1 = "Pallavi"
password1 = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == username1 and  password == password1:
    print("Valid User")
else:
  print("Invalid User")

#Assignment Operator
print("\nTo apply the assignment operators")
number9 = int(input("Enter a number: "))
number10 = int(input("Enter a number to verify assignment operators: "))
number9 += number10
print("with += operator: ", number9)
number9 -= number10
print("with -= operator: ", number9)
number9 *= number10
print("with *= operator: ", number9)
number9 /= number10
print("with /= operator: ", number9)

#Bitwise Operators
#Binary numbers
print("\nTo apply bitwise operators")
number11 = int(input("Enter one number: "))
number12 = int(input("Enter another numbers: "))
print("AND operator", number11 & number12)
print("OR operator", number11 | number12)
print("XOR operator", number11 ^ number12)

#Lists
#List Creation and Access
# Ask user to input 5 favorite movies
favorite_movies = []

print("Enter your 5 favorite movies:")
for i in range(5):
    movie = input(f"Movie {i + 1}: ")
    favorite_movies.append(movie)  # append()
print(favorite_movies)

# Add a new movie to the list
new_movie = input("\nEnter one more favorite movie to add: ")
favorite_movies.append(new_movie)  # append()
print("updated list is: ", favorite_movies)

# Change the third movie (index 2)
updated_movie = input("\nEnter a new movie to replace the third one: ")
favorite_movies[2] = updated_movie
print("updated list is: ", favorite_movies)

# Print the first and last movie
print("\nFirst movie:", favorite_movies[0])
print("Last movie:", favorite_movies[-1])

# Sort the list alphabetically
favorite_movies.sort()
print("\nSorted movie list:", favorite_movies)

# Insert a movie at position 2
movie_to_insert = input("\nEnter a movie to insert at position 2: ")
favorite_movies.insert(2, movie_to_insert)
print("After insert:", favorite_movies)

# Remove a movie by name
movie_to_remove = input("\nEnter a movie to remove from the list: ")
if movie_to_remove in favorite_movies:
    favorite_movies.remove(movie_to_remove)  # remove()
    print("After removal:", favorite_movies)
else:
    print(movie_to_remove, "not found in the list.")

# Pop the last movie
popped_movie = favorite_movies.pop()  # pop()
print("\nAfter popping the last movie:", favorite_movies)
print("Popped movie:", popped_movie)

# Reverse the list
favorite_movies.reverse()  # reverse()
print("\nFinal reversed list:", favorite_movies)

# Print each movie using a for loop
print("\nAll movies in the list:")
for movie in favorite_movies:
    print("-", movie)

# Print only movies starting with 'S'
print("\nMovies starting with 'S':")
for movie in favorite_movies:
    if movie.lower().startswith('s'):
        print("-", movie)


#List Comprehension
#list of squares from 1 to 10
print("\nList verification")
squares = [x**2 for x in range(1, 11)]
print("The list of squares from 1 to 10 are: ",squares)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]
print("\nThe even numbers in the list are: ",even_numbers)

#Another method
given_range = int(input("Enter the range of numbers: "))
squares = [x**2 for x in range(given_range)]
even_squares = [list_number for list_number in squares if list_number % 2 == 0]

print("\nThe list of squares from 0 to",given_range,"is: ",squares)
print("\nThe even numbers from the list of squares are: ",even_squares)


