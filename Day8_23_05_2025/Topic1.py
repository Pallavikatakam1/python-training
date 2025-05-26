# operators + Lists + Functions

list1 = list(map(int, input("Enter elements of first list separated by spaces: ").split()))
list2 = list(map(int, input("Enter elements of second list separated by spaces: ").split()))
def sum_lists(list1, list2):
    max_len = max(len(list1), len(list2))
    list1 += [0] * (max_len - len(list1))
    list2 += [0] * (max_len - len(list2))
    return [a + b for a, b in zip(list1, list2)]
result = sum_lists(list1, list2)
print("Result:", result)


