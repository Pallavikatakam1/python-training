import string
from os.path import split

# Tuple
# 1. Create a Tuple with different data types
my_tuple = (
    int(input("Enter an integer: ")),                  # Integer
    input("Enter a String: "),                         # String
    tuple(map(int, input("Enter tuple values separated by space: ").split())),  # Tuple of integers
    float(input("Enter a Float value: ")),           # Float
    list(map(int, input("Enter list values separated by space: ").split()))  # List of integers
)
print("\nTuple with different data types:", my_tuple)

# 2. Print the second element (string)
print("\nSecond element (String):", my_tuple[1])

# Print the second item of the third element (tuple inside tuple)
if len(my_tuple[4]) > 1:
    print("\nSecond item of the tuple element:", my_tuple[4][1])
else:
    print("\nThe tuple does not have a second item.")

# 3. Tuple immutability
#why the code is  getting error
my_tuple = (1,2,3)
# my_tuple[1] = 4
print("\nIn python, Tuples are immutable. That means after the tuple is created we cannot change or modify or update or the values of the tuple.")
print("In the above line no:24, we are trying to change the value of the tuple in the  position 1 i.e.2 to 4")
print("So, it was showing ann error, if we want to change the value we have to convert the tuple into list and then we can convert.")
print(my_tuple)

# 4. Tuple Unpacking
#Unpack the tuple variables latitude and longitude
# coordinates = (45.4215, -75.6972)
coordinates = (map(float, input("\nEnter the value of latitude and longitude seperated with spaces: "). split()))
latitude, longitude = coordinates
print("\nLatitude: ",latitude,"\nLongitude: ",longitude)


# 5. Tuple Operations
# Element wise sum
tuple1 = (map(int, input("\nEnter tuple numbers separated by space: ").split()))
tuple2 = (map(int, input("Enter tuple numbers separated by space: ").split()))
result = tuple(tuple1 + tuple2 for tuple1, tuple2 in zip(tuple1, tuple2))
print("\nSum of two tuples is: ",result)

#Sets
#Basic set operations
A={1,2,3,4,5}
B={4,5,6,7,8}
# Union
union=A.union(B)
print("\nUnion of A and B: ",union)
# Intersection
intersection=A.intersection(B)
print("\nIntersection of A and B: ",intersection)
#Difference A-B
difference_A_B = A-B
print("\nDifference of A and B: ",difference_A_B)
# Difference B-A
difference_B_A = B-A
print("\nDifference of B and A: ",difference_B_A)
# Symmetric Difference
symmetric_difference = A^B
print("\nSymmetric difference of A and B: ",symmetric_difference)

# 2. Set membership
## check  weather 3 is in set A and 6 in set B
number1 = int(input("\nEnter a number to check in A: "))
number2 = int(input("Enter a number to check in B: "))
if number1 in A:
    print("\nIs",number1,"in A",number1 in A)
if number2 in B:
    print("\nIs",number2,"in B",number2 in B)
if number1 not in A:
    print("\nIs", number1, "in A", number1 in A)
if number2 not in B:
    print("\nIs", number2, "in B", number2 in B)


#Removing Duplicates
# my_list = [1, 2, 2, 3, 4, 4, 5]
list =(map(int, input("\nEnter numbers separated by space to remove duplicates: ").split()))
# Use set to remove duplicates
unique_items = set(list)

print("\nUnique values:", unique_items)


#Set from String
sentence = str(input("\nEnter a sentence: "))

translator = str.maketrans('', '', string.punctuation)
cleaned = sentence.translate(translator).lower()
unique = set(cleaned.split())
print("\nUnique word",unique)

#Students and sports
# Example sets of student names
football = set(map(str, input("\nEnter the list of students who play football with space: ").split()))
basketball = set(map(str, input("Enter the list of students who play basketball with space: ").split()))
tennis = set(map(str, input("Enter the list of students who play tennis with space: ").split()))

# Students who play all three
all_three = football & basketball & tennis

# Students who play only one sport
only_football = football - (basketball | tennis)
only_basketball = basketball - (football | tennis)
only_tennis = tennis - (football | basketball)
only_one_sport = only_football | only_basketball | only_tennis

# Students who play exactly two sports
football_basketball = football & basketball
football_tennis = football & tennis
basketball_tennis = basketball & tennis

# Remove those who play all three
exactly_two = (football_basketball | football_tennis | basketball_tennis) - all_three

print("\nStudents who play all three sports:", all_three)
print("\nStudents who play only one sport:", only_one_sport)
print("\nStudents who play exactly two sports:", exactly_two)


#Dictionaries
#1.Count word Frequencies
input_text = input("\nEnter some words to check the frequency: ")
def count_words(text):
    words = text.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
print(count_words(input_text))

# 2.Merge two dictionaries
dictionary1 = {'a':1, 'p':1, 'e':8, 'q':4,}
dictionary2 = {'a':6, 'b':7, 'c':8, 'e':10}
def merge_dicts(d1, d2):
    merged = d1.copy()

    for key, value in d2.items():
        merged[key] = merged.get(key, 0) + value

    return merged
print("\nMerged dictionaries: ",merge_dicts(dictionary1, dictionary2))

#  3. Invert a Dictionary
def invert_dict(d):
    inverted = {}

    for key, value in d.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)

    return inverted

print("\nInverted Dictionary: ",invert_dict(dictionary1))


# 4. Most Frequent Value
ages = {'Alice': 25, 'Bob': 30, 'Charlie': 25, 'David': 30, 'Eva': 25}
def most_frequent_value(d):
    frequent = {}

    for value in d.values():
        frequent[value] = frequent.get(value, 0) + 1

    # Find the value with the highest frequency
    most_common = max(frequent, key=frequent.get)
    return most_common
print("\nFrequent Age: ",most_frequent_value(ages))

#Dictionary From two Lists
keys = ['name', 'age', 'city']
values = ['Pallavi', '22', 'Hyderabad']
def dictionary(keys, values):
    return dict(zip(keys, values))

print("\nDictionary from two lists: ",dictionary(keys, values))