# Sets + For loop + Lambda

def unique_squared_sorted(nums):
    unique = set(nums)
    squared = [x**2 for x in unique]
    return sorted(squared)

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = unique_squared_sorted(nums)
print("Sorted squares of unique numbers:", result)

