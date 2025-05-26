# Lambda + Filter + Map + Reduce

from functools import reduce

try:
    user_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, user_input.split()))

    odd_nums = list(filter(lambda x: x % 2 != 0, nums))
    squared = list(map(lambda x: x ** 2, odd_nums))
    sum_squares = reduce(lambda x, y: x + y, squared) if squared else 0

    print("Sum of squares of odd numbers:", sum_squares)

except ValueError:
    print("Please enter only integers separated by spaces.")

