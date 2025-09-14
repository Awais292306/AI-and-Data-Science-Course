def check_age(age):

    # Function returns message based on the given age
    if age < 18:
        return "You are a Minor."
    elif 18 <= age < 50:
        return "You are an Adult."
    else:
        return "You are a Senior Citizen."

# Example 
print(check_age(15))
print(check_age(47))
print(check_age(61))
