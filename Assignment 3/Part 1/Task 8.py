def is_prime(num):
    
    # Function checks if the given number is prime
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example 
print(is_prime(7))   # Output: True (prime)
print(is_prime(10))  # Output: False (not prime)
