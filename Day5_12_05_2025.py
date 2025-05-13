# 1. Match Statement - Day of the week
Day = int(input("Enter the number from 1 to 7: "))
match Day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid input")



# 2. For Loop - Multiplication table
number = int(input("\nEnter a number to print the table: "))
for i in range(1,11):
    print(number,"*",i,"=",number*i)


#While loop - Number Guessing game
import random
number1 = random.randint(1,100)
attempts = 0
while True:
    guess = int(input("\nGuess a number between 1 and 100: "))
    attempts += 1
    if guess < number1:
        print("Sorry, guess too low.")
    elif guess > number1:
        print("Sorry, guess too high.")
    else:
        print("You guessed my number in {} attempts.".format(attempts))
        break


# 4. Function - Prime number checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
primes = [str(i) for i in range(1, 101) if is_prime(i)]
number2 = int(input("\nEnter a number to check weather prime or not: "))
if is_prime(number2):
    print("\n",number2," is prime number")
    print("Prime numbers between 1 and 100:", ", ".join(primes))
else:
    print("\n",number2," is not prime number")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number3 = int(input("\nEnter the start of the range: "))
number4 = int(input("Enter the end of the range: "))

print("Prime numbers between", number3, "and", number4, "are:")

for num in range(number3, number4 + 1):
    if is_prime(num):
        print(num, end=" ")

# 5. Lambda -  Sorting a list of Tuples
people = []
number5 = int(input("\n\nEnter the number of people: "))
for i in range(number5):
    name = input(f"Enter name of person {i+1}: ")
    age = int(input(f"Enter age of {name}: "))
    people.append((name, age))
sorted_people = sorted(people, key=lambda x: x[1])
print("\nPeople sorted by age:")
for person in sorted_people:
    print(person[0]," - ",person[1], "years old")

# 6. Arrays - Reverse an Array
array = input("\nEnter an array of numbers: ")
reversed_array = array[::-1]
print("The reversed array is:", reversed_array)

#Class and Object
class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print("The amount of",amount,"is deposited successfully")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("The amount of",amount,"is withdrawn successfully")
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("Current balance is",self.balance)

account1 = BankAccount()
while True:
    print("\n  Choose an option you want: ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = input("\nEnter your choice(1-4): ")
    if choice == "1":
        amount = float(input("Enter the amount of deposit: $"))
        account1.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter the amount of withdraw: $"))
        account1.withdraw(amount)
    elif choice == "3":
        account1.check_balance()
    elif choice == "4":
        print("Thank you for using our application")
        break
    else:
        print("Invalid choice. Please try again.")


# 8. For Loop - Fibonacci Series
fibonacci = int(input("\nEnter the number of Fibonacci terms to generate: "))

number6 = 0
number7 = 1

print("Fibonacci series:")
for i in range(fibonacci):
    print(number6, end=", " if i < fibonacci - 1 else "")
    number6, number7 = number7, number6 + number7


# 9. While loop - Factorial Calculation
number8 = int(input("\n\nEnter a number to find factorial: "))
factorial = 1
for i in range(1, number8 + 1):
    factorial *= i
print("The factorial of  given number is: ",factorial)


# 10. Function - Palindrome Checker
def is_palindrome(word):
    return word == word[::-1]

words = str(input("\nEnter a word to check it is palindrome or not: "))

if is_palindrome(words):
    print(words,"is a palindrome")
else:
    print(words,"is not a palindrome")


