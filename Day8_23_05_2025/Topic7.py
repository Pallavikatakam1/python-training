# Iterators + For loop

class EvenIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.limit:
            raise StopIteration
        return self.current

try:
    user_limit = int(input("Enter the upper limit for even numbers: "))
    print("Even numbers up to", user_limit, ":")
    for num in EvenIterator(user_limit):
        print(num)
except ValueError:
    print("Please enter a valid integer.")
