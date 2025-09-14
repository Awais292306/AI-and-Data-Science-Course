def factorial(n):
    
    # Base case factorial 
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)

# Example
print(factorial(3))
print(factorial(6))
