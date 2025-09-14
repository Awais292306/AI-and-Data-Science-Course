# Original list

student = ["Awais", 57, "AI and Data Science", True]

# 2. Strings, numbers and Boolean in separate lists

strings = []
numbers = []
booleans = []

for item in student:
    if isinstance(item, str):
        strings.append(item)
    elif isinstance(item, (int, float)) and not isinstance(item, bool):
        numbers.append(item)
    elif isinstance(item, bool):
        booleans.append(item)

# Example 
print("Strings:", strings)
print("Numbers:", numbers)
print("Booleans:", booleans)

