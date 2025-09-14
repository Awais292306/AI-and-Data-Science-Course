# 3. Fruits list operations
fruits = ["apple", "raspberry", "pineapple", "cherry"]

# a. Check if apple is present and get index
if "apple" in fruits:
    print("apple found at index:", fruits.index("apple"))

# b. Replace raspberry and pineapple with orange
fruits[1:3] = ["orange"]
print("After replacing:", fruits)

# c. Insert apricot at index 2
fruits.insert(2, "apricot")
print("After inserting apricot:", fruits)

# d. Extend with car, bike, aeroplane
fruits.extend(["car", "bike", "aeroplane"])
print("Final fruits list:", fruits)

