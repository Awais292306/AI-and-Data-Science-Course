def largest_number(a, b, c):
    
    # Function returns the largest of the three numbers
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example 
print(largest_number(12, 25, 91))
print(largest_number(100, 55, 100))
