def check_result(score):
    
    # Function checks if the user passed or failed
    if score > 60:
        return "Pass"
    else:
        return "Fail"

# Example
print(check_result(69))
print(check_result(43))

