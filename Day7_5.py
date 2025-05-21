def outer_function():
    message = "Hello"

    def inner_function():
        nonlocal message  # Refer to the variable from outer_function
        print("Inside inner_function - before change:", message)
        message = "Hi from inner function"
        print("Inside inner_function - after change:", message)

    print("Before calling inner_function:", message)
    inner_function()
    print("After calling inner_function:", message)

outer_function()
