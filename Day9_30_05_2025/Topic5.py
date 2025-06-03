# Functions

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number for factorial and prime check: "))
print("Factorial: ",factorial(num))
print("Prime" if is_prime(num) else "Not Prime")
