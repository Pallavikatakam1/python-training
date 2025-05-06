#Reverse a String
string1 = str(input("enter a string to reverse it: "))
txt = string1[::-1]
print(txt)
print("--------------")

#Check if String is Palindrome or not
string2 = str(input("enter your string to check Palindrome or not: "))
string2 = string2.casefold()
string3 = reversed(string2)
if list(string2) == list(string3):
    print("Palindrome")
else:
    print("Not Palindrome")

print("---------------")

#Count vowels and consonants in a string
vowel = 0
consonant = 0
string4 = input("enter your string to check vowels and consonants: ")
string4 = string4.lower()
for char in range(0, len(string4)):
    if string4[char] in ("a","e","i","o","u"):
        vowel = vowel + 1
    elif (string4[char] >= 'a' and string4[char] <= 'z'):
        consonant = consonant + 1

print("vowel count: ", vowel)
print("consonant count: ", consonant)
print("remaining all are not alphabetic ")
print("---------------")


# Find frequency of each character (ignoring spaces)
string5 = input("Enter a string to verify frequency: ")
frequency = {}

for char in string5:
    if char == " ":
        continue
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency:", frequency)
print("---------------")


#Remove all white spaces from a string
string6 = input("Enter a string to remove white spaces: ")
no_whitespace = string6.replace(" ", "")
print("String without spaces: ", no_whitespace)
print("---------------")


#Replace a word in a sentence
string7 = input("Enter a sentence to word replace: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
updated_sentence = string7.replace(old_word, new_word)
print("Updated sentence: ", updated_sentence)
print("---------------")


#Extract digits from a string
string8 = input("Enter a string to extract digits: ")
digits = ''.join(char for char in string8 if char.isdigit())
print("Extracted digits: ", digits)
print("---------------")


#Check if a string contains only alphabets
string9 = input("enter your string to verify for alphabet or not: ")
result = string9.isalpha()
print("Contains only alphabets?", result)
print("---------------")


#Captalize the first letter of the string
string10 = input("Enter a string: ")
capitalized = string10.title()
print("Capitalized string:", capitalized)


