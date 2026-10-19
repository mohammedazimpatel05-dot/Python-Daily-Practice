def outer(x):
    def inner(y):
        return x * y  # Added the '*' operator
    return inner

# Example usage:
multiply_by_5 = outer(5)
print(multiply_by_5(3))  # Output: 15
