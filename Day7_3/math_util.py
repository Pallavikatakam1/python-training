import sys

# Math functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python math_utils.py <num1> <num2> <operation>")
        print("Example: python math_utils.py 3 4 add")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        operation = sys.argv[3].lower()
    except ValueError:
        print("Error: num1 and num2 must be numbers.")
        sys.exit(1)

    if operation == "add":
        result = add(num1, num2)
    elif operation == "sub":
        result = sub(num1, num2)
    elif operation == "mul":
        result = mul(num1, num2)
    elif operation == "div":
        result = div(num1, num2)
    else:
        print("Error: Operation must be one of: add, sub, mul, div")
        sys.exit(1)

    print("Result:", result)
