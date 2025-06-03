# Strings

text = input("Enter a string: ")

# Reverse string
print("Reversed:", text[::-1])

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
print("Vowel Count:", vowel_count)

# Palindrome check
print("Palindrome" if text == text[::-1] else "Not Palindrome")
