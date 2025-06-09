# 1. Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")
print("\nNumber of vowels:", count_vowels(user_input))


# 2. Reverse a string
def reverse_string(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

user_input = input("\nEnter a string to reverse: ")
print("\nReversed string:", reverse_string(user_input))


# 3. Largest number in the list
def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

user_input = input("\nEnter a list of numbers separated by spaces: ")
number_list = [int(num) for num in user_input.split()]
print("\nLargest number:", find_largest(number_list))


# 4. Palindrome check

def is_palindrome(string1):
    string1 = str(string1)
    return string1 == string1[::-1]

# Get user input
user_input = input("\nEnter a string or number to check for palindrome: ")
if is_palindrome(user_input):
    print("\nIt's a palindrome!")
else:
    print("\nIt's not a palindrome.")



# 5. Fibonacci series

def fibonacci(number):
    a, b = 0, 1
    for _ in range(number):
        print(a, end=' ')
        a, b = b, a + b

number = int(input("\nEnter the number of Fibonacci terms to print: "))
print("\nFibonacci series:")
fibonacci(number)



# 6.Prime numbers in a range
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    for num in range(start, end+1):
        if is_prime(num):
            print(num, end=' ')

start = int(input("\nEnter the start of the range: "))
end = int(input("\nEnter the end of the range: "))

print("Prime numbers between",start," and",end,":")
primes_in_range(start, end)


# 7. Word frequency counter
def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        word = word.lower().strip(".,!?")  # Clean punctuation
        freq[word] = freq.get(word, 0) + 1
    return freq

user_input = input("\nEnter a sentence: ")

frequencies = word_frequency(user_input)
print("Word frequencies:")
for word, count in frequencies.items():
    print(f"{word}: {count}")


# 8. Remove duplicates from a list
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

user_input = input("\nEnter a list of numbers separated by spaces: ")
number_list = [int(num) for num in user_input.split()]

print("\nList after removing duplicates:", remove_duplicates(number_list))



# 9.Sum of digits
def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

user_input = input("\nEnter a number: ")

print("\nSum of digits:", sum_of_digits(user_input))


# 10. Basic file write and read
#  writing to file
text_to_write = input("\nEnter text to write to the file: ")

# Write to file
with open("example.txt", "w") as file:
    file.write(text_to_write)

# Read from file and print
with open("example.txt", "r") as file:
    content = file.read()
    print("\nContent of the file:")
    print(content)


