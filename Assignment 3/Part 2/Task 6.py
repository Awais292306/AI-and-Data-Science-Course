# 6. Gadgets list operations
gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

# a. Separate strings and numbers
gadget_strings = [g for g in gadgets if isinstance(g, str)]
gadget_numbers = [g for g in gadgets if isinstance(g, (int, float))]

print("String list:", gadget_strings)
print("Number list:", gadget_numbers)

# b. Sort string list ascending & descending
print("Strings Ascending:", sorted(gadget_strings))
print("Strings Descending:", sorted(gadget_strings, reverse=True))

# c. Sort strings by length
print("Strings by length:", sorted(gadget_strings, key=len))

# d. Sort numbers ascending & descending
print("Numbers Ascending:", sorted(gadget_numbers))
print("Numbers Descending:", sorted(gadget_numbers, reverse=True))
