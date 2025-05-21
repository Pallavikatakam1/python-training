def func1():
    from module2 import func2  # Delayed import
    print("Function A")
    func2()

if __name__ == "__main__":
    func1()
