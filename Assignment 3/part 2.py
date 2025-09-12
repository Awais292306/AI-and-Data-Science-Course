
# Familiarizing with List Data Structure in Python


# Creating a list of numbers
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)

# 1. Accessing elements by index
print("First element:", numbers[0])   # 10
print("Last element:", numbers[-1])  # 50

# 2. Slicing (getting a part of the list)
print("First 3 elements:", numbers[:3])   # [10, 20, 30]

# 3. Adding elements
numbers.append(60)         # adds 60 at the end
print("After append:", numbers)

numbers.insert(2, 25)      # inserts 25 at index 2
print("After insert:", numbers)

numbers.extend([70, 80])   # adds multiple elements
print("After extend:", numbers)

# 4. Removing elements
numbers.remove(25)         # removes first occurrence of 25
print("After remove:", numbers)

popped = numbers.pop()     # removes last element
print("After pop:", numbers, " (Popped element:", popped, ")")

del numbers[0]             # deletes first element
print("After del:", numbers)

# 5. Searching and counting
print("Index of 30:", numbers.index(30))  # position of 30
print("Count of 40:", numbers.count(40))  # how many times 40 appears

# 6. Sorting and reversing
numbers.sort()             # ascending order
print("Sorted list:", numbers)

numbers.sort(reverse=True) # descending order
print("Sorted (reverse):", numbers)

numbers.reverse()          # reverses order
print("Reversed list:", numbers)

# 7. Copying the list
copy_numbers = numbers.copy()
print("Copied List:", copy_numbers)

# 8. Useful built-in functions
print("Length of list:", len(numbers))
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Sum of values:", sum(numbers))

# 9. Looping through the list
print("Looping through list:")
for num in numbers:
    print(num)
