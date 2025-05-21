import math_util

def main():
    print("Simple Calculator")
    print("Choose the option you want to do: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))
    try:
        number1 = float(input("Enter your first number: "))
        number2 = float(input("Enter your second number: "))
    except ValueError:
        print("Invalid input")
        return
    if choice == 1:
        result = math_util.add(number1, number2)
        print("The result is: ", result)
    elif choice == 2:
        result = math_util.subtract(number1, number2)
        print("The result is: ", result)
    elif choice == 3:
        result = math_util.multiply(number1, number2)
        print("The result is: ", result)
    elif choice == 4:
        result = math_util.divide(number1, number2)
        print("The result is: ", result)
    else:
        print("Invalid input")
if __name__ == "__main__":
    main()