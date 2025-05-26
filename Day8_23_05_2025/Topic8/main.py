import mymath
number = 5

def main():
    number = int(input("Enter a number to calculate its factorial: "))
    result = mymath.factorial(number)
    print(f"Factorial of {number} is {result}")
main()
print("Global number remains unchanged: ",number)
